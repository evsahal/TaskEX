import sys
import os
from cx_Freeze import setup, Executable

from core.app_settings import Settings

# ADD FILES
files = ['icon.ico','platform-tools/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "TaskEnforcerX",
    version = Settings.VERSION,
    description = Settings.TITLE_DESCRIPTION,
    author = "MwoNuZzz",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)

#venv\Scripts\activate

#python setup.py build > output.txt