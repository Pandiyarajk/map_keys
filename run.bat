@echo off
REM Run script for Key Mapper application

echo ========================================
echo Key Mapper - Starting Application
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found.
    echo Running setup first...
    call setup.bat
    if errorlevel 1 exit /b 1
)

REM Activate virtual environment and run
call venv\Scripts\activate.bat
python gui.py

if errorlevel 1 (
    echo.
    echo ERROR: Application failed to start
    echo Make sure all dependencies are installed
    pause
    exit /b 1
)
