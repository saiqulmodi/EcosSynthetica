@echo off
title Ecos-Synthetica Server
start chrome http://localhost:8000
:loop
python -m http.server 8000
echo Server exited. Restarting...
timeout /t 2 >nul
goto loop
