@echo off
setlocal enabledelayedexpansion

echo ========================================
echo SkillSpark GitHub Upload Script
echo ========================================
echo.

REM Check if git is available
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Initialize git repo if not exists
if not exist .git (
    echo Initializing Git repository...
    git init
    git config user.email "user@skillspark.dev"
    git config user.name "SkillSpark Developer"
    echo Git repository initialized.
    echo.
)

REM Add all files
echo Adding files to git...
git add .

REM Commit
echo Committing changes...
git commit -m "Deploy SkillSpark: Daily quests, coins currency, production-ready"

REM Instructions for remote
echo.
echo ========================================
echo NEXT STEPS:
echo ========================================
echo.
echo 1. Go to https://github.com/new
echo 2. Create a new repository named "SkillSpark"
echo 3. DO NOT initialize with README
echo 4. Copy the repository URL (should look like: https://github.com/YOUR_USERNAME/SkillSpark.git)
echo 5. Come back here and paste the URL when prompted
echo.
set /p REPO_URL="Enter your GitHub repository URL: "

if "!REPO_URL!"=="" (
    echo ERROR: No URL provided
    pause
    exit /b 1
)

REM Add remote and push
echo.
echo Adding remote repository...
git remote add origin !REPO_URL!

echo Pushing to GitHub (you may be asked to login)...
git branch -M main
git push -u origin main

echo.
echo ========================================
echo SUCCESS! Your code is now on GitHub
echo ========================================
echo Repository URL: !REPO_URL!
echo.
echo Next: Go to render.com and deploy from this GitHub repo
echo.
pause
