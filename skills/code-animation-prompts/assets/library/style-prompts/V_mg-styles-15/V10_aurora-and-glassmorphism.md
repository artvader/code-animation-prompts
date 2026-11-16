# V10 Aurora & Glassmorphism

Output language: Use English for all subtitles, narration, titles, labels, signs, and other readable text unless the user explicitly requests another language.

- Category: V mg-styles-15 · mg-styles-15
- Suitable for: soft glow, quiet passages

## Style prompt words

# Diffusion Gradient / Glass Morphism Gradient Blur (Aurora) & Glassmorphism

**Original film**: Aurora — think in light「Thinking, own light」 · 1920×1080 · 30 fps · 10 seconds · Final AI review 8.07 / 10

**Source code**: [demos/12-aurora-glass/](../demos/12-aurora-glass)

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
Gradient Blur (Aurora) & Glassmorphism

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML WebGL: aurora mesh-gradient shader + glass refraction (SDF lens, chromatic dispersion) + DOM/CSS backdrop-filter glass cards
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「Liquid Glass」2025–26 AI-product-launch aesthetic: slow, translucent, expensive.
- Deep indigo-black base; 4–5 aurora blobs (violet/blue/cyan/magenta, adjacent hues only) drifting on bezier paths, blending into a mesh gradient, 3–5% noise dithering (no banding).
- Frosted glass cards (backdrop blur ~30px, 5–10% white fill, 1px 30% white inner highlight, large radius) float in with parallax depth and slight 3D tilt; micro-UI inside (chat bubble, voice waveform, toggles) animates with opacity + 8px rise.
- WOW: a Liquid-Glass lens (true refraction, chromatic dispersion on the rim, specular edge) glides across and magnifies the aurora and the cards.
- Title (invented product, e.g. "Aurora — think in light") in a light elegant sans; sine/breathing easing everywhere; nothing fast.
Sound: ambient cinematic pad, soft shimmer, very subtle UI ticks.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
A large area of Gaussian blurred colored light spots (aurora/mesh gradient) slowly drifts as the base, with frosted translucent glass cards floating on top. Apple's iOS 26 Liquid Glass and the release of various AI products have promoted this style as the default vision of 2024-2026 technology brand films, with a temperament of 'slow, transparent and advanced'.
Visual characteristics: large color spot Gaussian blur drift, frosted glass card, 1px highlight stroke, adjacent color low contrast color matching, slow breathing rhythm
Key techniques: Bottom aurora: 3~5 solid color large circles blur 80~150px, each drifting cycle along the Bezier path for 20~40 seconds, blending with each other to create a mesh gradient feeling
Glass card recipe: background-filter blur(20~40px) + white 5~10% fill + 1px white 30% inner stroke + large radius rounded corners
Use 2~3 adjacent colors (purple, blue, green/orange and pink) for color matching. Contrasting colors will make them dirty; bright spots on a dark background are more effective than bright ones.
Global stacking 3~5% noise to prevent banding (crossed with grainy texture techniques)
Easing is close to linear or sine breathing curve, everything is slow - fast movement will immediately destroy the temperament; text entry only uses opacity+8px displacement

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

