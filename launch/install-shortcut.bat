@echo off
rem Puts an "AI-HUB" shortcut on the Desktop that runs AI-HUB.bat minimised, with the hub icon.
set "HERE=%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$d=[Environment]::GetFolderPath('Desktop'); $s=(New-Object -ComObject WScript.Shell).CreateShortcut(\"$d\AI-HUB.lnk\");" ^
  "$s.TargetPath='%HERE%AI-HUB.bat'; $s.WorkingDirectory='%HERE%'; $s.IconLocation='%HERE%ai-hub.ico'; $s.WindowStyle=7; $s.Description='AI-HUB (pulls the latest build, then opens)'; $s.Save();" ^
  "Write-Host 'Shortcut created:' \"$d\AI-HUB.lnk\""
pause
