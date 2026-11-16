# H1 Biennale Yellow

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: H Ready-made layout · Ready-made layout
- What it looks like: Warm parchment base, solar yellow halo, serif headline, indigo ink, thin lines

## Style prompt words

> The prompt word for this item is a rewritten detailed version: the screen rules, colors, and timeline are all written down, and both DeepSeek and Opus 5.5 can be used directly. {{ }} is the content you need to fill in yourself.

You are a front-end animation engineer. Please write a complete index.html file: only native HTML + JavaScript + Canvas, no external libraries, font files or images. Make an animated title card in the style of "Art Biennale Magazine Cover".

## content

- Headline (two lines): {{First line, for example: Biennale}} / {{Second line, for example: Yellow}} (The second line is in italics)
- Header left: {{Example: THE TWELFTH BIENNALE · EDITORIAL SERIES}}; Header right: {{Example: N° 01}}
- Footer left (English): {{one sentence description}}; footer right: {{number}}
- Total duration: {{seconds, default 6}}

## Output requirements (must be followed)

1. Only output an html code block without explanation. The code must be complete and runnable: do not use ellipsis, do not write "the rest is the same as above" or "omitted here".
2. The canvas is fixed at 1920×1080, scaled and centered using CSS, and the extra part is a black border.
3. All screens are determined by function `draw(t)` (`t` is seconds). Do not use `Math.random`; use mulberry32(seed) with seeds for paper texture.
4. Default loop; space to pause/continue; when the URL contains `?t=3`, only the 3rd second frame will be displayed.

## Colors and lines (only these are allowed)

- Background color paper = #F2E9D2; Add paper texture: 5000 small square dots of 1–3px, half #8C7A55, half #FFFAF0, transparency 0.045–0.095. The paper texture is only drawn once and cached to the off-screen canvas.
- The only accent color sun = #F6C23E.
- Use ink = #1D2A68 for text and all lines, with a line width of 1.6–1.8px.

## Font

`font-family: Georgia, "Times New Roman", "Noto Serif", serif`. Only serif fonts are used throughout the film. The main title is about 214px, `letterSpacing = '-4px'`; the header is 26px, in uppercase, `letterSpacing = '6px'`; the footer is 34px in English. (`ctx.letterSpacing` of canvas is available in new browsers; if it is not supported, it will be drawn verbatim.)

## Layout (coordinates are 1920×1080)

1. Outer frame: `strokeRect(64, 64, 1792, 952)`; draw two more horizontal lines: y=148 and y=932, from x=64 to x=1856.
2. Sun, center of circle (1380, 470):
   - Halo: radial gradient, radius 20→560, from `rgba(246,194,62,1)` to `rgba(246,194,62,0.92)` (38%), to `rgba(246,214,120,0.35)` (70%), to `rgba(246,214,120,0)` (100%);
   - Solid circle: radius 250, color sun;
   - Three concentric thin circles: radius 250, 330, 410 (ink, transparency 0.9, 0.45, 0.45);
   - Scale ring: radius 410 to 421 (every 5 long strips, to 432), 120 strips in total, ink, transparency 0.85.
3. Big title: left x=100, first line baseline y=560, second line (italic) baseline y=770. Be careful that the right end of the title does not touch the scale ring (the leftmost end is about x=948).
4. The baseline of two lines of small characters in the header is y=118 (left x=104, right x=1650); the English baseline of the footer is y=980 (left x=104), and the numbers are right-aligned to x=1816.

## Get moving

- 0–0.8 seconds: The outer frame and two horizontal lines are "drawn" from the four corners to the middle (use `setLineDash` or intercept according to the progress);
- 0.4–1.8 seconds: the sun rises from 300px below (ease-out), halo transparency 0→1;
- 1.0–2.4 seconds: the two lines of the title fade in sequentially from 24px below, and the kerning goes from +20px to −4px;
- 2.0–2.8 seconds: Header and footer fade in; scale ring rotates clockwise slowly at 1° per second;
- Ending 0.5 seconds: overall fades to paper color, then loops.

## don't want

Gradient color blocks, drop shadows, rounded corners card, second accent color, sans serif headline, glow, particles.

## After writing, go through it yourself (do not output)

- Is sun the only accent color in the entire film?
- Does the title touch the scale ring?
- If the same `t` is refreshed twice, is the screen exactly the same?
