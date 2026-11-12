@echo off
setlocal
set "PYTHON=%~dp0..\.venv\Scripts\python.exe"
if not exist "%PYTHON%" (
    echo No se encontro el entorno .venv del curso.
    pause
    exit /b 1
)
"%PYTHON%" -u "%~dp0ventana.py"
if errorlevel 1 pause
