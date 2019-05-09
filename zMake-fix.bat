@echo off
cd StarDustCFWpack
title %cd% 

:fix

attrib -a -s -h * /S /D
pause
exit
FOR /F "delims=" %%i in ('dir * /b') do (if /i %%i neq Nintendo attrib -a %%i/S /D)



:new
set oldver= %ver%
echo cual sera 
set /p ver=
cd %phat%

xcopy /e /h /y %oldver%\* %ver%\*
pause
exit