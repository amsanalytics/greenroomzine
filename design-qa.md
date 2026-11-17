# Export verification — November 16, 2026

**Final result: passed** for the requested static website export, with the external chart dependency described below.

## Source and comparison

The source is the published first issue at `https://greenroom.artsintelligence.com/`, confirmed through the owner's authenticated Squarespace dashboard. Verification used the interactive browser available in Codex Desktop; no cloud desktop was attached.

Source and local export were compared at 1280 × 900 desktop and 390 × 844 mobile CSS viewports. The browser's captured image dimensions were 1265 × 889 and 375 × 812 respectively; each source/export pair has identical capture dimensions. Paired evidence is in `docs/desktop-comparison.png`, `docs/mobile-comparison.png`, and `docs/interior-comparison.png` (source left, export right).

## Required fidelity surfaces

- **Typography:** original Open Sans variable font and Saira Condensed Bold files are local. Computed font families match. Hero and interior heading wraps, weights, and relative sizes match the source comparisons.
- **Layout:** original responsive CSS and fluid-grid markup retained. All 42 section heights matched at the mobile viewport within one CSS pixel. Neither source nor export had horizontal viewport overflow. Desktop hero alignment and spacing match. The original large inter-section spacing is intentionally preserved.
- **Colors:** original CSS, navy section backgrounds, image overlays, white display text, and red reading-progress bar retained.
- **Images:** original photos, logos, image variants, fonts, and artwork downloaded. Higher-resolution original image data may appear slightly sharper than the source CDN's small responsive variants. No replacement artwork was generated.
- **Content:** all 168 source paragraphs and headings match after whitespace normalization. Captions and outbound links are retained. Internal section links were changed from original-domain URLs to local fragment links.

## Functional checks

- Local validator passed for 193 asset references, 17 fragment links, and every manifest entry.
- Both photo-strip galleries advance through their original images.
- Section navigation lands at the requested anchor (observed within one CSS pixel after smooth scrolling settles).
- Animated background pause controls switch to Play Background.
- Native local MP4 loaded with readyState 4 and duration 36.327956 seconds.
- All eight live Datawrapper chart documents loaded in the local page.
- Browser asset inventory showed no remote image, font, stylesheet, or script dependency in the top-level page after fixes. Charts remain embedded third-party documents.

## Fixes during verification

1. Two dynamically loaded CSS chunks initially returned 404. Their original files were added at the runtime's expected local paths; subsequent reloads loaded them successfully.
2. Dynamic Squarespace script URLs initially still pointed to the source CDN. The template script root and runtime paths were localized, then verified with a fresh asset inventory.
3. Whitespace-only text nodes in preformatted headings were preserved to retain original indentation.
4. The original runtime's localhost-only chunk-root override was disabled so static preview paths remain valid on localhost as well as other hosts.

## Practical limits

This is a faithful static export, not a replacement Squarespace editor. Eight Datawrapper/Embedly embeds and outbound links require internet access. A nonessential Squarespace census telemetry POST has no backend on static hosting; it is not needed for page display or interaction. Existing external links were preserved, not comprehensively audited for availability. The current site and DNS settings were not changed, and GitHub Pages was not enabled by this export.

## Preview repair and recheck

The first temporary preview server stopped, preventing deferred image and script requests from completing. Restarting it and reloading restored the visual assets. Background playback was resumed after the prior pause-control test. Successive screenshots confirmed that the isometric pattern moves, and the native video time advanced while visible.

All 46 image elements now have native source attributes, including 19 gallery images that previously depended on JavaScript to assign a source. After traversing the page, all 46 images decoded successfully. The local validator now rejects images that rely solely on data-src. It passes 212 asset references and 17 internal anchors.

Rechecked the 390-pixel mobile layout: no horizontal overflow and no images without a source. Evidence: `docs/restored-background.jpg` and `docs/restored-mobile.jpg`. Cloudflare preview verification is recorded separately after deployment; the custom domain remains on Squarespace.
