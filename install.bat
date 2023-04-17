@echo off
echo Borrando Antigua Version...
rmdir /s /q C:\Temp\SaludOcup
echo Carpeta borrada exitosamente.
echo Descargando Python ...
curl -LOk https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe
echo Instalando Python ...
start /wait python-3.11.3-amd64.exe 
echo Python instalado exitosamente.
echo Instalando Dependencias ...
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip install PyQtWebEngine
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip install PyQt5
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip install GitPython
echo Dependencias Instalas exitosamente.
echo Version de Python
python --version
echo Descargando Git...
curl -LOk https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe
echo Instalando Git...
start /wait Git-2.40.0-64-bit.exe 
echo Git instalado exitosamente.
echo Descargando nueva version ...
curl -LOk https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/update.exe -o C:\Temp\update.exe
echo instalado nueva version ...
start /wait C:\Temp\update.exe /SILENT
echo Borrando residuos ..
del /F /Q Git-2.40.0-64-bit.exe 
del /F /Q python-3.11.3-amd64.exe 
echo THANKS SALUDOCUP VER 2.0 IS READY  
pause
