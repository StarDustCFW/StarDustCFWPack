@echo off
FOR /F "delims=" %%i in ('dir *.nro/b') do (
if %%i neq StarDust.nro mkdir %%~ni
if %%i neq StarDust.nro move /y %%i %%~ni\)
