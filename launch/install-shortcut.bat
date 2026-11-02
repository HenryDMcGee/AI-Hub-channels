@echo off
rem Puts an "AI-HUB" shortcut on the Desktop: moon icon, no console window (runs AI-HUB.bat through a headless console).
rem Run it normally (double-click). It only writes to your own Desktop and never needs admin.
set "RUNNER=%~dp0AI-HUB.bat"
set "ICON=%~dp0ai-hub.ico"
powershell -NoProfile -Command "$d=[Environment]::GetFolderPath('Desktop'); $s=(New-Object -ComObject WScript.Shell).CreateShortcut((Join-Path $d 'AI-HUB.lnk')); $s.TargetPath=Join-Path $env:WINDIR 'System32\conhost.exe'; $s.Arguments='--headless cmd.exe /c \"' + $env:RUNNER + '\" quiet'; $s.WorkingDirectory=Split-Path $env:RUNNER; $s.IconLocation=$env:ICON + ',0'; $s.Description='AI-HUB: syncs with GitHub, then opens'; $s.Save(); Write-Host ('Shortcut created: ' + (Join-Path $d 'AI-HUB.lnk'))"
pause
