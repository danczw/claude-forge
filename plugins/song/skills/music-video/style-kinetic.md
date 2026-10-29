# Style A: kinetic typography (2D DOM/SVG, no WebGL)

Follow the reference song's `type/` folder if it has one.
- **The lyric performs its meaning** (falls, stacks, freezes, gets graded, splits). Props may underline it; words stay the hero, never a static subtitle.
- Vary techniques across scenes: variable-font axes, words as objects (tally sticks, signs, signal bars), counters, stamps, lists. One file per section in `scenes/`.
- Kit: `Glyphs` (per-glyph transforms), `anim` (`seg`, `ease`), `Pen` (invisible-hand strokes), `transition` (tear, zoom, shrink, ink, pan, wipe, flash, dissolve), `chrome` (page furniture, margin `Aside`), `bg`, `page`.
- Load fonts with `FontFace` and await them before rendering.
- Speed (8 cores): 720p30 draft ~10 min, 4K60 final ~2 h 20 min.
