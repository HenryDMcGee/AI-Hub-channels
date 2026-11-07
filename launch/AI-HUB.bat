@echo off
setlocal
rem AI-HUB laptop launcher (Windows).
rem 1) pulls the latest hub from GitHub (skipped quietly when offline or when you have local edits)
rem 2) opens index.html as an app window (Edge, else Chrome: no tabs or address bar)
rem Change CHANNEL to "release" to follow tagged releases instead of main.
set "CHANNEL=main"

set "ROOT=%~dp0.."
pushd "%ROOT%" || exit /b 1
for /f "delims=" %%I in ('cd') do set "ABS=%%I"

rem Nothing here needs admin. If this folder is somewhere Windows protects (Program Files, C:\ root)
rem or was cloned from an admin terminal, pulling is skipped and the hub still opens.
set "CANWRITE=1"
(echo.>"%ABS%\.aihub-write-test") 2>nul || set "CANWRITE=0"
if exist "%ABS%\.aihub-write-test" del "%ABS%\.aihub-write-test" >nul 2>nul
if "%CANWRITE%"=="0" (
  echo AI-HUB: this folder needs admin rights to change, so updates are skipped.
  echo         Clone the repo into your user folder instead, e.g. %USERPROFILE%\AI-Hub-channels
  goto open
)

where git >nul 2>nul
if %errorlevel%==0 (
  if /i "%CHANNEL%"=="release" (
    git -c safe.directory="%ABS:\=/%" fetch --tags --quiet 2>nul
    for /f "delims=" %%T in ('git describe --tags --abbrev^=0 origin/main 2^>nul') do git checkout --quiet "%%T" 2>nul
  ) else (
    git -c safe.directory="%ABS:\=/%" pull --ff-only --quiet 2>nul || echo AI-HUB: offline or local changes - running the copy you already have.
  )
) else (
  echo AI-HUB: git not found - running the copy you already have.
)

:open
set "URL=file:///%ABS:\=/%/index.html"
set "PF86=%ProgramFiles(x86)%"
set "BROWSER="
if exist "%PF86%\Microsoft\Edge\Application\msedge.exe" set "BROWSER=%PF86%\Microsoft\Edge\Application\msedge.exe"
if not defined BROWSER if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" set "BROWSER=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
if not defined BROWSER if exist "%ProgramFiles%\Google\Chrome\Application\chrome.exe" set "BROWSER=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if not defined BROWSER if exist "%PF86%\Google\Chrome\Application\chrome.exe" set "BROWSER=%PF86%\Google\Chrome\Application\chrome.exe"
if not defined BROWSER if exist "%LocalAppData%\Google\Chrome\Application\chrome.exe" set "BROWSER=%LocalAppData%\Google\Chrome\Application\chrome.exe"

if defined BROWSER (
  start "" "%BROWSER%" --app="%URL%" --window-size=1366,860
) else (
  start "" "%URL%"
)
popd
endlocal
