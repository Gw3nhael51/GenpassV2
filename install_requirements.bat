@echo off
title GenpassV2 - Creation de l'environnement virtuel

:: ========================================
:: GenpassV2 - Configuration initiale
:: ========================================
echo ========================================
echo GenpassV2 - Configuration initiale
echo ========================================
echo.

REM ========================================
REM Verification de Python
REM ========================================
python --version >nul 2>&1
if errorlevel 1 (
    echo Python n'est pas installe ou n'est pas dans le PATH
    echo Telechargez Python depuis : https://python.org
    pause
    exit /b 1
)
echo Python detecte

REM ========================================
REM Creation de l'environnement virtuel
REM ========================================
if not exist ".venv" (
    echo Creation de l'environnement virtuel...
    python -m venv .venv
    if errorlevel 1 (
        echo Erreur lors de la creation de l'environnement virtuel
        pause
        exit /b 1
    )
    echo Environnement virtuel cree
) else (
    echo Environnement virtuel deja existant
)

REM ========================================
REM Activation du venv
REM ========================================
echo Activation de l'environnement virtuel...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo Erreur lors de l'activation de l'environnement virtuel
    pause
    exit /b 1
)
echo Environnement virtuel active

REM ========================================
REM Instructions manuelles
REM ========================================
echo.
echo ========================================
echo Environnement virtuel pret !
echo ========================================
echo.
echo Maintenant, installez les dependances :
echo.
echo     pip install -r requirements.txt
echo.
echo Puis lancez l'application :
echo.
echo     python generativepasswV2.py
echo.
echo Ou suivez les instructions dans le README.md
echo.
pause