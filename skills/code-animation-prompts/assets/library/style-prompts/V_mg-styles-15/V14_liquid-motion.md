# V14 Liquid Motion

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: V mg-styles-15 · mg-styles-15
- Suitable for: soft transitions, emotional flow

## Style prompt words

# Liquid Motion Liquid Motion

**Original film**: drop. "Everything begins with a drop" · 1920×1080 · 30 fps · 10 seconds · AI review final rating 7.57 / 10

**Source code**: [demos/07-liquid/](../demos/07-liquid)

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
Liquid Motion Liquid Motion

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML WebGL2 fragment shader: 2D SDF metaballs (smooth-min) + fake 3D lighting from field gradient normals, text SDF for the logo
(You may choose a better route if it clearly raises quality; say why.)

#Creativeseed
Liquid logo genesis — glossy, organic, high energy.
- Deep plum ground; glossy candy liquid (hot orange → pink → violet) with specular highlights and fresnel rim so it reads like thick 3D liquid, not flat blobs.
- 0–2s: droplets fall and splash with squash on landing; 2–4s: blobs merge via metaball fusion — stretched necks, snap, 2–3 frame rebound; secondary droplets follow 2–3 frames late;
- 4–6s: a big liquid wave floods across the frame as a transition (wavy front with 3–5 phase-offset bulges);
- 6–8.5s: the liquid coalesces into a wordmark (e.g. "FLUX") — text SDF blended with the metaballs;
- 8.5–10s: a last drip falls from the logo and ripples; hold.
Ease: flung, never uniform (cubic-bezier(0.22,1,0.36,1)).
Sound: bubbly gloops, pour, splash, drip, deep bass swell under a glossy synth bed.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
Graphics flow like liquid, drawing, dripping, merging: the transition is a splash of paint across the screen, the logo coalescing from a drop of liquid. Organic, decompressive, high-energy, widely used in music videos, food and beverage advertising and transition packaging.
Visual characteristics: wave edge transition, brushing and dripping, metaball fusion, secondary droplet following, organic curves are never straight
Key techniques: liquid transition: mask path hand K, sweep the wavy front edge across the screen, add 3~5 out-of-phase bumps to the front edge
General forgery method for metaball fusion: Gaussian blur (20px+) → Increase the contrast threshold (use Levels to tighten for AE, feColorMatrix alpha threshold for Web), and the two balls will automatically 'stick' when they are close to each other.
Drawing-Breaking-Rebound: When the main shape leaves, a thin neck is left, and both ends rebound 2~3 frames at the moment of breaking.
The easing is fast in front and slow in cubic-bezier(0.22,1,0.36,1). The liquid will only be 'slapped' out and not at a uniform speed.
The secondary droplet delays the main body for 2~3 frames to follow (follow-through), and flattens when it lands.

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

