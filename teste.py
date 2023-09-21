#Caminho : C:\Users\campos\Documents\GitHub\Hub-Gerenciamento\Hub-Gerenciamento>
#No prompt, digite python teste.py build
from cx_Freeze import setup, Executable

base = None    

executables = [Executable("aula5.py", base=base)]

packages = ["time", "tqdm","datetime","qrcode", "random"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Hub",
    options = options,
    version = "1.2",
    description = 'Hub',
    executables = executables
)