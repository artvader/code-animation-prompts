# B5 Circle of Breathing

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: A–G code samples · B particles
- What it looks like: A cloud of particles that expands and shrinks with breathing.
- Suitable for: soothing, slowing down, meditating
- Keywords: breathing, expansion and contraction, slow

## Style prompt words

Use code (Canvas 2D) to draw a "breathing circle" animation: a group of particles expands and shrinks with breathing.
Suitable for speaking: soothing, slowing down, meditating
Keywords: breathing, expansion and contraction, slow

The following is the reference implementation we wrote ourselves: a drawing function S.B5(c, w, h, t, s), c is the 2D context of the canvas, w/h is the width and height, t is the second, and s is an empty object used to store the state of this function. Public widget functions are in _public function.js in the same folder.

```js
S.B5 = (c, w, h, t, s) => {
  if (!s.init) { s.init = 1; const r = rng(17); s.p = Array.from({ length: 750 }, () => [r() * TAU, Math.sqrt(r()), r()]); }
  const b = .5 - .5 * Math.cos(TAU * t / 8), R = Math.min(w, h) * .33 * (.55 + .45 * b);
  c.fillStyle = '#061213'; c.fillRect(0, 0, w, h);
  glowDot(c, w / 2, h / 2, R * 1.3, '#4fb7a8', .12 + .1 * b);
  c.fillStyle = mixHex('#5fbfb0', '#dff3ec', b);
  for (const p of s.p) { const a = p[0] + t * .05 * (p[2] - .5), rr = p[1] * R + Math.sin(t * 1.3 + p[2] * 50) * 2; c.fillRect(w / 2 + Math.cos(a) * rr, h / 2 + Math.sin(a) * rr, 1.4, 1.4); }
  const rising = Math.sin(TAU * t / 8) > 0; c.font = `500 ${Math.min(w, h) / 20}px ${SERIF}`; c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillStyle = 'rgba(220,240,235,.55)'; c.fillText(rising ? 'Inhale' : 'exhale', w / 2, h / 2 + Math.min(w, h) * .42);
};
```

