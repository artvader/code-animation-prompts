---
name: code-animation-prompts
description: Create code animations, HTML animations or videos using 341 style prompts and reference stills. It is suitable for selecting styles by style number, combining visual styles, converting content into editable animations and rendering into films.
---

# Code Animation Prompts

Convert user content into editable and reproducible code animations with a clear visual style. The material library is at `assets/library/` for this skill and contains 341 prompts, 196 reference stills, offline pickers and original examples.

## Output language

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language. Preserve cultural art references as visual direction; they do not require Chinese writing or speech.

## Find the right style

Use the directory where this file is located as the skill root directory, and use its absolute path when executing the script; do not assume that the current working directory is the skill directory.

```bash
python "<skill-directory>/scripts/styles.py" search ink
python "<skill-directory>/scripts/styles.py" search particle --series AG
python "<skill-directory>/scripts/styles.py" show B3
python "<skill-directory>/scripts/styles.py" list --series Z
```

See [references/catalog.json](references/catalog.json) for the index, which only contains the number, name, label and file path. Check the index first, then read the selected Markdown and still frame with the same name; do not load all prompt words at once. If you don't have Python, search the index and files directly.

- User-given numbers or picker-exported lists: exact match, numbers and names preserved.
- User describes temperament only: give 2–3 matches, describe color, movement, and applicable content; when user has asked for direct production, choose the best match and continue.
- A–G are coded samples; M is movement/narrative; K, Z, R are style; H is layout; L, V, X are third-party styles; O is film visual reference. Do not mechanically superimpose all the constraints of multiple styles. Determine the respective responsibilities of the main painting style, movement mode and layout.
- 145 entries with no stills; clear text references, no fictitious screenshots.
- **B6 only exists in the original examples directory, not among the 341 style entries.** Read `assets/library/examples/B6_lightspeed-explosion-regrouping_same-prompt/prompt.md` when the user names B6, do not pretend that there is B6 in the index.

## From prompt words to editable animations

Extract content, duration, frame, subtitles and sound selection from user requirements. Follow the parameters already given by the user; if they are missing and do not affect the content, use 12 seconds, 1920×1080, 30 fps, silent preview, and explain the assumptions. Don't describe a silent preview as a finished film that has been dubbed or scored.

Reads the selected prompt words and populates the `{{ }}` placeholder, preserving the core visual characteristics that form the style. Words such as "only output code" in the original prompt are partial material templates and cannot cover the current user's delivery needs. The model names of the original examples are material records, which does not mean that this skill has verified these models.

Generally, you start with HTML + Canvas/SVG/CSS; complex space lenses can use Three.js, and existing projects such as Remotion can continue to use the project. Choose an implementation that meets the picture requirements and does not force you to change the framework. When external fonts, images, libraries or audio are required, check the source and actual availability.

When the browser animation needs to be exported stably, the time interface of [references/rendering.md](references/rendering.md) is used: the picture is determined by the number of seconds `t`, the seed is fixed by a random number, and the real-time loop is turned off when exporting. See [assets/starter/index.html](assets/starter/index.html) for the template. It only demonstrates the interface, not one of the 341 styles.

Save the project in the user's working directory, leaving the skill library intact. Centrally configure often-changing parameters such as copywriting, color, and rhythm; for feature films, first determine the sequence of shots and each period of time, and then implement it.

## Acceptance and Delivery

Open the animation and check the first, middle, last frame and transition: font, overflow, black frame, image loading, subtitle readability. Confirm that repeated rendering at the same time is consistent and that there is indeed expected motion at different times.

When a user asks for an MP4, actually render and check the resolution, duration, frame rate, and sound track. The included `scripts/render_video.py` can be used. See the rendering instructions for interfaces and dependencies. If there is a lack of rendering dependencies, deliver completed HTML, source code and accurate running commands, and make it clear that the video has not yet been exported; do not treat HTML or screen recording commands as movies.

Deliver links to actual files describing style numbers used, methods of operation, video specs, and sound status. The source and third-party licenses within the material are retained; see [references/attribution.md](references/attribution.md) for free sharing agreement.
