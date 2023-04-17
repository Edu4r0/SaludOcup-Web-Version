import shutil
from git import Repo
import shutil
from git import Repo

# Elimina el repositorio existente
shutil.rmtree('SaludOcup-Web-Version')

# Clona una copia actualizada del repositorio desde GitHub
Repo.clone_from('https://github.com/Edu4r0/SaludOcup-Web-Version.git', 'SaludOcup-Web-Version')

