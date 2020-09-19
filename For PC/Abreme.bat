@echo off
title Descargando utilidades
mode con:lines=4 cols=52
echo Obteninedo lista
wget https://myrincon.duckdns.org/net/PC.php -O PC.txt
for /f "delims= " %%i in (PC.txt) do (
start /MIN wget %%i
)

cls
echo Descargando en segundo plano

:1
for /f "delims= " %%i in ('tasklist /fi "imagename eq wget.exe"') do (set e=%%i)
if /i "%e%" neq "wget.exe" goto:2
%windir%\system32\timeout 01>nul
goto:1

:2
echo.
echo Todo Descargado
echo.
del PC.txt
rem del /a wget.exe
rem del /a vcruntime140.dll
rem del /a %0
pause
