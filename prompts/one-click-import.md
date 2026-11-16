# Import prompt words with one click

Copy the entire paragraph below to Claude Code or Codex with local file and terminal permissions.

```text
Please install https://github.com/XiaoyeCodes/code-animation-prompts as a skill available to the current programming assistant.

1. Download the repository to a suitable local directory; if there is already a directory with the same name, check the content first and do not overwrite existing changes.
2. Read README.md, docs/INSTALL.md, and skills/code-animation-prompts/SKILL.md.
3. Select the installation target based on the current assistant: Codex uses ~/.agents/skills/code-animation-prompts,
   Claude Code uses ~/.claude/skills/code-animation-prompts.
   Run python scripts/install_skill.py --target codex or --target claude in the root directory of the repository.
   Just confirm the target with me if the current assistant can't determine it; don't install in two locations without permission.
4. Keep the complete skill folder during installation, including all prompt words, still frames, HTML,
   Sample video and license file. If the target already exists, the existing directory is retained and reported, and is not automatically deleted or overwritten.
5. Execute scripts/styles.py search ink in the installed directory to confirm that the style can be found;
   Then execute scripts/styles.py show B3 to confirm that the complete prompt word can be read.
6. Tell me the actual installation path, how to call it, and whether you need to open a new session.
   Finally, give me a request example of "12 seconds particle polymorph animation" that can be used directly.

This time, only the style skill will be installed, the video rendering dependencies will not be automatically installed, and other assistant configurations will not be modified.
```

[Return to README](../README.md)
