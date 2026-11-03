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

## Demo screens

Demo mode has seven screens, side by side on desktop and stacked on phones:

1. **Home**, the mcgeehenry.com hero (replaces the Tap to begin screen).
2. **AI-HUB**, the channel grid.
3. **About me**, the About section from mcgeehenry.com with the wiring photo.
4. **Video**, the YouTube video (youtube.com/watch?v=05zyH7eds8s). The player is created only while the screen is showing and removed on leaving, which stops playback. Where the host blocks other sites' frames (the claude.ai artifact does), a Watch on YouTube card links out instead; on GitHub Pages it plays inline.
5. **AI fluency**, the AI fluency section from mcgeehenry.com.
6. **Leadership**, coaching judo for kids with special needs at UH Manoa, counselor for the spring judo camp, and founding the Honolulu Japanese Language Exchange, with three photos (`demo/ow-*.webp`).
7. **Get in touch**, the contact section from mcgeehenry.com (Email me opens the site's contact section).

Every screen size: a bar fixed across the top (previous screen) and one across the bottom (next screen), labelled with the destination and shown only when there is one. ← → also work (on the hub they step through its pages of apps first), and phones can swipe up from the bottom / down from the top. The arrows hide while a walkthrough or demo app is open. On laptop-height windows the screens after the hub shrink type and spacing to fit (AI fluency goes two columns, Leadership puts the photos beside the text); if one still runs long, a fade and "Scroll for more" sit at the bottom. Animations and music run only on the hub; on phones the music starts switched off until the visitor turns it on. The landing's Get in touch button jumps straight to the Get in touch screen. The Video screen embeds the YouTube player where the host allows other sites' frames (GitHub Pages, mcgeehenry.com); claude.ai artifacts block them, so there it shows a Watch on YouTube card instead. Real mode on the laptop is unchanged; `?landing=0` skips the extra screens. Scrolling with a mouse wheel or trackpad also moves one screen per scroll; a screen with more to read scrolls to its end first.

## Demo tutorial

The first time a visitor reaches the hub in demo mode, a game-style guide starts: a text box from Henry with typewriter text, a dimmed screen with a glowing spotlight, and an animated hand tapping each channel in turn, then the bottom bar, then "Your turn!". Next / Enter / → advance (a click while text is typing finishes the line), ← goes back, Esc or Skip tutorial ends it. Finishing or skipping stores `aihub-tutorial-v1` in localStorage so it does not start again; a "? Tutorial" button on the hub replays it. `?tutorial=0` suppresses the automatic start. The per-channel lines live in `TUT_LINES` in build.py. Real mode never shows it.

## Demo CRM

`demo/crm/index.html` is the real Internship CRM UI running on sample data: the Claude capabilities (`db`, `user`, `mcp`) are replaced by a small in-memory shim at the top of the file, so adding, editing, Autofill and the Live activity feed all work, but nothing persists past the tab. It ships inside the hub: the walkthrough's Try-it step opens `demo/crm/index.html` in a full-screen view inside the hub itself (an iframe with a Back bar), so no new tab and no link hand-off to the host page is needed and is also published on its own at https://claude.ai/artifact/WDjxaCiJ8uqrS9vKwmubvc. Rebuild it from a fresh copy of the real CRM by re-running the shim insertion in `/crm-preview` (see the commit that added it).

## Demo Internship Watch

`demo/watch/` is the real Internship Watch dashboard front end (`frontend/index.html`, `app.js`, `style.css` and the three.js city background, copied from HenryDMcGee/internship-watch with asset paths made relative) plus `demo-api.js`, which answers every `/api` call from sample data in memory. No Cloudflare Access sign-in, no Worker, nothing saved. Search now and per-company Check now are switched off because a real search spends Claude credits; budgets, companies, titles, locations, applied/hidden/deleted all work against the sample data until the page reloads. The internship-watch walkthrough's Try-it step opens it inside the hub.

## Demo Jira board

`demo/jira/` is a read-only copy of the internship-watch (IW) Jira board: `data.js` is a snapshot of every IW epic, story, task and sub-task with descriptions and acceptance criteria (taken Nov 1, 2026), and `index.html` draws it as a Kanban board (To Do / In Progress / Done) with search, an epic filter, an Epics view with progress per phase (the view it opens on), and a detail drawer per card. Nothing can be moved or edited and nothing talks to Atlassian. No Atlassian logos or artwork are used. The Jira walkthrough's Try-it step opens it inside the hub. To refresh it, re-export the IW issues into `data.js`.

## Demo Course Planner

`demo/planner/index.html` is the real McCombs Course Planner page (The Codex of Courses) with made-up data: every professor is swapped for a fictional name, ratings are invented and no longer link anywhere, bid-history numbers are jittered, and storage is an in-memory stand-in seeded with a sample Spring 2027 plan and notes, so nothing is saved and there is no shared database. Course codes, titles, times and rooms are the public schedule. Rebuild it from a fresh download of the real planner with `python3 .build/make_planner_demo.py demo/planner/index.html` (run from a folder holding the real page as `real.html`). The planner walkthrough's Try-it step opens it inside the hub.

## Spec sheets

`demo/specs/` holds Henry's nine Internship Watch phase plans as page images (`phaseN-K.webp`, rendered from the PDFs at 120 dpi) and a small viewer, `index.html`, with a phase list (a picker on phones) and next/previous buttons. Step 3 of the internship-watch walkthrough has a "View all 9 spec sheets" button that opens it inside the hub. A walkthrough step can carry such a button with `btn={"label", "embed", "name"}` in `content.py`; a step image can set `ratio=` (its frame shape) and `zoom=True` (click to enlarge). To refresh a sheet, re-render its PDF with `pdftoppm -r 120 -png` and save each page as WebP under the same names.

## mcgeehenry.com

The demo is also the home page of mcgeehenry.com. That domain is served by the `resume-website` Cloudflare Worker (Workers Static Assets from `public/`) in the HenryDMcGee/Resume-Website repo, and pushing that repo's `main` deploys it. To ship the current hub there:

```sh
.build/deploy_site.sh /path/to/resume-website          # stage public/ and review the diff
.build/deploy_site.sh /path/to/resume-website --push   # stage, commit and push = deploy
```

It replaces `index.html` and `demo/` in `public/` (site-only pages such as `public/feedback/` are left alone) and writes `public/version.txt` with the hub commit. The page carries the site's title, description, canonical URL, link-preview tags and icons (`demo/site/`), and the Email and LinkedIn links are base64 in the source and assembled on load, as on the old site; Email opens a new message in Outlook on the web. The old resume site is kept on the `classic-site` branch of that repo.

## Demo captures

`demo/` holds screenshots of the real apps running on dummy data, used by the walkthroughs. Nothing in them is real data.

## Constraints this was built under

No assets reused from the iPhone-style hub, and no trademarked material anywhere: no console maker's marks or music, and no GitHub, Atlassian or Jira logos. Those channels use their names and original glyphs.
