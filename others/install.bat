@echo off
echo Borrando Antigua Version...
rmdir /s /q C:\Temp\SaludOcup
echo Borrando Antiguas Tareas ...   
schtasks /delete /tn "Notificador Mañana" /f
schtasks /delete /tn "Notificador Tarde"  /f
echo Tareas Borradas con Exito.
echo Programando Tareas Nuevas ...
schtasks /create /sc weekly /d "MON,TUE,WED,THU,FRI" /tn "SaludOcup M" /tr "C:\Temp\SaludOcup-Web-Version\main.exe" /st 10:30
schtasks /create /sc weekly /d "MON,TUE,WED,THU,FRI" /tn "SaludOcup T" /tr "C:\Temp\SaludOcup-Web-Version\main.exe" /st 15:30
schtasks /create /sc weekly /d "MON,TUE,WED,THU,FRI" /tn "Update" /tr "C:\Temp\SaludOcup-Web-Version\update.exe" /st 08:00
echo Tareas Programadas con Exito.