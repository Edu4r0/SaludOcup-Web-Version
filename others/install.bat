@echo off
echo Borrando Antigua Version...
rmdir /s /q C:\Temp\SaludOcup
echo Carpeta borrada exitosamente.
echo Descargando Python ...
curl -LOk https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe
echo Instalando Python ...
start /wait python-3.11.3-amd64.exe /verysilent
echo Python instalado exitosamente.
echo Version de Python
python --version 
echo Instalando Dependencias ...
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip install PyQtWebEngine
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip install PyQt5
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip install GitPython
echo Dependencias Instalas exitosamente.
echo Descargando Git...
curl -LOk https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe
echo Instalando Git...
start /wait Git-2.40.0-64-bit.exe /verysilent
echo Git instalado exitosamente.
echo Descargando nueva version ...
mkdir "SaludOcup-Web-Version"
curl -LOk https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/others/update.exe -o C:\Temp\update.exe
echo instalado nueva version ...
start update.exe /verysilent
echo Borrando residuos ...
del /F /Q Git-2.40.0-64-bit.exe 
del /F /Q python-3.11.3-amd64.exe 
echo Borrando Antiguas Tareas ...   
schtasks /delete /tn "Notificador Mañana" /f
schtasks /delete /tn "Notificador Tarde"  /f
echo Tareas Borradas con Exito.
echo Programando Tareas Nuevas ...
schtasks /create /sc weekly /d "MON,TUE,WED,THU,FRI" /tn "SaludOcup M" /tr "C:\Temp\SaludOcup-Web-Version\__pycache__.vbs" /st 10:30
schtasks /create /sc weekly /d "MON,TUE,WED,THU,FRI" /tn "SaludOcup T" /tr "C:\Temp\SaludOcup-Web-Version\__pycache__.vbs" /st 15:30
schtasks /create /sc weekly /d "MON,TUE,WED,THU,FRI" /tn "Update" /tr "C:\Temp\update.exe" /st 08:00
echo Tareas Programadas con Exito.
echo THANKS SALUDOCUP VER 2.0 IS READY  
del /F /Q install.bat 
