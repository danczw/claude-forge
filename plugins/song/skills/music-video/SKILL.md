---
name: music-video
description: Create a code-rendered music video with Remotion in a song workspace, as kinetic typography (2D) or story (3D): audio prep, lyric alignment, storyboard, build, review, render. Use when the user wants to make, storyboard, render or revise a music video.
---

# Code-rendered music video

Work in the current directory. Check it has `songs/<slug>/` (song data), `tools/` (`new_song.sh`, `prepare.sh`, `transcribe.py`) and `video/` (Remotion); if not, ask before setting it up. Use the most complete song in `video/src/songs/` as the reference implementation.

Work in stages with checkpoints; commit atomically after each and push. Whenever a design choice is the user's, offer 2–4 options with a recommendation.

## 0. Brief and questions
Get: title + audio path; style (A kinetic typography / B story); concept in one sentence (story: who wants what, what stops them, how it ends); tone; 1–4 recurring motifs; one unifying frame every scene lives in (e.g. pages of one exam booklet, with shared page furniture and a margin "voice"); structure (e.g. chorus escalates, bridge breaks); palette (muted base, ink, one motif accent; no black/neon); fonts (show a still comparing 2–3 candidates); formats (16:9, optional 9:16; final 4K60); optional reference video (analyse frames, never copy) and delivery folder.
After reading the lyrics/transcript, ask one round of clarifying questions (which lines carry the joke, literal vs. abstract, escalation, ending, lead motif). Don't build until answered.

## 1. Audio prep (uv for Python, brew for tools)
1. `tools/new_song.sh <audio>` → `songs/<slug>/`, lyrics from tags.
2. The sung arrangement rarely matches the lyric sheet. Separate vocals (Demucs via `prepare.sh`), map vocal activity (RMS per 2 s), transcribe freely (`tools/transcribe.py`).
3. Write `lyrics.txt` as *sung*: one line per row, repeats in full, `@<seconds>` anchors at gaps.
4. `tools/prepare.sh songs/<slug>` aligns between anchors (stable-ts) and tidies; check against the transcript.
5. Fix misalignments in `lyrics.overrides.json` (`{"<line>": [[start, end], …]}`), never in generated `lyrics.json`. "X is late/early" notes are usually alignment fixes.
6. `data/audio.json` holds beats and envelopes: check tempo and steady gaps; lock looped phrases to the grid.

## 2. Storyboard (approve before building)
Table: **# · time · lyric/section · shot · gag/object**, stored as data in `shots.ts` (id, lines, start/end, context, aside, `out` transition).
- Times come from `lyrics.json`/`audio.json` via `timing.ts` (`L`, `E`, `nearestBeat`, `snap`), never by hand.
- Cut ~0.12 s before its line, snapped to the beat; transitions centred on the cut.
- Every gag reads at a glance, or gets replaced.

## Motion rules (non-negotiable)
- **Reading time:** final readable state ≥ 1.2 s before each cut (`at = min(planned, leave − 1.2 − writeDuration)`); run `node video/scripts/reading-time.mjs` before every render. Exception: the song itself runs straight on.
- **Transitions** 0.2–0.4 s. Long gags (~0.7 s page rip) only at section changes with ≥ 2 s gaps. 1–2 s page turns are too slow.
- **Calm:** text moves with intent, then holds. No idle wiggle, sway, beat-driven camera pumping; constant effect strength unless escalation is the point.
- **Invisible hand:** marks appear via stroke/clip reveal; never draw a pen or hand. Typing cursor sits after the last typed glyph.
- **Backgrounds breathe** with slow, damped grain/marks/light.
- **Physical gags look physical:** simple believable mechanics (tearing paper, not a cartoon shredder).

## 3. Build
Read [style-kinetic.md](style-kinetic.md) or [style-story.md](style-story.md).
- **Determinism:** frames render in parallel, out of order. Scenes are pure functions of `t` and seeds (`shared/math.ts`: `hash`, `noise1`, `fbm2`); no `useFrame`, state or `Math.random`.
- `fps` is a composition prop (`calculateMetadata` in `Root.tsx`): drafts 30, final 60.

## 4. Review with stills
You can't watch video; verify everything through frames.
1. Stills per scene: `node video/scripts/stills.mjs <CompositionId> <outDir> <seconds…>` → `sheet.jpg`; `video/scripts/shot-keys.mjs` lists shot key times.
2. Low-res draft, iterate on timestamped notes: pull frames (4/s strip for motion) before and after each fix; ask rather than guess.
3. After every render: ffprobe (resolution, fps, duration, both streams) and frames at every cut.

## 5. Render
- Output to git-ignored `songs/<slug>/out/<slug>_v<N>.mp4`: major per rewrite, minor per feedback round; approved final adds `_high_res`.
- Run detached with `nohup`, log beside the MP4 ending `exit <code> <timestamp>`; always give the user `tail -f <log>`.
- Draft: `--scale=0.6666666666666666` (720p; non-integer heights fail), 30 fps.
- Final: show metadata first, then `--scale=2 --props='{"fps":60,"quality":"final"}' --codec=h264 --crf=16 --pixel-format=yuv420p --audio-codec=aac --audio-bitrate=320k`. Copy to the delivery folder and verify with `cmp`.

## Environment gotchas (apply those matching this machine)
- WSL/Ubuntu 22.04: Chrome needs apt `libnss3` (brew NSS needs glibc 2.38). No ad-hoc pip.
- Homebrew ffmpeg lacks `drawtext`; reuse a filter label with `split=N`.
- CRLF font licence files can block commits; normalise them.
- Whisper medium on 8 CPU cores: ~9 min for a 4-minute song.
