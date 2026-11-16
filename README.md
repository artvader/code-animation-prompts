> This local edition translates the documentation, all 341 style prompts, catalog, picker, and filenames into English using machine translation. Some technical wording may need review. Text embedded in supplied images and videos is unchanged. Original paths and checksums are retained only in historical provenance records.

<div align="center">

<img src="docs/images/promo-hq.gif" alt="Code Animation Prompts — 24.5-second promotional video featuring 341 animation styles" width="100%">

# Code Animation Prompts

**From a creative idea to a stylish code animation.**

341 style prompts · 196 reference stills · 10 series · Claude Code & Codex Skill

[![Styles](https://img.shields.io/badge/styles-341-b7f47b?style=flat-square&labelColor=161d28)](docs/STYLES.md)
[![Stills](https://img.shields.io/badge/reference_stills-196-86b7ff?style=flat-square&labelColor=161d28)](docs/images/style-gallery.png)
[![Skill](https://img.shields.io/badge/Agent_Skill-Claude_Code_%26_Codex-e6ceaa?style=flat-square&labelColor=161d28)](skills/code-animation-prompts/SKILL.md)
[![Sharing](https://img.shields.io/badge/sharing-free-ecb7cc?style=flat-square&labelColor=161d28)](LICENSE.md)

[Browse all styles](docs/STYLES.md) · [One-click import](#one-click-import-claude-code--codex) · [Manual installation](docs/INSTALL.md) · [Original example](skills/code-animation-prompts/assets/library/examples) · [Source and license](LICENSE.md)

</div>

## Explore the styles

Particles, neon, ink, paper cutting, comics, movie feel... Give your favorite picture to AI, and then use code to animate it.

![12 styles of authentic reference stills](docs/images/style-gallery.png)

The above pictures are from the reference still frames that come with the material package, and the numbers correspond to the prompt words one-to-one. **196 have images, 145 are text references**; still frames show visual direction, actual animation depends on content, implementation and rendering results.

| What you want to do | You can start here |
|---|---|
| Warm particle narrative/title | **B3** Particle aggregation,**B2** Firefly dust |
| National style title/festival short film | **Z5** paper-cutting,**Z1** ink painting,**Z8** Dunhuang |
| Sense of Technology/Cyber City | **R1** Neon Rainy Night,**R5** Pixel Cyber,**R6** Oriental Cyber |
| Popular science/knowledge explanation | **M1** whiteboard hand-drawn explanation,**L10** project plan comparison wall |
| Comic shorts/impactful expressions | **R3** American comics,**X7** hero comics |
| Magazine layout/movie visual reference | **H1** Biennale Yellow,**O** series |

## What does it contain

| Composition | What you can do with it |
|---|---|
| **Material Library and Community Supplement** | Read 341 Markdown prompts, view still frames, reference implementations and original examples |
| **Offline style picker** | Search, filter by category, enlarge image, check style, export selected list |
| **Agent Skill can be installed** | Let Claude Code/Codex read styles on demand, plan shots and create code animations |
| **Lightweight search script** | Search by number, keyword, series; no need to stuff the entire material library into the context |
| **Browser Rendering Tool** | Export HTML that provides a time interface to MP4 frame by frame, and can mix in existing audio |
| **One-click import prompt words** | Copy to Claude Code/Codex with local file and terminal permissions, complete download and installation |

## One-click import: Claude Code / Codex

**Copy the entire paragraph below and paste it into Claude Code or Codex:**

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

You can also open [Independent version import prompt words](prompts/one-click-import.md) to copy. The "one-click import" here refers to handing over the entire request to the programming assistant for execution; if ordinary web chat does not have local file permissions, it cannot be installed on your behalf.

<details>
<summary><b> Prefer to run commands yourself? </b></summary>

Requires Git and Python 3.10+. Execute in terminal:

```bash
git clone https://github.com/XiaoyeCodes/code-animation-prompts.git
cd code-animation-prompts

# Install to Codex
python scripts/install_skill.py --target codex

# or install to Claude Code
python scripts/install_skill.py --target claude

# Install both
python scripts/install_skill.py --target both
```

The installation script only copies files and does not download additional dependencies. If there is already a skill with the same name, it will be stopped and the existing content will be retained. For project-level installation and copying methods without Python, see [Installation Instructions](docs/INSTALL.md).

</details>

## After installing it, just say this

**Codex：**

```text
Use $code-animation-prompts to create a 12-second horizontal screen animation using B3 particle polymorphs.
The theme is "turning ideas into reality" and presents the three stages of inspiration, construction and completion in sequence.
1920×1080, 30 fps, dark background with warm golden particles, with English subtitles, silent.
Please deliver editable HTML, keyframe previews, and MP4s; if rendering dependencies are missing, please state this clearly.
```

**Claude Code：**

```text
/code-animation-prompts Use Z5 paper cutting to create a 12-second New Year’s Prologue, 16:9.
The text is "In the new year, everything can be expected", on red paper, beige rice paper, and layered shadows.
Create editable HTML and keyframes first, without adding sounds; export MP4 when the environment has dependencies.
```

**Haven’t chosen a style yet:**

```text
Use code-animation-prompts to help me make a 30-second popular science video about "Why does it rain?"
For primary school students, vertical screen 9:16, English subtitles, if you want a hand-drawn and warm feeling.
First give me 3 numbered candidate styles, explain how to move them, and then recommend one.
```

Skills provide style reference and production processes, and videos still need to be written by programming assistants and rendered locally. Only looking for styles does not require an API Key or paid image service; the cost of using the assistant itself is determined by the corresponding platform.

## Pick with your eyes, faster than describing

![Original offline picker project screenshot](docs/images/style-picker.png)

After downloading the complete repository, double-click to open it:

```text
skills/code-animation-prompts/assets/library/style-picker.html
```

Browse offline in Chrome/Edge. Search for keywords or numbers → check the style → open the "Selected List" → copy to the assistant, and then add the theme, duration, frame and sound requirements.

Please retain its relative position to `style-prompts/`. The GitHub file page displays HTML source code. After downloading, open it in a browser to use the selector.

<details>
<summary> View search status screenshot </summary>

![Screenshot of items searched by R1](docs/images/picker-search.png)

</details>

## Take a look at the animation from the original example

![B6 excerpt animation from the original sample video](docs/images/b6-preview.gif)

*The picture above is an excerpt from the B6 sample video in the material package, with silent preview. The model annotation in the original file name comes from the material package and does not mean that this repository has conducted separate model comparison tests. *

| Example | Documentation |
|---|---|
| **B6 Speed of Light · Explosion · Reunion** | [Full Prompt Words](skills/code-animation-prompts/assets/library/examples/B6_lightspeed-explosion-regrouping_same-prompt/prompt.md) · [Original HTML with 2 MP4s](skills/code-animation-prompts/assets/library/examples/B6_lightspeed-explosion-regrouping_same-prompt) |
| **X7 Hero Comics** | [One sentence prompt](skills/code-animation-prompts/assets/library/examples/X7_hero-comic_one-sentence/prompt.md) · [Original HTML and MP4](skills/code-animation-prompts/assets/library/examples/X7_hero-comic_one-sentence) |

**B6 is a standalone example and does not count towards the 341 style entries.** The original 3 MP4s, 3 sample HTMLs and process screenshots are retained with the repository.

## The 341 styles at a glance

| Series | Quantity | Focus |
|---|---:|---|
| A–G · Code samples | 26 | Words, particles, lines and ink, light and weather, graphics and paper, explanation, texture |
| M · Dynamic style | 40 | How to move, cut, and speak the entire video |
| K · Cartoon style | 38 | Visual language of characters and images |
| Z · Chinese style | 15 | Ink, gongbi, paper-cut, shadow puppet, Dunhuang, etc. |
| H · Ready-made layout | 12 | Matching of color and fonts |
| L · Lemo-Opuscar | 59 | Multiple styles with complete practices |
| V · mg-styles-15 | 15 | Motion graphics styles |
| X · code-video | 31 | Code video style |
| R · Learned from reference | 7 | Visual reference such as cyberpunk presented in code |
| O · Oscar 98 | 98 | Movie style reference organized according to original materials |
| **Total** |**341** |**196 stills + 145 text references** |

→ [Open the complete style index, each entry can be clicked](docs/STYLES.md)

## Export your own video

Find styles, read hints, and use pickers without rendering dependencies. **Playwright + Chromium + FFmpeg** is only required when using the included HTML → MP4 tool.

```bash
python -m pip install playwright
python -m playwright install chromium
ffmpeg -version

# Validate the environment with the attached time interface example
python skills/code-animation-prompts/scripts/render_video.py skills/code-animation-prompts/assets/starter/index.html --output output/demo.mp4 --duration 12 --fps 30 --width 1920 --height 1080
```

`ffmpeg -version` is a check command; if it is not installed, see [FFmpeg official download](https://ffmpeg.org/download.html). The renderer requires the page to provide `window.renderAt(t)` and closes the real-time loop at `?export=1`; the original example needs to be adapted to this interface first and cannot be directly used as a general web page screen recorder. For details, see [Rendering Interface and Audio Description](skills/code-animation-prompts/references/rendering.md).

## Repository structure

```text
code-animation-prompts/
├── README.md
├── LICENSE.md # Source and usage agreement of each part
├── prompts/one-click-import.md # Copy the import request to Claude Code / Codex
├── docs/
│ ├── INSTALL.md # Installation location, project installation, update method
│ ├── STYLES.md # 341 clickable items
│ ├── images/ # Cover, style wall, screenshots of real projects, animations
│ └── source-manifest.json # Fixed SHA-256 baseline of original 555 files
├── scripts/ # Installation, index generation, preview image generation, verification
└── skills/code-animation-prompts/
    ├── SKILL.md # Skill entrance
    ├── agents/openai.yaml # Codex display information
    ├── references/ # Style index, rendering and source description
    ├── scripts/ # Search and video export
    └── assets/
        ├── starter/index.html # New deterministic animation interface example
        └── library/ # Original materials and registered community additions
            ├── style-picker.html       # English offline style picker
            ├── style-prompts/        # English style prompts
            ├── examples/             # Examples
            ├── third-party-licenses/        # Third-party licenses
            ├── stats.json        # Statistics
            ├── guide.md           # Library guide in English
            └── licenses-and-sources.md      # Licenses and sources in English
```

## Acknowledgments and Free Sharing Agreement

Thanks to the original material organizer - Bilibili [**Pitching and Viewing**](https://space.bilibili.com/3690990015613855/?spm_id_from=333.788.upinfo.detail.click) for sharing the resources.

Thanks to [**Strange Leo (@strangeyu911-tech)**](https://github.com/strangeyu911-tech) for adding the three reference instruction cards K1–K3 via [PR #1](https://github.com/XiaoyeCodes/code-animation-prompts/pull/1). The current 196 reference pictures are composed of 193 pictures in the original package and 3 pictures added by the community; [Source and Change Record](skills/code-animation-prompts/references/attribution.md) is installed with the skill.

Also thanks to **LemoLab (Lemo-Opuscar)**,**Vincentwei1021 (mg-styles-15)**,**Bae-ChangHyun (code-video)**. XiaoyeCodes adds skill encapsulation, tool scripts and project documents based on the original materials; the original prompts, examples and licenses are retained; changes to selectors, statistics and new materials are also recorded.

**Free to use, free to share; please do not package this collection as a paid course, paid skills or other paid content for sale.** Third-party content continues to be subject to their respective licenses, see [Source and License](LICENSE.md) for details. Not all material in this repository is redeclared as MIT.

---

<div align="center">

**Choose a style, write your story, and let the code move.**

If this project is helpful to you, you are welcome to star and share your code animation works. Please read [Submission Guidelines](CONTRIBUTING.md) before adding images.

</div>

## Star History

<a href="https://www.star-history.com/?repos=XiaoyeCodes%2Fcode-animation-prompts&amp;type=date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=XiaoyeCodes/code-animation-prompts&amp;type=Date&amp;theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=XiaoyeCodes/code-animation-prompts&amp;type=Date" />
    <img alt="Star History Chart for XiaoyeCodes/code-animation-prompts" src="https://api.star-history.com/svg?repos=XiaoyeCodes/code-animation-prompts&amp;type=Date" width="100%" />
  </picture>
</a>


