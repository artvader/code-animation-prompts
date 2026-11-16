# Z5 paper cutting

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: Z Chinese style · Chinese style
- What it looks like: Red paper hollowing, folk patterns / Chinese paper cutting

## Style prompt words

> The prompt word for this item is a rewritten detailed version: the screen rules, colors, and timeline are all written down, and both DeepSeek and Opus 5.5 can be used directly. {{ }} is the content you need to fill in yourself.

You are a front-end animation engineer. Please write a complete index.html file: only native HTML + JavaScript + Canvas, no external libraries, font files or images. Make a "Chinese paper-cut" style animation: circular hollow window grilles cut out of red paper, layered on the window paper, with projections.

## content

- Theme: {{Theme, for example: Newcomer's title}}
- Total duration: {{seconds, default 12}}
- The word to be engraved in the center: {{Default "JOY"; fit the English word inside the central medallion}}

## Output requirements (must be followed)

1. Only output an html code block without explanation. The code must be complete and runnable: do not use ellipsis, do not write "the rest is the same as above" or "omitted here".
2. The canvas is fixed at 1920×1080, scaled and centered using CSS, and the extra part is a black border.
3. All screens are determined by function `draw(t)` (`t` is seconds). Don't use `Math.random`; if you need randomness, use mulberry32(seed) with seeds. The same `t` will be drawn the same every time.
4. The default loop playback; space to pause/continue; when the URL contains `?t=5`, only the 5th second frame will be displayed.

## color

Window Paper #F1E8D4; Primary Red #C8102E; Deep Red #8F0B22. In addition to these three colors, no other colors are needed, no gold, gradient, or highlight.

## How to draw (follow these steps)

1. **Window paper**: Use #F1E8D4 to cover it, and then randomly draw 2000 thin short lines with a length of 8–34px (half #B9A98A, half #FFFAF0, transparency 0.05–0.11) with seeds as paper fibers. This layer is only drawn once and put into the off-screen canvas cache.
2. **Create two red papers** (use an off-screen canvas each, size 1920×1080, move the coordinate origin to the center of the screen):
   - `layerBase`: A deep red #8F0B22 disk with a radius of 452; use `destination-out` to dig 48 small holes with a radius of 10 on the outer edge (place them at a radius of 428), and then dig out the entire circle within a radius of 400 (leaving only a dark red edge).
   - `layerTop`: bright red #C8102E disk, radius 404; use `destination-out` to dig out the following, **each circle is "draw 1/N, rotate and copy N copies"**:
     - 48 small holes on the outer edge: radius 9, placed at r=378;
     - 24 droplets: from r=342 to r=274, width 22;
     - 12 large petals: from r=244 to r=74, width 50;
     - 12 small rhombuses: each rotated by π/12, centered at r=226, width 32 and height 48;
     - 12 small dots: each is rotated by π/12, radius 12, and placed at r=170;
     - 12 inner petals: from r=78 to r=148, width 26;
     - Dig out the center circle with a radius of 66; then use bright red to fill in a small plate with a radius of 46 in the center; finally use `destination-out` to write the center word on the small plate (bold 66px, centered).
   - There must be a red "bridge" between the petals, do not cut the red paper.
3. **Four Corners**: Use another off-screen canvas to draw a bright red "quarter circle" (radius 250, the center of the circle is at the corner of the screen), dig: 9 small holes along the arc (radius 7), 4 water droplets, and a round window with a radius of 58. Copy to the four corners (flip).
4. **Synthesis**: First draw the window paper; then draw `layerBase`, `layerTop`, and the four corner flowers in sequence. Set the projection before each layer of painting: `shadowColor='rgba(70,12,12,0.38)'`, `shadowBlur=16`, `shadowOffsetX=5`, `shadowOffsetY=9`.

The teardrop-shaped path can use this function directly (the origin is at the center of the window grille, and the y-axis is negative upward):

```js
function drop(g, y0, y1, w) {
  const d = y0 - y1;
  g.beginPath(); g.moveTo(0, y0);
  g.bezierCurveTo(w, y0 - d * .25, w * .9, y1 + d * .35, 0, y1);
  g.bezierCurveTo(-w * .9, y1 + d * .35, -w, y0 - d * .25, 0, y0);
  g.fill();
}
function ring(g, n, fn) { for (let i = 0; i < n; i++) { g.save(); g.rotate(i * Math.PI * 2 / n); fn(g, i); g.restore(); } }
```

## Get moving

- 0–0.8 seconds: The dark red chassis expands from radius 0 to full (ease-out); the bright red main disk also expands after 0.25 seconds.
- 1.2–4 seconds: The hollow is "opened" in circles from the outside to the inside (the radius of each hole grows from 0 to the target value, each circle is delayed by 0.18 seconds, and each hole is 0.35 seconds); because the holes are dug out, the "radius of the hole × progress" is passed to the above hole digging step during implementation, and `layerTop` is regenerated every frame (completed circles can be cached).
- 4–4.4 seconds: center word "stamp": scale 1.15 → 1.0.
- After that, the entire window grille slowly swings at ±0.6° (period 6 seconds), and the shadow offset subsequently changes ±2px.
- Hold still for the last second, then loop.

## don't want

Gold, gradients, plastic highlights, 3D, particles, glow, heavy shadows, writing words on paper (must be carved out).

## After writing, go through it yourself (do not output)

- The hollow is made by `destination-out`, isn't it covered with the base color?
- Are the 12 copies perfectly symmetrical?
- Do all shadows go down and to the right?
- If the same `t` is refreshed twice, is the screen exactly the same?
