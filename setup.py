import sys
import os
from cx_Freeze import setup, Executable

from config.settings import VERSION, TITLE_DESCRIPTION

# ADD FILES
files = ['icon.ico','platform-tools/', 'Tesseract-OCR/', 'assets/', 'db/task_ex.db']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)




# SETUP CX FREEZE
setup(
    name = "TaskEnforcerX",
    version = VERSION,
    description = TITLE_DESCRIPTION,
    author = "MwoNuZzz",
    options = {'build_exe' : {'include_files' : files , 'packages': ['sqlalchemy.dialects.sqlite'],}},
    executables = [target]
    
)

#venv\Scripts\activate

#python setup.py build > output.txt