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

1. Clone the repo: `git clone https://github.com/HenryDMcGee/AI-Hub-channels`
2. Make a desktop shortcut whose target opens the browser in app mode on the local file, for example on Windows:
   ```
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --app="file:///C:/path/to/AI-Hub-channels/index.html"
   ```
   Edge works the same way with `msedge.exe --app=…`. The hub opens in its own window with no address bar.
3. To update, fetch and check out the release tag: `git fetch --tags && git checkout v0.1.0`

Layout and the music setting are saved in the browser (`aihub-layout-v1`, `aihub-music`). The checked-out version is logged to the console on load.

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

## Demo captures

`demo/` holds screenshots of the real apps running on dummy data, used by the walkthroughs. Nothing in them is real data.

## Constraints this was built under

No assets reused from the iPhone-style hub, and no trademarked material anywhere: no console maker's marks or music, and no GitHub, Atlassian or Jira logos. Those channels use their names and original glyphs.
