@echo off
chcp 65001 >nul
cls
echo 成功運行FruitPriceCalculator.py

set ANACONDA_PATH=C:\ProgramData\anaconda3
set ANACONDA_PATH_USER=%LOCALAPPDATA%\Continuum\anaconda3

if exist "%ANACONDA_PATH%\python.exe" (
    "%ANACONDA_PATH%\python.exe" FruitPriceCalculator.py
    goto :end
)
if exist "%ANACONDA_PATH_USER%\python.exe" (
    "%ANACONDA_PATH_USER%\python.exe" FruitPriceCalculator.py
    goto :end
)

:end
if errorlevel 1 pause