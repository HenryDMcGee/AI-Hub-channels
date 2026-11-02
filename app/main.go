//go:build windows

// AI-HUB desktop app: a small native window (Edge WebView2) around the hub in the
// AI-Hub-channels folder. It has its own taskbar entry and icon, keeps the folder
// in sync with GitHub (git pull in the background), and sends web links to the
// default browser.
package main

import (
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"syscall"
	"time"

	webview2 "github.com/jchv/go-webview2"
	"golang.org/x/sys/windows"
)

// Folder names looked for next to AI-HUB.exe (and one level up), in order.
var hubFolders = []string{"AI-Hub-channels-main", "AI-Hub-channels", "."}

func findHub() string {
	if v := os.Getenv("AIHUB_DIR"); v != "" {
		return v
	}
	exe, _ := os.Executable()
	dir := filepath.Dir(exe)
	for _, base := range []string{dir, filepath.Dir(dir)} {
		for _, name := range hubFolders {
			p := filepath.Join(base, name)
			if _, err := os.Stat(filepath.Join(p, "index.html")); err == nil {
				return p
			}
		}
	}
	return ""
}

func git(dir string, args ...string) (string, error) {
	cmd := exec.Command("git", append([]string{"-c", "safe.directory=*"}, args...)...)
	cmd.Dir = dir
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true, CreationFlags: 0x08000000} // CREATE_NO_WINDOW
	out, err := cmd.Output()
	return strings.TrimSpace(string(out)), err
}

func fileURL(p string) string {
	return "file:///" + strings.ReplaceAll(filepath.ToSlash(p), " ", "%20")
}

func openExternal(u string) {
	if !(strings.HasPrefix(u, "https://") || strings.HasPrefix(u, "http://") || strings.HasPrefix(u, "mailto:")) {
		return
	}
	verb, _ := windows.UTF16PtrFromString("open")
	target, _ := windows.UTF16PtrFromString(u)
	_ = windows.ShellExecute(0, verb, target, nil, nil, windows.SW_SHOWNORMAL)
}

// Runs in every page before its own scripts: web links leave the app for the default browser.
const linkShim = `(function () {
  function ext(u) { return /^(https?:|mailto:)/i.test(u); }
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a || e.defaultPrevented) return;
    var u = a.href;
    if (ext(u)) { e.preventDefault(); e.stopPropagation(); window.aihubOpen(u); }
  }, true);
  var open0 = window.open;
  window.open = function (u) { if (u && ext(String(u))) { window.aihubOpen(String(u)); return null; } return open0.apply(window, arguments); };
})();`

func main() {
	hub := findHub()
	local := os.Getenv("LOCALAPPDATA")
	w := webview2.NewWithOptions(webview2.WebViewOptions{
		Debug:     false,
		AutoFocus: true,
		DataPath:  filepath.Join(local, "AI-HUB"),
		WindowOptions: webview2.WindowOptions{
			Title:  "AI-HUB",
			Width:  1280,
			Height: 860,
			IconId: 2, // rsrc: manifest is resource 1, the icon group is 2
			Center: true,
		},
	})
	if w == nil {
		openExternal("https://go.microsoft.com/fwlink/p/?LinkId=2124703") // WebView2 runtime download
		return
	}
	defer w.Destroy()

	_ = w.Bind("aihubOpen", func(u string) { openExternal(u) })
	w.Init(linkShim)

	if hub == "" {
		w.SetHtml(`<body style="background:#0b1424;color:#e8f1ff;font:16px system-ui;padding:40px">
<h2>AI-HUB folder not found</h2><p>Put AI-HUB.exe next to the <b>AI-Hub-channels</b> folder (or set AIHUB_DIR) and start it again.</p></body>`)
		w.Run()
		return
	}

	w.Navigate(fileURL(filepath.Join(hub, "index.html")))

	// Sync with GitHub in the background. If the pull lands a new build within the first
	// few seconds, reload straight away; later than that, show the hub's update pill instead.
	started := time.Now()
	go func() {
		if _, err := os.Stat(filepath.Join(hub, ".git")); err != nil {
			return
		}
		before, _ := git(hub, "rev-parse", "HEAD")
		if _, err := git(hub, "pull", "--ff-only", "--quiet"); err != nil {
			return
		}
		after, _ := git(hub, "rev-parse", "HEAD")
		if after == "" || after == before {
			return
		}
		w.Dispatch(func() {
			if time.Since(started) < 8*time.Second {
				w.Navigate(fileURL(filepath.Join(hub, "index.html")))
			} else {
				w.Eval(`(function(){var p=document.getElementById('update');if(p){p.hidden=false;p.querySelector('span').innerHTML='UPDATED · <b>CLOSE AND REOPEN TO APPLY</b>';}})();`)
			}
		})
	}()

	w.Run()
}
