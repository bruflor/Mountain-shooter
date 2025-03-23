import os

from cx_Freeze import Executable, setup

build_exe_options = {
    "packages": ["pygame"],  
    "include_files": ["asset/"],
}

executables = [Executable("main.py")]

setup(
    name="MountainShooter",
    version="1.0.0",
    description="Mountain Shooter arcade game",
    options={"build_exe": build_exe_options},
    executables=executables,
)