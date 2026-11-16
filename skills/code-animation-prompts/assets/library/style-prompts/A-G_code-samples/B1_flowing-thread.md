# B1 flowing silk thread

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: A–G code samples · B particles
- What it looks like: Countless thin lines flowing with the invisible wind.
- Suitable for: thoughts and emotions flowing, calming down
- Keywords: flow, thread, wind

## Style prompt words

Use code (Canvas 2D) to draw an animation of "flowing threads": countless thin lines flowing with the invisible wind.
Suitable for speaking: thoughts and emotions are flowing, calming down
Keywords: flow, thread, wind

The following is the reference implementation we wrote ourselves: a drawing function S.B1(c, w, h, t, s), c is the 2D context of the canvas, w/h is the width and height, t is the second, and s is an empty object used to store the state of this function. Public widget functions are in _public function.js in the same folder.

```js
S.B1 = (c, w, h, t, s, dpr) => {
  if (!s.init) { s.init = 1; [s.bc, s.bx] = offscreen(w, h, dpr); s.bx.fillStyle = '#05080d'; s.bx.fillRect(0, 0, w, h); const r = rng(5); s.r = r; s.p = []; for (let i = 0; i < 800; i++) s.p.push([r() * w, r() * h, r() * 200, r()]); }
  const b = s.bx, sc = 3.2 / Math.min(w, h); b.fillStyle = 'rgba(5,8,13,.07)'; b.fillRect(0, 0, w, h); b.lineWidth = .8;
  for (const p of s.p) {
    const a = nz(p[0] * sc, p[1] * sc, t * .12) * Math.PI, sp = Math.min(w, h) / 260;
    const nx = p[0] + Math.cos(a) * sp, ny = p[1] + Math.sin(a) * sp;
    b.strokeStyle = `hsla(${195 + p[3] * 40},60%,${62 + p[3] * 25}%,.4)`; b.beginPath(); b.moveTo(p[0], p[1]); b.lineTo(nx, ny); b.stroke();
    p[0] = nx; p[1] = ny; p[2]--;
    if (p[2] < 0 || nx < 0 || nx > w || ny < 0 || ny > h) { p[0] = s.r() * w; p[1] = s.r() * h; p[2] = 80 + s.r() * 200; }
  }
  c.drawImage(s.bc, 0, 0, w, h);
};
```

