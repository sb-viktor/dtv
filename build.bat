@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

REM Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Compile the dtv.py script to an executable
echo Compiling dtv.py to an executable...
pyinstaller --onefile dtv.py

REM Check if the executable was created successfully
IF EXIST dist\dtv.exe (
    echo Build successful. The executable can be found in the dist directory.
) ELSE (
    echo Build failed.
    exit /b 1
)

pause