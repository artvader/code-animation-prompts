# Install to Claude Code / Codex

This repository is for Claude Code and Codex with local file and terminal capabilities. First download the complete repository (including the original video, about 75 MiB, and README pictures), and install the entire directory of `skills/code-animation-prompts/`.

## Give the assistant a sentence

[Copy one-click import prompt words](../prompts/one-click-import.md). The assistant downloads the repository, reads the description, selects the installation location for the current tool, and validates the style query.

## Python installation script

Requires Python 3.10+ and does not rely on third-party packages. Run in the root directory of the repository:

```bash
python scripts/install_skill.py --target codex
python scripts/install_skill.py --target claude
```

Just choose one of them. `--target both` will be installed in two locations. `--dry-run` only displays the path and does not write the file.

| Tools | User-level directory | Project-level directory |
|---|---|---|
| Codex | `~/.agents/skills/code-animation-prompts/` | `<project>/.agents/skills/code-animation-prompts/` |
| Claude Code | `~/.claude/skills/code-animation-prompts/` | `<project>/.claude/skills/code-animation-prompts/` |

`~` refers to the user's home directory; Windows is usually `C:\Users\username`. The paths are organized according to [OpenAI official skills document](https://learn.chatgpt.com/docs/build-skills) and [Claude Code official skill documents](https://code.claude.com/docs/en/skills).

Install to specified project:

```bash
python scripts/install_skill.py --target codex --scope project --project-dir "your project path"
python scripts/install_skill.py --target claude --scope project --project-dir "your project path"
```

Do not repeatedly install skills with the same name at the user level and project level of the same assistant at the same time to avoid multiple entries with the same name.

## Not using Python

Manually copy the entire `skills/code-animation-prompts/` directory in the repository to the location in the table. Eventually there should be:

```text
<installation-directory>/code-animation-prompts/SKILL.md
<installation-directory>/code-animation-prompts/assets/library/style-picker.html
<installation-directory>/code-animation-prompts/references/catalog.json
```

Just copying `SKILL.md` will lose the style library. Do not change the relative positions between files within `assets/library/`.

## Verify installation

Replace `<skill-directory>` with the real installation path:

```bash
python "<skill-directory>/scripts/styles.py" search ink
python "<skill-directory>/scripts/styles.py" show B3
```

After starting a new session, Codex can enter `$code-animation-prompts`; Claude Code can enter `/code-animation-prompts`. You can also just say "use code-animation-prompts to create an animation." If the new skill does not appear in the current session, restart the session; account or administrator settings may affect skill discovery.

## renew

The installation script does not overwrite existing directories. Before updating, save your modifications and back up the old skill directory outside of the skill scanning directory; then pull the repository and rerun the installation command. Do not leave a backup with `SKILL.md` underneath `.agents/skills/` or `.claude/skills/`, or it may still be scanned.

Update the material index in the repository and check the integrity:

```bash
python scripts/build_catalog.py
python scripts/validate_repo.py
```

## Optional: Video export

Installing the skill will not automatically install the browser or FFmpeg. When you need to actually export the video, click [Rendering Instructions](../skills/code-animation-prompts/references/rendering.md) to configure dependencies.

[Return to README](../README.md)
