@echo off
cd StarDustCFWpack
title %cd% 

:fix


xcopy.exe /y payload.bin atmosphere\reboot_payload.bin
xcopy.exe  /y payload.bin bootloader\payloads\payload.bin

xcopy.exe /y StarDust\payloads\Atmosphere.bin bootloader\payloads\Atmosphere.bin

xcopy.exe /y StarDust\payloads\ReiNX.bin bootloader\payloads\ReiNX.bin

xcopy.exe /y StarDust\payloads\SXOS.bin bootloader\payloads\SXOS.bin
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