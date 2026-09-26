@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Project environment was not found.
    echo Create it first with Python 3.11 and install requirements.txt.
    pause
    exit /b 1
)

echo Starting Personal Voice AI...
".venv\Scripts\python.exe" app.py

if errorlevel 1 (
    echo.
    echo The application stopped with an error.
    pause
)
endlocal