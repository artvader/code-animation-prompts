# B3 particle polyshape

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: A–G code samples · B particles
- What it looks like: Particles gather into hearts, houses, and people, and then spread out.
- Suitable for: Talking about specific things: home, relationship, a person
- Keywords: gathering, shape, dispersion

## Style prompt words

> The prompt word for this item is a rewritten detailed version: the screen rules, colors, and timeline are all written down, and both DeepSeek and Opus 5.5 can be used directly. {{ }} is the content you need to fill in yourself.

You are a front-end animation engineer. Please write a complete index.html file: only native HTML + JavaScript + Canvas 2D, no external libraries, font files or images. Make a "particle gathering" animation: thousands of small luminous particles gather into a shape, stop, spread out, flow along the arc to the next shape, and then gather again, and the cycle continues.

## content

- The four shapes are: heart → house → person → an English word ({{default: HOME}}).
- When each shape stops, a line of subtitles will appear at the bottom of the screen. The four sentences are: {{Four sentences, separated by |. Default: First there is a heart | Then there is a house | One person lives in it | Together they are called home}}.

## Output requirements (must be followed)

1. Only output an html code block without explanation. The code must be complete and runnable: do not use ellipsis, do not write "the rest is the same as above" or "omitted here".
2. The canvas is fixed at 1920×1080; use CSS to scale it proportionally and center it in the window, and the extra part is a black border.
3. The picture is a pure function of time t (seconds) `draw(t)`. Don't use `Math.random`; use seeded mulberry32(2026) for all randomness, and only generate it once at boot. Don't accumulate state in draw (don't use "remnants of the previous frame"). In this way, the same t will be drawn exactly the same every time.
4. The default loop playback (requestAnimationFrame, t = the number of seconds played); press the space to pause/continue; when the URL contains `?t=3.3`, only the 3.3 second frame (still) will be displayed.

## Constants

N = 5000 particles; one cycle per shape PER = 4.8 seconds, 4 shapes total, total cycle 19.2 seconds; shape scaling SC = 1080 × 0.36; shape center at (960, 520).

## Shape (coordinates in the box [-1,1], y downward)

```js
const heart  = (x,y)=>{ y=-y*1.15+.1; x*=1.15; return Math.pow(x*x+y*y-1,3)-x*x*y*y*y<=0; };
const house  = (x,y)=>(Math.abs(x)<=.6&&y>=-.1&&y<=.75&&!(Math.abs(x)<.14&&y>.38))||(y<-.1&&y>-.8&&Math.abs(x)<=.8*(y+.8)/.7);
const person = (x,y)=>(x*x+(y+.55)*(y+.55)<=.05)||(y>=-.28&&y<=.85&&Math.abs(x)<=.25+(y+.28)*.2);
```

- Hearts, houses, people: Use random points with seeds in [-1,1]² to do "rejection sampling", and keep the ones that fall in the shape, and make up to N points.
- English word: Use a 400×400 off-screen canvas to draw the word in white bold Georgia or Times New Roman. Measure it with `measureText` and reduce the font size until it fits within 360 px; horizontally centered, `textBaseline='middle'`, y=210; after `getImageData`, take a point with alpha>128 every 2 pixels, converted to [-1,1]; use N after shuffling with seeds (if it is not enough, take it again and add ±0.004 jitter).
- Each of the four groups of target points is shuffled once. The i-th particle goes to its respective i-th target point in the four shapes - so it looks like "the same batch of particles are changing shapes".

## Fixed parameters for each particle (generated once at startup)

Angle `a` (0–2π), amplitude `m` (0–1), phase `ph` (0–2π), flicker frequency `f` (0.6–1.6), size `s` (0–1), whether with halo `glow` (20% true).

## Position (core, calculated as this)

Let k = floor(t / PER) % 4 (current shape), n = (k+1) % 4 (next shape), q = t % PER (time within shape); A = i-th target point in the k-th shape, B = i-th target point in the n-th shape.

- progress e = smoothstep(2.4, 4.2, q). q e=0 (stopped) at 0–2.4 seconds; deforming at 2.4–4.2 seconds; e=1 (settled) at 4.2–4.8 seconds.
- Control point C = (A+B)/2 + (cos a, sin a) × (0.35 + 0.9·m).
- Position P = (1−e)²·A + 2(1−e)e·C + e²·B (quadratic Bezier, so particles follow an arc, first explode and then converge).
- Micromotion: P plus (cos(ph + 1.3t), sin(1.7·ph + 1.1t)) × 0.012 × (1 − sin(π·e)).
-Screen coordinates = (960 + P.x × SC, 520 + P.y × SC); the whole is multiplied by zoom = 1 + 0.015·sin(0.33t) based on the center of the screen (960, 540).

## How to draw

1. **Background**: #07080C covered; a radial gradient (radius 800) in the center from `rgba(40,46,66,0.30)` to `rgba(7,8,12,0)`; then draw 220 fixed-position dark star points (randomly once at startup, transparency 0.15–0.4, flickering slightly with t).
2. **Particles**: Use `globalCompositeOperation = 'lighter'` to superimpose light. Colors: heart #F08A8A, house #F1C070, person #A9C6FF, kanji #F6EBD0; press e while transforming to linearly blend between the "color of the current shape" and the "color of the next shape".
3. Brightness of each particle L = 0.75 + 0.25·sin(f·t + ph); radius r = 1.1 + 1.6·s (pixel); basic transparency 0.55·L.
4. **Tail**: Each particle is drawn three times, respectively at time t, t−0.045, and t−0.09 (recalculate using the same position function, do not save the history); the transparency is ×1, ×0.5, ×0.25, and the radius is ×1, ×0.8, ×0.6.
5. **Glow**: For particles with glow=true, draw an additional large circle with a radius × 3 and a transparency of 0.05.
6. **Subtitles**: When each shape is stopped (q fades in from 0.3 to 1.0, q fades out from 2.1 to 2.5), display the sentence corresponding to the shape centered at (960, 960), serif 46px, color #EDE6D6, maximum opacity 0.85.

## don't want

Exploding flash, lens flare, rainbow colors, second background, real-time timer driven randomization, save state from previous frame in `draw`.

## After writing, go through it yourself (do not output)

- If the same t is refreshed twice, will the screen be exactly the same?
- Is what you see at t=1.8 a heart made of particles? Is it exploding and flowing towards the house at t=3.3?
- If I draw 5000×3 particles in one frame, will it get stuck? If it is stuck, you can apply the halo only to the glow particles.
