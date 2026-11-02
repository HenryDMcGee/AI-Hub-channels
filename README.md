# AI-HUB

A night-time channel grid that links every one of my projects from one screen. One `index.html`, no build step, no dependencies, no image or audio files for the hub itself. All channel art is inline SVG and every sound is synthesized in the browser.

Spec: [AI-HUB — Night Edition: Spec Sheet](https://claude.ai/artifact/XUH9Redzv7cTBvRYtWawcg). Mockup: [AI-HUB — Night Edition: Mockup](https://claude.ai/artifact/UYk5sQJYx9CNSym66UuVv2).

## Two modes, one file

The page picks its mode from where it is opened.

| Origin | Mode | What tapping a channel does |
| --- | --- | --- |
| A local file or `localhost` | **Real hub** | Apps zoom to a preview with a Start button, Jira and GitHub open a dialog listing their boards and repos |
| Any hosted address | **Demo** | A walkthrough of that app: what it is, how it works, the design process, a link to the real thing |

Only the demo is ever deployed. The real hub runs from a local clone on my laptop.

## Run the real hub as a laptop app

**Windows: `AI-HUB.exe`** (source in `app/`). A 3 MB native window around the hub using the Edge WebView2 runtime that ships with Windows 10/11, so it has its own taskbar entry and moon icon and can be pinned.

1. Clone the repo, then put `AI-HUB.exe` in the folder that *contains* the clone (it looks for a sibling `AI-Hub-channels` or `AI-Hub-channels-main` folder with `index.html`; or set `AIHUB_DIR`).
2. Run it, right-click its taskbar icon, **Pin to taskbar**.

On each start it opens the hub at once and runs `git pull --ff-only` in the background (no console). If that lands a new build in the first few seconds it reloads; later than that, the **UPDATED** pill appears. Web links (Start, Open the real app, repo links) open in your default browser; the hub's layout and settings are kept in `%LOCALAPPDATA%\AI-HUB`.

Build: `app/build.sh` (Go 1.22+, any OS).

**Without the exe:** `launch\AI-HUB.bat` / `launch/ai-hub.sh` pull and then open `index.html` as a Chrome or Edge app window; `launch\install-shortcut.bat` makes a Desktop shortcut for it.

## Using the hub

- **Boot screen.** Tap to begin. That first tap is what lets the browser play sound. Add `#full` to the URL to skip it.
- **Pages.** The pill tabs at the edges turn pages, or swipe on a phone.
- **Edit mode.** Press and hold any channel. Keep holding to drag it to another slot, including across a page edge. Tap ⓧ to remove a channel, Reset Layout to bring everything back, Done to finish.
- **Music.** The speaker beside the clock mutes and unmutes. The loop is an original: a warm pad on two chords, a sparse music-box line and a soft shaker, at 72 bpm.
- **Keyboard.** Tab moves between channels, Enter opens one, Esc closes anything.

## Adding a channel

Channels live in `ITEMS` in `.build/content.py`, their art in the mockup, and the walkthroughs in `DEMOS`. Rebuild with:

```
python3 .build/build.py
```

The build writes `index.html`. Commit the result. The `.build/` folder and `.build-art.json` are the source of the art and copy, not something the page loads.

## Releases and deployment

Pushing to `main` does nothing on its own. Publishing a GitHub release (tag `vX.Y.Z`) runs `.github/workflows/deploy.yml`, which deploys the repo to GitHub Pages. The demo is served from there and embedded on [mcgeehenry.com](https://mcgeehenry.com) as the Projects section.

To embed it elsewhere:

```html
<iframe src="https://henrydmcgee.github.io/AI-Hub-channels/" title="AI-HUB demo" style="width:100%;aspect-ratio:16/10;border:0;border-radius:20px" allow="autoplay"></iframe>
```

## Performance notes

The biggest fix was not the art at all: the iPhone audio-unlock trick looped a zero-length silent WAV in an `<audio>` element from the first tap onward, which pinned a core in every browser (main thread ~60 → ~900 ms per second). It is now half a second of real silence and only created on iOS.

The channel art is inline SVG with SMIL animations. Left to themselves, every animated tile repaints at 60 fps, which made the first build lag in a normal browser. The build now:

- pauses every SVG clock and advances only the art that can be seen (the visible page, or the open dialog) from one 15 fps ticker (`ANIM_FPS` in `.build/build.py`);
- paints the star field once on a canvas and animates only a handful of twinkles with CSS opacity, which the compositor handles off the main thread;
- splits STARR into a static sand/water layer and a small animated lettering layer so the noise and blur filters are rasterised once;
- isolates each tile's art in its own paint layer (`contain` + `translateZ(0)`), stops animations on a hidden tab and behind dialogs, and honours `prefers-reduced-motion`.

- adapts: a frame monitor drops to a lighter tier (8 fps art, no twinkles) and then to still art if more than a quarter of frames run long. `?tier=0|1|2` forces a tier, `?perf=1` shows fps, long-frame share, tier and device info in a corner.
- walkthrough screenshots are 1400 px WebP (~60–80 KB each) and are fetched quietly right after the grid appears, so no step waits on the network.

Headless profile (Chromium, software rasteriser): idle main-thread time went from ~270 ms per second to ~60.

## Demo landing

In demo mode the hub opens on the mcgeehenry.com hero (portrait, name, role, claim, Wells Fargo line, See the work / Get in touch) instead of the Tap to begin screen. The channel grid sits to the right on desktop and below on phones: click the Projects · AI-HUB tab or See the work, press → or scroll, or swipe up on a phone. On the grid, About Henry (or ←, or a swipe down on a phone) goes back. The last screen is remembered for the browser session. Real mode on the laptop is unchanged. `?landing=0` skips it.

## Demo CRM

`demo/crm/index.html` is the real Internship CRM UI running on sample data: the Claude capabilities (`db`, `user`, `mcp`) are replaced by a small in-memory shim at the top of the file, so adding, editing, Autofill and the Live activity feed all work, but nothing persists past the tab. It ships inside the hub: the walkthrough's Try-it step opens `demo/crm/index.html` in a full-screen view inside the hub itself (an iframe with a Back bar), so no new tab and no link hand-off to the host page is needed and is also published on its own at https://claude.ai/artifact/WDjxaCiJ8uqrS9vKwmubvc. Rebuild it from a fresh copy of the real CRM by re-running the shim insertion in `/crm-preview` (see the commit that added it).

## Demo Internship Watch

`demo/watch/` is the real Internship Watch dashboard front end (`frontend/index.html`, `app.js`, `style.css` and the three.js city background, copied from HenryDMcGee/internship-watch with asset paths made relative) plus `demo-api.js`, which answers every `/api` call from sample data in memory. No Cloudflare Access sign-in, no Worker, nothing saved. Search now and per-company Check now are switched off because a real search spends Claude credits; budgets, companies, titles, locations, applied/hidden/deleted all work against the sample data until the page reloads. The internship-watch walkthrough's Try-it step opens it inside the hub.

## Demo captures

`demo/` holds screenshots of the real apps running on dummy data, used by the walkthroughs. Nothing in them is real data.

## Constraints this was built under

No assets reused from the iPhone-style hub, and no trademarked material anywhere: no console maker's marks or music, and no GitHub, Atlassian or Jira logos. Those channels use their names and original glyphs.
