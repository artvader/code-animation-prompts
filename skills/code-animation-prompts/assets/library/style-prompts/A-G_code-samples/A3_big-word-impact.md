# A3 large character impact

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: A–G code sample · A word
- What it looks like: One word at a time slamming into the frame, following the beat.
- Suitable for: emotional outbursts, golden phrases, MV choruses
- Keywords: big characters, smash down, follow the beat

## Style prompt words

Use code (Canvas 2D) to draw an animation of "big character impact": one word after another hits the screen, following the beat.
Suitable for speaking: emotional outbursts, golden phrases, MV choruses
Keywords: big characters, smash them down, follow the beat

The following is the reference implementation we wrote ourselves: a drawing function S.A3(c, w, h, t, s), c is the 2D context of the canvas, w/h is the width and height, t is the second, and s is an empty object used to store the state of this function. Public widget functions are in _public function.js in the same folder.

```js
S.A3 = (c, w, h, t, s) => {
  const L = [["you", .17, .33, .30, 0], ["Understand", .40, .30, .22, 0], ["What", .70, .33, .17, 0], ["I", .19, .64, .20, 0], ["All", .43, .62, .14, 0], ["for your own good", .63, .84, .16, 1], ["obedient", .80, .60, .13, 0], ["！", .90, .84, .22, 1]];
  const beat = .4, len = L.length * beat + 1.4, tm = t % len, k = Math.floor(tm / beat), age = tm - k * beat;
  const m = Math.min(w, h), hit = k < L.length ? Math.exp(-age * 9) : 0;
  c.fillStyle = mixHex('#08080a', '#2a2a2e', hit * .5); c.fillRect(0, 0, w, h);
  const sx = (Math.sin(t * 91) * 6) * hit, sy = (Math.cos(t * 77) * 6) * hit;
  c.save(); c.translate(sx, sy); c.textAlign = 'center'; c.textBaseline = 'middle';
  for (let i = 0; i <= Math.min(k, L.length - 1); i++) {
    const [txt, fx0, fy, fz, red] = L[i], newest = i === k, port = h > w, fx = port ? .5 + (fx0 - .5) * .85 : fx0;
    const sc = newest ? 1 + .9 * Math.exp(-age * 16) : 1;
    c.font = `900 ${fz * m * (port ? .95 : 1.45) * sc}px ${SANS}`;
    c.fillStyle = red ? (newest ? '#ff4a32' : '#a3392a') : (newest ? '#ffffff' : '#55565c');
    c.fillText(txt, fx * w, fy * h);
  }
  c.restore();
};
```

