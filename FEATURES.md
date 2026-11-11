# AI-HUB features

Everything the hub does today, grouped by where it runs, with the newest feature last. Details for each live in the [README](README.md).

Status: **Shipped** is live (in the real hub, the demo, or both). **Prototype** works for testing but isn't the finished feature. **Planned** is designed but not built yet.

## Hub (both modes)

| Feature | What it does | Status |
| --- | --- | --- |
| Channel grid | Night-themed grid of channels, one per project, with original inline SVG art and no image files | Shipped |
| Pages | Pill tabs at the edges (or a swipe) move between pages of 12 channels | Shipped |
| Edit mode | Press and hold to drag channels between slots and pages, remove them, or reset the layout | Shipped |
| Music and sounds | An original synthesized loop and UI sounds, with a mute button beside the clock | Shipped |
| Keyboard control | Tab between channels, Enter to open, Esc to close | Shipped |
| Performance tiers | Art animates at 15 fps only where visible, and drops to lighter tiers on slow machines (`?tier=`, `?perf=1`) | Shipped |

## Real hub (laptop)

| Feature | What it does | Status |
| --- | --- | --- |
| App previews | Tapping an app zooms to a preview with a Start button | Shipped |
| Jira and GitHub dialogs | List the Jira boards and GitHub repos | Shipped |
| Windows app | `AI-HUB.exe`, a native window with its own taskbar icon, which pulls the latest build on start and shows an UPDATED pill | Shipped |
| Launch scripts | `launch/` scripts open the hub as an Edge or Chrome app window after a `git pull`, with a desktop shortcut installer | Shipped |

## Demo (mcgeehenry.com and the public artifact)

| Feature | What it does | Status |
| --- | --- | --- |
| Seven screens | Home, AI-HUB, About me, Video, AI fluency, Leadership, Get in touch | Shipped |
| Screen navigation | Top and bottom bars, arrow keys, swipes and mouse wheel move one screen at a time, with vertical transitions | Shipped |
| Channel walkthroughs | Each channel opens a step-by-step story of the app: the problem, the design process, how it's built, and a Try it step | Shipped |
| In-hub demo apps | CRM, Internship Watch, a read-only Jira board, the McCombs Course Planner and the spec-sheet viewer run inside the hub on sample data | Shipped |
| GitHub list | Opens a list of the AI app repos plus a link to the GitHub profile | Shipped |
| Image zoom | Walkthrough images can open full size in a lightbox | Shipped |
| Video | YouTube video that loads on click (and links out where frames are blocked) | Shipped |
| Tutorial | Game-style guide on the first visit with a spotlight and tapping hand, plus a replay button | Shipped |
| Demo-only channel set | Personal channels (site, Mars) are hidden in the demo | Shipped |

## mcgeehenry.com

| Feature | What it does | Status |
| --- | --- | --- |
| Home page deploy | `.build/deploy_site.sh` ships the demo as the site's home page through the Resume-Website repo | Shipped |
| Contact links | Email (opens Outlook on the web) and LinkedIn, assembled in the browser so the addresses aren't plain text in the source | Shipped |
| Feedback page | `/feedback` takes free-form notes from user testers, with a private responses page | Shipped |
| Visit path log | Records each visitor's decisions (screens, channels, walkthrough depth, demo apps, reaching out) with no names or typing | Shipped |
| Happy-path report | `/insights` compares every visit with the seven-step happy path: funnel, what people did instead, walkthrough depth, input methods, routes and a per-visit log | Shipped |
| Recording switch | Turn recording off or on for the whole site, and choose whether your own browser is counted | Shipped |
| Mouse heatmaps | Per-screen movement and click heatmaps drawn over a live preview of each screen | Shipped |
| Microsoft Clarity | Recordings and heatmaps tied to the same visit IDs, added at deploy time | Shipped, waiting on a Clarity project ID |
| Private-page sign-in | `/insights` and the feedback responses sit behind Cloudflare Access (email code), shared with Internship Watch | Shipped |

## Latest: App Store

| Feature | What it does | Status |
| --- | --- | --- |
| App Store | A shared store inside AI-HUB where students publish their own apps and add classmates' apps to a personal dashboard | Prototype in the demo (one browser); shared version planned |

How it would work:

- **Publish.** A student pastes a publicly shared Claude artifact link, then adds a name, a one-line pitch, a category and a tile style (color, pattern, icon). A GitHub repo is optional and shows below the app as Source code, with View code and Fork it. The app goes live immediately and can be edited or unpublished anytime.
- **Browse and add.** Everyone sees every published app, with search, categories, New this week and Popular in your class. Add to my dashboard puts the tile in the student's next free slot. Removing it only takes it off their own dashboard.
- **Personal dashboards.** Each student's channel grid is saved to their account, starts with the App Store tile, and follows them across devices. Tiles point to the shared listing, so author updates reach everyone.
- **Sign-in and safety.** UT-email sign-in, generated tile art only (no uploaded images or logos), a report button with an admin hide switch, and a daily check that grays out apps whose links stop working.

Wireframe: [AI-HUB App Store wireframe](https://claude.ai/artifact/FjeTmAeYdgrXoVHq8tKM9C) (dashboard, store, app listing and publish form, clickable).

Prototype (in the demo now): the App Store channel is the last channel on the dashboard. Browse, search and filter apps, add them to the dashboard (they take the next free slot and glow NEW), publish your own with a shared Claude artifact link and an optional GitHub repo, edit or unpublish it, and press and hold a tile to rearrange or remove it. Everything is saved in the visitor's own browser, so nothing is shared between people yet. The store lists Henry's demo apps (which open inside the hub) and sample listings. `?store=0` turns it off. Test copy: [AI-HUB — App Store test](https://claude.ai/artifact/9PsttxYzjQjdrmvv7XrPjB).

Still to build for the shared version: UT sign-in, a store database and per-student dashboards on the server, a report queue with an admin hide switch, and a daily link check.
