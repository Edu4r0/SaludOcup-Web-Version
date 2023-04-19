import wget
import subprocess

wget.download('https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/others/install.bat','C:\Temp\install.bat')
wget.download('https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/others/install.vbs','C:\Temp\install.vbs')

subprocess.call(['cmd.exe', '/c', 'C:/Temp/install.bat'])
# Especifica la ruta completa del archivo .vbs
#ruta_vbs = r"C:\Temp\install.vbs"

# Ejecuta el archivo .vbs con la función subprocess.call()
#subprocess.call(['cscript.exe', ruta_vbs])