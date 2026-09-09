@echo off
setlocal enabledelayedexpansion
title 1-Click Push to GitHub - ICAR PG Rank 1 App

echo ========================================================
echo        1-CLICK PUSH TO GITHUB (ICAR PG RANK 1)
echo ========================================================
echo.

cd /d "%~dp0"

where node >nul 2>nul
if %errorlevel% equ 0 (
    node scripts\push-to-github.js %*
    goto END
)

echo [1/3] Staging all files...
git add -A

git diff-index --quiet HEAD --
if %errorlevel% neq 0 (
    for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value 2^>nul') do set dt=%%I
    if "!dt!"=="" (
        set "msg=feat: update project (%date% %time%)"
    ) else (
        set "msg=feat: update project (!dt:~0,4!-!dt:~4,2!-!dt:~6,2! !dt:~8,2!:!dt:~10,2!)"
    )
    echo [2/3] Committing changes: "!msg!"...
    git commit -m "!msg!"
) else (
    echo [2/3] No local changes to commit.
)

echo.
echo [3/3] Pushing to GitHub (origin main)...
git push origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo   SUCCESS! All changes pushed to GitHub successfully!
    echo   Repository: https://github.com/fazalzama77-sys/ICAR-PG-RANK-1-APPLICATION
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo   ERROR: Push failed! Check your connection or auth.
    echo ========================================================
)

:END
echo.
echo Press any key to exit...
pause >nul
