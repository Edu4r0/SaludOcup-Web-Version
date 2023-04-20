import os
import subprocess
import urllib.request

# Descargar los archivos en la carpeta temporal
urllib.request.urlretrieve(
    'https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/others/install.bat', 'C:\\Temp\\install.bat')
#urllib.request.urlretrieve(
#    'https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/others/install.vbs', 'C:\\Temp\\install.vbs')

# Obtener la ruta absoluta de los archivos
bat_path = os.path.abspath('C:\\Temp\\install.bat')
vbs_path = os.path.abspath('C:\\Temp\\install.vbs')

# Ejecutar el archivo .bat usando subprocess.run()
subprocess.call(['cmd.exe', 'C:\Temp\install.bat'])

# ruta_vbs = r"C:\Temp\install.vbs"

# Ejecuta el archivo .vbs con la función subprocess.call()
# subprocess.call(['cscript.exe', ruta_vbs])
