# E3 character painting

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Classification: A–G Code Samples · E Graphics and Paper
- What it looks like: The screen is made up of characters, like an old computer screen.
- Suitable for: technology, cold, memory fragments
- Keywords: character painting, terminal, pixel

## Style prompt words

Use code (Canvas 2D) to draw a "character painting" animation: the screen is entirely made up of characters, like an old computer screen.
Suitable for talking about: technology, coldness, memory fragments
Keywords: character painting, terminal, pixel

The following is the reference implementation we wrote ourselves: a drawing function S.E3(c, w, h, t, s), c is the 2D context of the canvas, w/h is the width and height, t is the second, and s is an empty object used to store the state of this function. Public widget functions are in _public function.js in the same folder.

```js
S.E3 = (c, w, h, t, s) => {
  const cs = Math.max(7, Math.round(Math.min(w, h) / 26)), cols = Math.floor(w / (cs * .62)), rows = Math.floor(h / cs), ch = ' .,:;-=+*#%@';
  c.fillStyle = '#0a0703'; c.fillRect(0, 0, w, h); c.font = `500 ${cs}px ${MONO}`; c.textBaseline = 'top';
  const lx = .5 + .3 * Math.cos(t * .7), ly = .5 + .3 * Math.sin(t * .9);
  for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
    const x = i / cols, y = j / rows, ax = (x - .5) * w / h, d = Math.hypot(ax, y - .5);
    let v = .5 + .5 * Math.sin(d * 22 - t * 2.4); v *= Math.exp(-d * 1.6);
    v += .9 * Math.exp(-(((x - lx) * w / h) ** 2 + (y - ly)** 2) / .02);
    const k = Math.min(ch.length - 1, Math.floor(clamp(v, 0, .999) * ch.length)); if (!k) continue;
    c.fillStyle = `rgba(255,179,71,${.35 + v * .65})`; c.fillText(ch[k], i * cs * .62, j * cs);
  }
};
```

