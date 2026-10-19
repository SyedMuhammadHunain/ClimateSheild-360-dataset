@echo off
setlocal
if "%1"=="" goto data
if "%1"=="data" goto data
if "%1"=="test" goto test
if "%1"=="inventory" goto inventory
echo Usage: make.bat [data^|test^|inventory]
exit /b 1

:data
python -m climateshield make-data
exit /b %ERRORLEVEL%

:test
python -m pytest tests -q
exit /b %ERRORLEVEL%

:inventory
python -m climateshield inventory
exit /b %ERRORLEVEL%
