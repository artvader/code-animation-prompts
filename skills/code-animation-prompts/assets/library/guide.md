# Code animation style prompt words

There are **341** styles in total, each with one prompt word. Opus 5.5 can be used, and DeepSeek can also be used. 193 of them have still frames.

Some of them are collected from the Internet, and many of them are organized, made and summarized by myself.

## What's in it

| Folder/File | What is |
|---|---|
| `style-picker.html` | Select web pages. Double-click to open it directly with Chrome or Edge, no need to connect to the Internet. You can filter by category, search, zoom in to see still frames, see prompt words, check, and export lists. Do not separate it from the "Style Tips" folder. |
| `style-prompts/` | 341 styles, one for each `.md` prompt word, with a still frame next to a picture of the same name `.jpg` |
| `examples/` | Two sets of actual measurements: Comparison between Opus 5.5 and DeepSeek given the same detailed prompt word; the result of giving only one sentence to DeepSeek |
| `licenses-and-sources.md`, `third-party-licenses/` | Where does each style come from and what license is used |

### How to divide 341 species

| Category | Quantity | What is |
|---|---|---|
| A–G code samples | 26 | Words, particles, lines and ink, light and weather, graphics and paper, explanations, textures; each comes with reference implementation code |
| M Dynamic Style | 40 | How to move, cut, and speak the entire video |
| K cartoon style | 38 | What the characters and pictures look like |
| Z Chinese style | 15 | Ink, gongbi, paper-cut, shadow puppet, Dunhuang... |
| H Ready-made layout | 12 | Complete set of color matching and fonts |
| L Lemo-Opuscar | 59 | Open source project Lemo-Opuscar styles, each has a complete approach |
| V mg-styles-15 | 15 | Dynamic styles for the open source project mg-styles-15 |
| X code-video | 31 | The style of the open source project code-video |
| R learned from the reference | 7 | Learned to draw cyberpunk with code according to the reference |
| O Oscars 98 | 98 | 98 Oscars for Best Picture, each with a style of painting |

## How to use

**Using DeepSeek Harness (or Claude Code):**

1. Put this folder where it can read it, and tell it: "Read this folder, I want to use the style inside to animate the code."
2. Select the style in `style-picker.html`, click "Selected List" to copy and send it.
3. Make it clear what you want to express: what content, how long, horizontal or vertical screen, how to move the camera, and how to connect several styles together.
4. **Remember to mention whether you want soundtrack and sound effects.**If you don’t say anything, it will probably be silent.
5. Let it output an html that can be opened in the browser, and then let it render into a video.

**Use a style directly:**Open that type of `.md`, copy the "Style Prompt Word" paragraph to the model, and add your content. Some prompt words include `{{ }}`, which is where you need to fill in the prompts yourself.

**Tips:** The more detailed the prompt words are written (color, time, lens are all written down), the closer the models will be. It can be done with just one sentence, but the results will be different and slower every time. `examples/` has both.

## Agreement

- It’s all free, no need to send private messages or buy courses.
- You can use it for free and transfer it to others for free; please share it for free when transferring it.
- **It is prohibited to package these contents into courses, paid skills or anything for sale.**
- Portions from open source projects retain their original licenses and attributions, see `licenses-and-sources.md`.

If you find it useful, you are welcome to support it with one click and three links. Thank you everyone, I will continue to open source more useful information.
