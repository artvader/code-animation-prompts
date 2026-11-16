# Browser animation export

## Time interface

The included renderer is used to provide the following interface to HTML (without directly rendering arbitrary web pages):

```js
window.renderAt = async function (t) {
  // t It’s seconds; position all animations, particles, cameras, and subtitles to this moment. draw(t);
};
```

After the page receives `?export=1`, it does not start the requestAnimationFrame/timer loop and stops the CSS self-playing animation; `renderAt(t)` only advances the screen. Random particles are generated with a fixed seed when started, or calculated directly from index and time. Asynchronous resources should be ready before `renderAt` returns. The canvas's pixel dimensions, CSS viewport, and output dimensions are the same, and does not include player controls.

`../assets/starter/index.html` is a minimal reproducible example. The HTML in the original material is not guaranteed to provide this interface; a copy is saved during adaptation and the original library is not modified. Existing projects such as Remotion use their own export tools.

## Dependencies

Retrieval and installation only require the Python 3.10+ standard library. Only browser rendering requires additional installation:

```bash
python -m pip install playwright
python -m playwright install chromium
ffmpeg -version
```

FFmpeg needs to be installed and located in PATH; for the installation method, see [FFmpeg official download](https://ffmpeg.org/download.html).

## Export

```bash
python "<skill-directory>/scripts/render_video.py" ./index.html \
  --output ./output/video.mp4 --duration 12 --fps 30 --width 1920 --height 1080
```

If you have prepared soundtrack/dubbing, you can add `--audio ./narration.wav`. The script will not generate sound, nor will it automatically loop short audio; it will fill in silence or crop to the length of the video. Silent by default. Stop when the output file already exists, just choose another file name.

The script loads HTML using the local HTTP service and binds the random port of `127.0.0.1`; dependent resources should be placed in the directory where the HTML is located and its subdirectories. Screenshot frame by frame according to `t = frame / fps`, encoded to H.264 / yuv420p using FFmpeg. Size must be a positive even number; frame number is `ceil(duration × fps)`, actual duration may be rounded up to one frame. By default, the entire output viewport will be captured.

Long films or high resolutions render frame by frame slower. First export a small section to check the visuals and dependencies, and then render the entire film. Reports specific missing items or interface errors when output fails, without claiming completion.
