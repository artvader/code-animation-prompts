"""Check output-language instructions across docs and embedded prompt copies."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHINESE_OUTPUT = re.compile(
    r"\bChinese\s+(?:subtitles?|captions?|narration|voiceovers?|headings|baseline|"
    r"labels?|line|name)\b|"
    r"\b(?:spoken|dubbed|narrated|subtitled)\s+in\s+Chinese\b|"
    r"\bidiomatic\s+Chinese\b|\ba Chinese character\b|"
    r"\b(?:use|write|render|display|output)\s+Chinese\s+(?:text|characters?|speech)\b",
    re.IGNORECASE,
)


class EnglishOutputTest(unittest.TestCase):
    def test_documented_and_embedded_instructions_use_english(self):
        matches = []
        for path in ROOT.rglob("*"):
            relative = path.relative_to(ROOT)
            if any(part in {".git", ".build", ".vibe-wise", "tests", "__pycache__"}
                   for part in relative.parts):
                continue
            if path.name in {"source-manifest.json", "library-changes.json"}:
                continue  # Historical upstream paths and contribution records.
            if path.suffix not in {".md", ".html", ".json", ".yaml", ".yml", ".js", ".py", ".txt", ".svg"}:
                continue
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                for match in CHINESE_OUTPUT.finditer(line):
                    matches.append(f"{relative}:{number}: {match.group()}")
        self.assertEqual(matches, [], "Chinese-output instructions remain:\n" + "\n".join(matches))


if __name__ == "__main__":
    unittest.main()
