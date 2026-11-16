import hashlib
from pathlib import Path
import tempfile
import unittest

from scripts.validate_repo import validate_library


class LibraryRenamesTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.library = Path(self.temp.name)
        self.digest = hashlib.sha256(b"prompt").hexdigest()
        self.manifest = {"file_count": 1, "files": {"original.md": self.digest}}
        self.changes = {"modified": {}, "added": {}, "contributions": {},
                        "renamed": {"original.md": "english.md"}}
        (self.library / "english.md").write_bytes(b"prompt")

    def test_rename_preserves_original_checksum(self):
        self.assertEqual(validate_library(self.library, self.manifest, self.changes), (1, 0, 0))

    def test_renamed_file_tampering_is_rejected(self):
        (self.library / "english.md").write_bytes(b"changed")
        with self.assertRaisesRegex(AssertionError, "Unexpected library change"):
            validate_library(self.library, self.manifest, self.changes)

    def test_case_insensitive_collision_is_rejected(self):
        self.manifest["files"]["other.md"] = self.digest
        self.manifest["file_count"] = 2
        self.changes["renamed"]["other.md"] = "ENGLISH.md"
        with self.assertRaisesRegex(AssertionError, "collide"):
            validate_library(self.library, self.manifest, self.changes)

    def test_path_outside_library_is_rejected(self):
        self.changes["renamed"]["original.md"] = "../outside.md"
        with self.assertRaisesRegex(AssertionError, "Invalid renamed path"):
            validate_library(self.library, self.manifest, self.changes)


if __name__ == "__main__":
    unittest.main()
