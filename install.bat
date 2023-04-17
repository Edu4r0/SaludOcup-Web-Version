pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip install PyQtWebEngine
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip install PyQt5
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip install GitPython
python --version
@echo off
echo Descargando Git...
curl -LOk https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe
echo Instalando Git...
start /wait Git-2.31.1-64-bit.exe /SILENT
echo Git instalado exitosamente.
pause