@echo off
echo Starting Propalytic House Price Prediction App...
echo.

REM Check if Python is available in PATH
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found in system PATH
    echo Please install Python 3.8+ and add it to your PATH
    pause
    exit /b 1
)

REM Check Python version
echo Checking Python version...
python --version
if errorlevel 1 (
    echo Failed to check Python version
    pause
    exit /b 1
)

REM Check if we're in the right directory
if not exist "src\app.py" (
    echo Error: src\app.py not found
    echo Please run this script from the project root directory
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Run the Streamlit app
echo.
echo Starting Propalytic...
echo Open your browser and go to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

python -m streamlit run src/app.py

echo.
echo Application stopped. Press any key to exit...
pause >nul
