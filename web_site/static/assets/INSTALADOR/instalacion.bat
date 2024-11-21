@echo off
:inicio
echo.
echo [1] Instalar SOLO mods
echo [2] Instalar SOLO Forge
echo [3] Instalar forge y mods
echo.
set /p accion=...

if %accion% == 1 goto mods
if %accion% == 2 goto forge
if %accion% == 3 goto ambos

:forge
java -jar forge-1.20.1-47.3.11-installer.jar
goto salir

:mods
xcopy mods C:\Users\%username%\AppData\Roaming\.minecraft\mods /D
goto salir

:ambos
java -jar forge-1.20.1-47.3.11-installer.jar
xcopy mods C:\Users\%username%\AppData\Roaming\.minecraft\mods /D
goto salir

:salir
pause
exit