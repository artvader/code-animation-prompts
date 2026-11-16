# B6 Light speed shuttle·explosion·reunion

> The results of the same prompt word given to Opus 5.5 (High) and DeepSeek-V4.1-Flash (1017, High) are in this folder. {{ }} is the content you need to fill in yourself.

You are a front-end animation engineer. Please write a complete index.html file: only native HTML + JavaScript + Canvas 2D, no external libraries, font files or images. Make a 12-second, **one shot to the end** animation: shuttle at the speed of light → break through 5 halos in a row → brake, particles are sucked towards the center → explode → the fragments rotate and reunite into the title words. The entire section is a camera flying forward in 3D space,**without cutting the lens from beginning to end**; the same batch of 4,000 particles first became star rays, then became exploded fragments, and finally formed the title.

## content

- Title: {{Default: Pitch Viewing}}
- Subscript: {{Default: See the fleeting moment in the river, see eternity in the trees}}

## Output requirements (must be followed)

1. Only output an html code block without explanation. The code must be complete and runnable: do not use ellipsis, do not write "the rest is the same as above" or "omitted here".
2. The canvas is fixed at 1920×1080; use CSS to scale it proportionally and center it in the window, and the extra part is a black border.
3. The picture is a pure function of time t (seconds) `draw(t)`. Don't use `Math.random`; use seeded mulberry32(7) for all randomization, generated only once at boot. Don't save the state of the previous frame in draw. The same t is drawn exactly the same every time.
4. Default loop playback (requestAnimationFrame, t = seconds played, remainder 12); press space to pause/continue; when the URL contains `?t=5.7`, only the 5.7th second frame (still) will be displayed.

## Constants

W=1920, H=1080, screen center (960,540); N=4000 particles; total length 12 seconds; tunnel length L=6000; base focal length F0=900.

## Lens (the camera moves forward along the z-axis. Write these functions correctly first)

```js
const V0 = 80, V1 = 2600;
const z1 = t => V0*t + (V1-V0)*(3/3.2)*Math.pow(Math.min(t,3)/3, 3.2) + V1*Math.max(0, t-3);
const Z5 = z1(5.0), zB = Z5 + 780, ZC = zB + 900, Z3 = z1(3), ZT = zB - 700;
function camZ(t) {
  if (t <= 5.0) return z1(t);                                              // Accelerate to the speed of light if (t <= 5.6) { const u = (t-5.0)/0.6; return Z5 + 2600*0.6*(u - u*u/2); } // brake suddenly if (t <= 8.0) { const v = (t-5.6)/2.4; return zB - 2200*(1-(1-v)*(1-v)); } // Retreat suddenly after the explosion return zB - 2200 - 120*(t-8.0);                                          // Then slowly retreat
}
```

- **5 halos**: The kth one (k=0..4) is at world coordinate z = Z3 + 2600·(0.3 + 0.42k), the time when the lens passes through it is tk = 3.3 + 0.42k; color when k is an even number (125,249,255), when it is an odd number (255,213,154); radius R=260.
- **Focal length** f(t) = 900 + Add 260·exp(−9(t−tk)) + (when t≥5.6, add 520·exp(−6(t−5.6))) for each ring with tk≤t. - Every time it passes through a ring and at the moment of explosion, the screen will suddenly "top".
- **Roll** roll(t) = 0.02·sin(1.7t) + (when t≥5.6, add 0.12·sin(2π·0.9·(t−5.6))·exp(−2.2(t−5.6))).
- **Jitter**: amp = (t≥5.6 ? 22·exp(−3.2(t−5.6)) : 0), offset = (sin(53t)·amp, cos(47t)·amp).
- Before drawing particles, halo, core and shock wave: `ctx.translate(960+Jitterx, 540+Jittery); ctx.rotate(roll); ctx.translate(-960, -540)`; after drawing these, `restore`, flash white, subtitles, etc. are not affected by rolling and shaking.

## Projection

The coordinates (X, Y, d) of a point in "camera space" (d is its distance from the camera) are drawn on the screen: `sx = 960 + f·X/d`, `sy = 540 + f·Y/d`.

## Fixed parameters for each particle (generated once at startup)

- `a` (0–2π); `rho` = 220 + 1280·rand^0.8; `zw` = rand·L (the depth of the world in the tunnel); `s` (0–1); `cls` (15% is 1, the rest is 0); `ph` (0–2π); `fq` (0.6–1.6);
- Explosion direction `dir`: zz = −0.55 + 1.55·rand, φ = rand·2π, rxy = √(1−zz²), dir = (rxy·cosφ, rxy·sinφ, zz);
- Explosion strength `mag` = 300 + 2600·rand^1.6;
- Rotation amount `sw` = (1.2 + 2·rand)·(random sign);
- Title Target Point `(tx, ty)`: See below.

## The target point of the title

Use a 1200×400 off-screen canvas with white bold fonts (`bold 280px "Noto Serif SC","Songti SC","SimSun",serif`, horizontally centered, `textBaseline='middle'`, position (600, 205)) to write the title; take a point with alpha>128 every 3 pixels, and convert the coordinates to ((x−600)·2.093, (y−200)·2.093); shuffle the cards with seeds and take N numbers (repeat if not enough, and add ±3 jitter). The i-th particle uses the i-th point.

## The camera space position of each particle at time t (written as function `place(p, t)`, returns X, Y, d)

- **t < 5.6 (tunnel)**: k = 1 − 0.92·smoothstep(5.0, 5.6, t) (5.0–5.6 seconds particles move towards the center of the screen);
- **5.6 ≤ t ≤ 8 (explosion)**: τ = min(1, (t−5.6)/2.4), g = 1 − (1−τ)³; world coordinates X = dir.x·mag·g, Y = dir.y·mag·g, Z = ZC + dir.z·mag·g; d = Z − camZ(t).
- **t > 8 (reunion)**: e = smoothstep(8, 10, t); starting point E = (dir.x·mag, dir.y·mag, ZC + dir.z·mag), end point Tg = (tx, ty, ZT); Q = E + (Tg − E)·e; then rotate (Q.x, Q.y) around the origin θ = sin(π·e)·sw; X, Y = result after rotation, Z = Q.z; d = Z − camZ(t).

## How to draw each frame

1. **Background** #05060A; draw another radial gradient with center (960,540) and radius 700: from `rgba(30,60,90, 0.28·sf·(t<5.6 ? 1 : 0.4))` to `rgba(5,6,10,0)`. sf = 0.45 + 0.55·clamp(speed/2600, 0, 1), speed is the current speed of the camera: when t<3, 80+2520·(t/3)^2.2; 3–5 seconds 2600; 5–5.6 seconds 2600·(1−(t−5)/0.6); the rest are 0.
2. Use `globalCompositeOperation='lighter'` and `lineCap='round'` for everything below.
3. **Particles**: Each particle is drawn as a line segment, connecting from "screen position at time tp" to "screen position at time t". tp = max(t − DT, t≥5.6 ? 5.6 : 0), DT = (t<5.6 ? 0.03 : 0.06 − 0.03·smoothstep(8, 9, t)); at tp moment, use the focal length corresponding to tp. As long as d<30 at either end, or the difference between d at both ends exceeds 500 (just around the beginning of the tunnel), this line will not be drawn.
   - **Color**: t<5.0: cls=1 is (255,213,154), otherwise (191,232,255); 5.0–5.6: press smoothstep(5.0, 5.6, t) to mix towards white; 5.6–8: when τ<0.4, mix from white to orange (255,176,74), and then mix from orange to magenta (255,61,110); 8–10: mix from magenta to warm white (246,235,208) (press smoothstep(8,10,t)); t≥10: warm white.
   - **Transparency**: t<5.6: (1 − d/L)^1.4·(0.25 + 0.55·s)·sf·1.6, limited to 0–1; t≥5.6: 0.9·(0.7 + 0.3·sin(fq·t + ph))·(t<8 ? 1−0.4τ : 0.9).
   - **Line width**: t<5.6: (0.9 + 1.8·s)·clamp(√(900/d), 0.5, 2.2); t≥5.6: (2 + 3·s)·clamp(√(900/d), 0.6, 2.2).
4. **Halo (only not drawn in t<5.6 Time painting! )**：For each ring,d = ring z − camZ(t)；d<40 or d>5200; otherwise draw a 96-segment circle along radius R=260: point = (960 + f·R·cosθ/d, 540 + f·R·sinθ/d); line width clamp(6·900/d, 1.5, 16), transparency 0.6·clamp(1 − d/5200, 0, 1); after drawing once, draw one more time as a halo with 3 times the line width and 1/4 transparency.
5. **Core light**: When t≥4.4 and dc = ZC − camZ(t) > 40, draw a white radial gradient circle (center (960,540), from `rgba(255,255,255,0.9)` to transparent), radius = 140000/dc·(0.4 + 0.6·smoothstep(4.4, 5.6, t))·(f/900), when t≥5.6, multiply exp(−3(t−5.6)).
6. **Shock wave**: When t≥5.6, ts = clamp((t−5.6)/1.2, 0, 1), world radius Rw = 3600·(1 − (1−ts)³); if ts<1 and dd = ZC − camZ(t) > 40: Draw a white stroked circle, center (960,540), radius f·Rw/dd, transparency 0.8·(1−ts), line width 1 + 8·(1−ts).
7. Cancel translation/rotation (`restore`), and then draw:- **Flash White**: full screen white rectangle (lighter), transparency = (t≥5.6 ? 0.95·exp(−9(t−5.6)) : 0.7·smoothstep(5.4, 5.6, t)) + each ring of t≥tk plus 0.3·exp(−14(t−tk)) + (t≥10 ? 0.35·exp(−8(t−10)) : 0), the sum is limited to 1;
   - **Title Freeze** (source-over): Transparency 0.9·smoothstep(9.7, 10.3, t)·(1 − smoothstep(11.4, 12, t)), center draw title at (960, 545), `bold 300px` same font, color #F6EBD0;
   - **Subscript**: transparency 0.85·smoothstep(9.6, 10.4, t)·(1 − smoothstep(11.4, 12, t)), centered at (960, 790), serif 40px, color #EDE6D6;
   - **Vignetting**: radial gradient, radius 400→1150, from `rgba(0,0,0,0)` to `rgba(0,0,0,0.55)`;
   - **First and last fade**: black full-screen rectangle, transparency (1 − smoothstep(0, 0.35, t)) + smoothstep(11.4, 12, t).

smoothstep(a, b, x): t = clamp((x−a)/(b−a), 0, 1), returns t·t·(3 − 2t).

## don't want

`Math.random`; save the state of the previous frame in `draw`; use DOM elements for animation; extra colors; draw the halos after the explosion (they will pop up "head on" when the camera pulls back, so they must not be drawn).

## After writing, go through it yourself (do not output)

- If the same t is refreshed twice, will the screen be exactly the same?
- t=2.8 Do you see star lines extending in all directions, with several cyan/amber rings in the middle?
- t=5.3 Are the particles sucked towards the center, a ball of white light in the center? Is t=5.7 a white radial explosion?
- t=9.5 Are the particles rotating and converging? Is t=10.8 a clear title word?
- If I draw 4,000 lines and 5 rings in one frame, will it get stuck?
