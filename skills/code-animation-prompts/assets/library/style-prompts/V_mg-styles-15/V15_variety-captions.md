# V15 Variety Captions

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: V mg-styles-15 · mg-styles-15
- Suitable for: 9:16 vertical screen variety show subtitles, please refer to the vertical screen subtitles

## Style prompt words

# Variety Show Kinetic Captions (Hanazi)

**Original film**: Meow Diary EP.07 "Happy Today" · 1080×1920 · 30 fps · 10 seconds · AI Judge Final Rating 7.64 / 10

**Source code**: [demos/18-hanazi/](../demos/18-hanazi)

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
Variety Show Kinetic Captions (Hanazi)

# Output (fixed)
- 1080×1920, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

#Suggested technical route
HTML DOM/SVG: multi-layer text-stroke floral components + spring pops + SVG burst/sweat/sparkle decorations over a pet-vlog footage layer (CC0 photos with Ken Burns + handheld shake + punch-ins)
(You may choose a better route if it clearly raises quality; say why.)

#Creativeseed
"Cute pet variety show vlog" variety show captions in its native habitat — reactive captions over a pet vlog.
- Base layer that feels like footage: CC0/PD cat or dog photos from /assets/images with slow Ken Burns, subtle handheld shake, snap punch-in zooms on 'moments' (you may also build a stylized scene if photos look weak).
- Flower character moments synced to beats: title "Happy Today" (fill gradient + thick white stroke + colored outer stroke + drop shadow, rounded heavy font), "???" bouncing question marks, "Shocked!!" inside a radial explosion box with speed lines + radial flash, "（Quietly)" small aside, "Jue Juezi" with sparkles, sweat drops, a "Cat Owner Certification" stamp.
- Motion: pop 0 → 1.15 → 1.0 in ~8 frames, per-character bounce with 2-frame stagger, slight rotation, gentle wiggle while holding; appear 2–3 frames after the audio/visual moment. High-saturation pink/yellow/cyan with white strokes.
Sound: bouncy variety-show bed (pizzicato/bass/claps) + boing, pop, ding, slide whistle, record scratch on '? ? ? '.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
Emotional decorative subtitles originating from the late stage of TV variety shows: multi-layered rounded fonts with elastic entrance, changing color and deformation following the character's emotions, and accompanied by percussive sound effects. It has now become a universal packaging language for vlogs, cute pets, interviews, and comedy creations. It has a large number of built-in flower character templates, and free flower character style packages are also circulated at Station B.
Visual features: Multi-layer stroked round/fat fonts, highly saturated contrasting colors + white edges + projection, elastic pop entry, appearing with sound effects, hand-painted decorative symbols (explosion frame/sweat drop/flash)
Key techniques: three-layer structure of fonts: fill color + thick white stroke + colored outer stroke/drop shadow (CSS can be simulated with multiple layers of text-shadow or SVG stroke)
Entry overshoot: scale 0→1.15→1.0 (about 8 frames), or bounce the wrong frame by 2 frames verbatim
Emotion matching: skewed handwriting for complaints, radioactive explosion boxes for surprise, and sweat drop symbols for embarrassment
The timing of appearance is aligned with the punchline/sound effects, 2~3 frames later than the voice, which is more natural
Long-stay floral with a slight wiggle to stay active

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

