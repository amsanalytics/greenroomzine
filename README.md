# Green Room Zine

Static export of **The Green Room, Issue No. 1: From Return to Reset**, retrieved from the owner's Squarespace site on November 16, 2026.

Source: https://greenroom.artsintelligence.com/

## Preview

Serve this folder with any static web server. No build step or package installation is required:

```sh
python -m http.server 4174 --bind 127.0.0.1
```

Then open http://127.0.0.1:4174/ . Use an HTTP server rather than opening `index.html` as a file, because the original runtime loads script modules.

## What is preserved

- Original page markup, editorial text, captions, links, responsive grids, typography, colors, and section styling.
- Local images and responsive image variants, original fonts, stylesheets, and the page's required JavaScript chunks.
- Both photo galleries, animated backgrounds and pause controls, the scrolling report heading, reading-progress bar, and internal section navigation.
- The 36-second umbrella background video, saved as a local MP4 from the original stream.
- All eight interactive Datawrapper charts, retained as the original live embeds.

`asset-manifest.json` maps the retrieved asset URLs to local files. Original artwork, font, and third-party runtime rights remain with their respective owners; this repository does not relicense them.

## Portability notes

The page's visual assets and runtime are local. Datawrapper/Embedly charts and outgoing article links still require internet access. The export retains Squarespace's frontend runtime for fidelity, but it does not include the Squarespace editor, account tools, or a server backend. The runtime may attempt a nonessential `/api/census/render-batch` telemetry request, which a static server does not implement. Explicit performance/error-reporting script tags were omitted.

Internal section links now use local fragments. The native video no longer depends on expiring Squarespace streaming URLs. No DNS, Squarespace subscription, or hosting settings were changed. This commit alone does not publish the site or enable GitHub Pages.

## Validation

Run `python validate.py` to check local references and anchor targets. Browser verification and source comparisons are summarized in `design-qa.md`.
