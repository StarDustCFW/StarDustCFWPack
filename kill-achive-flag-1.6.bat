@echo off
set ver=1.6
rem by Kronos2308
rename %0 kill-achive-flag-%ver%.bat
title yo busco la sd solita ponme donde quieras ver %ver%
color 0a
set azucar=false
set l=d
set con=0
echo ----------->%temp%\loger
echo LOG>>%temp%\loger
echo ----------->>%temp%\loger

:loop
title yo busco la sd solita ponme donde quieras ver %ver% %l%:
if exist %l%:\Nintendo (
echo Encontre la sd en %l%:\ >>%temp%\loger
echo Encontre la sd en %l%:\
echo Buscando errores en %l%:
CHKDSK /f %l%:
echo -------------------------
echo Arreglando flag de archivo en %l%:
echo Arreglando flag de archivo en %l%:>>%temp%\loger
attrib -s -h -a %l%:\* /S /D>>%temp%\loger
attrib +a %l%:\emutendo\Contents\registered\* /S /D
attrib +a %l%:\Nintendo\Contents\registered\* /S /D>>%temp%\loger
set azucar=true
)
if %azucar% equ true goto:26
set l=c
set /a con+=1
goto:%con%

:1

vol d:
if %errorlevel% == 0 set l=d
goto:loop
:2
vol e:
if %errorlevel% == 0 set l=e
goto:loop
:3
vol f:
if %errorlevel% == 0 set l=f
goto:loop
:4
vol g:
if %errorlevel% == 0 set l=g
goto:loop
:5
vol h:
if %errorlevel% == 0 set l=h
goto:loop
:6
vol i:
if %errorlevel% == 0 set l=i
goto:loop
:7
vol j:
if %errorlevel% == 0 set l=j
goto:loop
:8
vol k:
if %errorlevel% == 0 set l=k
goto:loop
:9
vol l:
if %errorlevel% == 0 set l=l
goto:loop
:10
vol m:
if %errorlevel% == 0 set l=m
goto:loop
:11
vol n:
if %errorlevel% == 0 set l=n
goto:loop
:12
vol o:
if %errorlevel% == 0 set l=o
goto:loop
:13
vol p:
if %errorlevel% == 0 set l=p
goto:loop
:14
vol q:
if %errorlevel% == 0 set l=q
goto:loop
:15
vol r:
if %errorlevel% == 0 set l=r
goto:loop
:16
vol s:
if %errorlevel% == 0 set l=s
goto:loop
:17
vol t:
if %errorlevel% == 0 set l=t
goto:loop
:18
vol u:
if %errorlevel% == 0 set l=u
goto:loop
:19
vol v:
if %errorlevel% == 0 set l=v
goto:loop
:20
vol w:
if %errorlevel% == 0 set l=w
goto:loop
:21
vol x:
if %errorlevel% == 0 set l=x
goto:loop
:22

vol y:

if %errorlevel% == 0 set l=y
goto:loop
:23
vol z: 
if %errorlevel% == 0 set l=z
goto:loop
:24

@vol a:
if %errorlevel% == 0 set l=a

goto:loop
:25
@vol b:
if %errorlevel% == 0 set l=b
goto:loop
:26
set l=d
set con=0
type %temp%\loger
echo -------
color 0a
if %azucar% == false (
echo NO ENCONTRE LA SD, Donde esta?
color 04
)

echo termine todo

%windir%\system32\timeout.exe 150
exit




