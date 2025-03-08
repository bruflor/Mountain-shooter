import os

from cx_Freeze import Executable, setup

path = './asset'
asset_list = os.listdir(path)
asset_lista_completa = [os.path.join(path, asset).replace('\\', '/') for asset in asset_list]
print(asset_lista_completa)

executables = [Executable("main.py")]
files = {"include_files":asset_lista_completa, "packages":["pygame"]}

setup(
    name="MountainShooter",
    version="1.0.0",
    description="Mountain Shooter arcade game",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables,
)