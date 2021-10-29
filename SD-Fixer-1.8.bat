@echo off
set ver=1.8
rem by Kronos2308
rename %0 SD-Fixer-%ver%.bat
title Yo busco la sd solita ponme donde quieras ver %ver%
set azucar=false
echo ----------->%temp%\loger
echo LOG>>%temp%\loger
echo ----------->>%temp%\loger

for /D %%i in (D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
set l=%%i
rem if exist %%i:\Nintendo goto:Work


	if exist %%i:\Nintendo (
		echo Encontre la sd en %%i:\ >>%temp%\loger
		echo Encontre la sd en %%i:\
		echo Buscando errores en %%i:
		CHKDSK /f %%i:
		echo -------------------------
		echo Arreglando flag de archivo en %%i:
		echo Arreglando flag de archivo en %%i:>>%temp%\loger
		attrib -s -h -a %%i:\* /S /D>>%temp%\loger
		if exist %%i:\emutendo attrib +a %%i:\emutendo\Contents\registered\* /S /D>nul
		attrib +a %%i:\Nintendo\Contents\registered\* /S /D>>%temp%\loger
		set azucar=true
	)
)

:Work
set l=d
set con=0
type %temp%\loger
echo -------
if %azucar% == false (
echo NO ENCONTRE LA SD, Donde esta?
fsutil fsinfo drives
color 04
%windir%\system32\timeout.exe 150
exit
)

echo termine todo
color 0a
%windir%\system32\timeout.exe 150
exit




