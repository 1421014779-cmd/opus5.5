---
paths:
  - "promo-video/**"
---

# Promo video

- `video.html` (hand-written animation) and `video-motion.html` (Motion timelines with springs) render the same scenes. When you change a scene in one file, make the same change in the other.
- Each page exposes `window.render(t)`, which draws the frame at time `t` (0–60 seconds) and depends only on `t`. Don't add time-based state, `Date.now()` calls or real timers inside `render`, because frame-by-frame rendering relies on it.
- `video-motion.html` loads Motion from the local copy in `vendor/motion-12.43.0.js`. Don't switch it to a CDN.
- The sound cue times in `music.py`, such as the drums starting at 12.3 s and stopping at 57.5 s, are hard-coded to match the scene timing. When scene timing changes, update the cues in `music.py`.

## Commands (run from `promo-video/`)

- Render a few stills to check a change: `node render.cjs /tmp/stills 30 1.5,12,40`, then look at the `still_<t>.jpg` files.
- Render the full frame sequence: `node render.cjs <outDir> [fps]` (default 30 fps). For the Motion version, prefix the command with `PAGE=video-motion.html`.
- Generate the soundtrack: `python3 music.py`, which writes `music.wav`.
- To preview a single frame in the browser, add `?t=<seconds>` to the page URL.
- The repo has no tests or lint. Use rendered stills to verify changes.
- The ffmpeg command that combines frames and audio into `miyuhe_promo_60s*.mp4` isn't in the repo. Ask before you overwrite an existing mp4.
