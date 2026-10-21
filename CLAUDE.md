# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

The repo holds two unrelated projects.

## nutrition-research/ — 公共营养调研（中文）

Markdown research notes on public-nutrition and healthy-diet developments in China and abroad. `README.md` is the index; `04-open-questions.md` tracks claims still to verify and next research directions.

Conventions:
- Write in Chinese; keep English names for guidelines, journals and terms where that is standard (DGA, UPF, GLP-1, EAT-Lancet).
- Every claim gets a source link and an evidence tag: **[原文]** (checked against the official document or paper), **[二手]** (media/society summary, not yet checked), **[待核]** (sources conflict or a single non-authoritative source). Upgrade a tag only after reading the primary source.
- Prefer primary sources: WHO, 国家卫健委, 中国营养学会, USDA/HHS, peer-reviewed papers. Record dates precisely; distinguish publication date from effective date (e.g. GB 28050-2025 published 2025-03-27, effective 2027-03-16).
- When a claim is resolved, update both the topic file and the checklist in `04-open-questions.md`.

## promo-video/ — 60s vertical promo video

Two HTML implementations of the same 1080×1920 scenes:
- `video.html` — hand-written animation.
- `video-motion.html` — same scenes as Motion (motion.dev) timelines with springs; loads the vendored `vendor/motion-12.43.0.js` (no CDN).

Both expose `window.render(t)` (t in seconds, 0–60), which draws the frame for time `t` deterministically. Opening a page directly plays it in a loop, and `?t=<seconds>` shows a single frame. Keep scene changes in sync between the two files.

Rendering:
- `node render.cjs <outDir> [fps]` screenshots every frame via Playwright (default 30 fps); `PAGE=video-motion.html node render.cjs ...` renders the Motion version.
- `node render.cjs <outDir> 30 1.5,12,40` renders only stills at those times, for quick checks.
- `python3 music.py` generates `music.wav` (100 BPM synth pad, beat and UI cues timed to the scenes).
- Frames and audio are muxed into `miyuhe_promo_60s*.mp4` with ffmpeg; the exact command is not in the repo.

There are no tests or lint scripts.
