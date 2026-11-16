# V8 Cyberpunk Interface (Cyberpunk HUD / FUI)

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: V mg-styles-15 · mg-styles-15
- Suitable for: science fiction interface

## Style prompt words

# CYBERPUNK HUD / FUI Cyberpunk HUD / FUI (Fictional UI)

**Original film**: KESTREL-9 TARGET ACQUIRED · 1920×1080 · 30 fps · 10 seconds · AI review final rating 7.93 / 10

**Source code**: [demos/22-hud/](../demos/22-hud)

## How to use

1. Create a new empty folder and open an AI assistant (such as Claude Code) that can write code and execute commands. This machine needs to be able to run web rendering (Node + Chrome) and ffmpeg.
2. Copy the entire "prompt word" below and send it.
3. If you want to change it to your own content: change the story, brand name, copywriting and color matching in `Creative seed`, or change the size in `Output` (for example, vertical screen 1080×1920). Don't delete the paragraph `Signature features`, it is the basis for this style to be instantly recognized.
4. Want to improve further: After the finished film is released, open another AI to review it with [rubric.md](../rubric.md), and post the review comments back to the production AI for another round of revisions. The original film was changed twice like this.

## Prompt word

```text
You are the director, motion designer, engineer and sound designer of ONE 10-second motion-design film.
The goal is the most classic, yet most stunning form of this style — award-shortlist / high-end commercial quality. A clean,
template-looking result is a fail. Benchmarks: Buck, ManvsMachine, Ordinary Folk, Giant Ant, Territory Studio, Apple keynote
motion, Pentagram motion identities, top Behance/Motionographer features, top Douyin/Bilibili designer accounts.

#Style
Cyberpunk HUD / FUI Cyberpunk HUD / FUI (Fictional UI)

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: SVG/Canvas FUI layers + Three.js wireframe hologram; seeded random data; glow/scanline post pass
(You may choose a better route if it clearly raises quality; say why.)

#Creativeseed
"TARGET ACQUIRED" Cyberpunk HUD / FUI, film-UI grade (Territory Studio-level density & restraint).
- Deep teal-black; cyan #00E5FF linework with orange/red #FF6A00 alert state; hex grid, concentric rotating rings with ticks, radar sweep (conic) with blips, data columns (monospace numbers rolling 3–5 frames then settling), typewriter status lines with cursor, sparkline graphs, a central Three.js wireframe hologram (globe or drone) with scanlines.
- Layered build-up: lines draw on in hierarchical staggered order → data comes alive → a target is found → lock brackets snap 1.4 → 1.0 (fast-out slow-in) → everything flips to alert orange with 'TARGET LOCKED / target lock', coordinates "N31°14′ E121°29′".
- Glow, slight chromatic aberration, scanlines, restrained micro-glitches.
Sound: darksynth pulse + HUD beeps, scan sweeps, ascending lock-on tone, alarm on lock.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
Heads-up display packaging that simulates the interface of science fiction movies/games: green and orange neon line frames, target lock boxes, radar scans, and small text in data streams. It is used as the default skin for "technical sense" in technology digital evaluation, game editing (Cyberpunk 2077, EVA Second Creation), military and aerospace science popularization, and AI product demonstrations. The AE HUD case tutorial of Station B has been viewed 200,000 times.
Visual features: cyan/orange neon wireframe, target lock box and crosshair, radar/circular scan loop, constant-width small font data stream and typewriter text, hexagonal grid and glow
Key techniques Wireframe growth: SVG stroke-dasharray/dashoffset stroke animation, elements are expanded according to hierarchical staggered frames
Loop radar: conic-gradient scanning sector rotation loop + target point flashing
Digital scrolling: random numbers jump quickly for 3~5 frames before settling on the true value; text typewriter + cursor flashing
Lock box: The four-corner brackets shrink the adsorption target from large to small (scale 1.4→1.0 + fast out and slow in)
Global outer glow (glow) + slight color difference + scan line overlay for unified texture

# How to work
1. Treatment. Write down one clear idea: a hook in the first 0.5 s (never open on more than 0.3 s of empty or black), an
   escalation, one unmistakable hero moment at ~60–75 % of the runtime, and a composed end frame held ~0.8–1.2 s with living
   micro-motion. Map every signature feature above to a moment. Keep one cue sheet (beats and hit times) that both the
   picture and the sound read from.
2. Key frames before motion. Build the look, render stills at 6–10 key times and actually look at them. Each still should be
   poster-worthy: composition, hierarchy, negative space, type set properly (kerning, line-height, weight contrast, Latin glyph coverage
   punctuation, ~5 % safe margins). Iterate until nothing looks default, generic, cramped or "AI-template".
3. Motion. Build the choreography and preview at low resolution. Step through the fastest moves frame by frame: spacing,
   easing, arcs, overlap, anticipation and follow-through, motion blur. No unintended dead spans; the energy follows the music.
4. Sound. Write genre-correct music and sound design locked to the cue sheet. Check that visual hits land on audio onsets.
   Master to the output spec.
5. Final. Render at full resolution (motion blur where apt), then check: exactly 10.00 s, resolution, fps, audio present and at
   the right loudness, no black frames, no fallback fonts or tofu, no clipped elements at the frame edges, no shimmer on thin
   lines, no gradient banding. Fix and repeat until you would submit it to a festival.
6. Write an honest self-critique: what is strongest, what is weakest, what you would do with more time.

# Rules
- Rendering must be deterministic: every frame is a pure function of time t. Seeded randomness only; physics and particles
  precomputed or closed-form; no real-time clocks; no state-triggered CSS transitions. A reliable route: a web page that can
  draw any time t on request, captured frame by frame with a headless browser and encoded with ffmpeg (or a Blender script
  that renders a PNG sequence).
- Assets: only CC0 / public domain / OFL / Apache / free-for-commercial-use. Record each source and licence in CREDITS.md.
  No real brand trademarks; invent brand names.
- On-screen text must be correct and natural: idiomatic English, proper English punctuation, no typos.

# Craft checklist (what a jury looks for)
- Style authenticity: an expert names the style in one second; every signature technique is present and executed correctly.
- Motion craft: purposeful easing (no linear unless mechanical by design), overlap and stagger, anticipation and
  follow-through, arcs, squash and stretch where the style allows, consistent physics, motion blur where apt; transitions
  carried by elements, not crossfades.
- Rhythm: hits locked to the music; contrast between busy and calm; no monotony.
- Design: strong composition, grid, typographic hierarchy, controlled palette; texture and finishing (grain, glow, vignette)
  only where the style wants it; nothing looks accidental.
- Technical polish: no jitter (unless intended), no popping, no aliasing, no banding, no fallback fonts, no half-loaded images.
- Sound: genre-correct, musical, synced, mastered.

# Before you deliver, score yourself honestly
1–10 on style fidelity, concept wow, motion craft, design & typography, finish & texture, sound & sync, technical
(6 = template-level, 8 = high-end agency, 9 = award shortlist). Aim for 9; fix whatever scores lowest first.

# Deliver
video.mp4, plus a short report: the concept in two sentences; a beat sheet with timecodes; how each signature feature is
realised; the tech route; check numbers (duration, resolution, fps, loudness, true peak); your honest top-3 weaknesses.
```

