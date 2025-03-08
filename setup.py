import os

from cx_Freeze import Executable, setup


executables = [Executable("main.py")]

setup(
    name="MountainShooter",
    version="1.0.0",
    description="Mountain Shooter arcade game",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables,
)