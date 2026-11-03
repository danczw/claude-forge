# Style B: story (Three.js via `@remotion/three`)

Follow the reference song's `story/` folder if it has one.
- `Story.tsx`: one `ThreeCanvas` per shot (hard cuts). Lock the edit with labelled placeholders, then build one set at a time.
- Lyrics live in the world (screens, signs, glass, paper), never as subtitles; at most one large centred line.
- 3D text: not drei `<Text>` (hangs headless). Draw on a 2D canvas texture (`CanvasPlane`), fonts via `WaitForFonts`.
- Silhouettes need light behind them (window, screen, fridge, sky); figures are unlit pure black. Code can't do faces.
- Close-ups need their own high-res surface. Flashbacks: distinct light plus a faded grade.
- Expect a reframing pass per set: camera inside objects, subject behind camera, text off-frame, too dark.
- WSL WebGL needs `--gl=swangle` (in `remotion.config.ts`); ~0.5 s/frame at any resolution (~1 h for 4 min).
