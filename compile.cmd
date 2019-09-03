@echo off
cd %userprofile%\Documents\GitHub\switchbru-libnx
title libnx - git pull
git pull
git fetch --all
cd nx
title libnx - make 
make

title libnx - xcopy
del C:\devkitPro\libnx /s/q
pacman -Syu
xcopy /y /h /e .\* C:\devkitPro\libnx\

cd %userprofile%\Documents\GitHub\atmosphere
title Atmosphere - git pull
git pull

title Atmosphere - xcopy mod
xcopy /y /h /e %userprofile%\Documents\GitHub\Atmosphere-ex-mod\* %userprofile%\Documents\GitHub\atmosphere\

title Atmosphere - make dist
make dist
echo completado

cd %userprofile%\Documents\GitHub\atmosphere

git rev-parse --short HEAD > %temp%\tmpFile 
set /p comit= < %temp%\tmpFile 
git symbolic-ref --short HEAD > %temp%\tmpFile
set /p branch= < %temp%\tmpFile 
del %temp%\tmpFile
cd atmosphere-*-%branch%-%comit%-Kronos2308
echo %cd%
title Atmosphere - xcopy to StarDust
xcopy /y /h /e %cd%\* "%~dp0StarDustCFWpack\"

title argon - make
cd %userprofile%\Documents\GitHub\StarDust-Bootmenu
make
title argon - xcopy to StarDust
xcopy /y /h /e %cd%\output\payload.bin "%~dp0StarDustCFWpack\"


cd %~dp0StarDustCFWpack
set /p SDV= < %~dp0StarDustCFWpack\StarDust\StarDustV.txt
echo %cd%
echo StarDust_%SDV%
title StarDust_%SDV% - flags
attrib -a -s -h * /S /D
title StarDust_%SDV% - compress
rar a %~dp0StarDust_%SDV%.rar * -r -m5
title StarDust_%SDV% - ready
%systemroot%\system32\timeout.exe 200
exit
%systemroot%\system32\timeout.exe 200
%~dp0StarDustCFWpack
zip -r -9 StarDust_%SDV%.zip *