# M1 whiteboard hand-drawn explanation

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: M Dynamic Style · Explanation
- What it looks like: White background, one hand (or a pen) drawing while talking, lines drawn first and then colored.
- Suitable for: paragraphs that talk about concepts and principles. For example, "The big language model is the brain, and Harness is the hands and feet."

## Style prompt words

> The prompt word for this item is a rewritten detailed version: the screen rules, colors, and timeline are all written down, and both DeepSeek and Opus 5.5 can be used directly. {{ }} is the content you need to fill in yourself.

You are a front-end animation engineer. Please write a complete index.html file: only native HTML + JavaScript + Canvas, no external libraries, font files or images. Make a whiteboard hand-drawn explanation animation.

## What to talk about

- Topic: {{Topic, for example: the large language model is the brain, Harness is the hands and feet}}
- Total duration: {{seconds, default 20}}
- Words on the screen: {{3–6 short words. Example: Title "How does AI work?"; "Large Language Model" on the left, subtitled "Can Think and Speak"; "Harness" on the right, subtitled "Hands and Feet: Really Do Things"; "Instructions" on the arrow}}

## Output requirements (must be followed)

1. Only output an html code block without explanation. The code must be complete and runnable: do not use ellipsis, do not write "the rest is the same as above" or "omitted here".
2. The canvas is fixed at 1920×1080; use CSS to scale it proportionally and center it in the window, and the extra part of the window will be black borders.
3. All screens are determined by function `draw(t)`, `t` is seconds. Don't use `Math.random`; if you need randomness, use mulberry32(seed) with seeds, so that the same `t` will be exactly the same every time you draw it.
4. The default loop playback; press space to pause/continue; when the URL contains `?t=8.5`, only the 8.5 second frame (still) is displayed, which is convenient for screenshots.

## How to draw the picture

- Base color #FBFAF7; overlay a few very light gray scratches (40–90px wide, opacity 0.03–0.06).
- The lines are black marker #1B1B1B, 10px wide, and round for both `lineCap` and `lineJoin`. Draw each stroke twice: the first pass has an transparency of 0.93; the second pass has a width of 5.5px, an transparency of 0.55, and a position offset of ±1.5px.
- Only black and **one** accent color #E5432B (used in title underlines, arrows, subtitles and pen caps). No third color.
- Font: `font-family: KaiTi, STKaiti, "Kaiti SC", "Microsoft YaHei", sans-serif`, bold; title 110px, label 90px, subtitle 56px. Use `strokeText` plus `fillText` for the font, and the stroke width is about 3.5% of the font size.
- Hand-painted feeling: Add ±2.5px jitter to each point. The jitter is randomly selected according to the "point number" with a seed. Do not re-randomize every frame.
- Things to draw:
  - Cloud-shaped "brain": polar coordinates r = R·(1 + 0.11·|sin(3.5θ)|), with several wavy lines drawn inside;
  - A stick figure: a round head, a line body, two arms (draw a circle at the end as a hand), and two legs;
  - A curved accent arrow with the head pointing in the direction of the tail;
  - A marker pen: black rod, red cap, about 330px long, slanted at 55°, the pen tip always stops at the end of "the stroke currently being drawn"; slide out of the screen after all the drawings are completed.

## Rules for moving

- Each stroke is a list of points. Use progress (0→1) to determine which point to draw, progress uses ease-in-out; one stroke is 0.4–1.2 seconds.
- Sequence: title → title underline (red) → brain on the left → little man on the right → red arrow → two words "instruction" → two label texts. Only draw one stroke at a time.
- After all drawings are completed, wait for 1.5 seconds and then cycle again.

## don't want

Gradient, shadow, glow, 3D, particles, complex color matching, full screen text, camera shake.

## After writing, go through it yourself (do not output)

- Is it an almost blank whiteboard at `t=0`?
- Are all elements present at `t=total duration−0.1`?
- Is the text held down by lines or pens?
- If the same `t` is refreshed twice, is the screen exactly the same?
