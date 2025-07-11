import sys
import os
from cx_Freeze import setup, Executable

from config.settings import VERSION, TITLE_DESCRIPTION

# === Add project folders and files ===
include_files = [
    'icon.ico',
    'platform-tools/',
    'Tesseract-OCR/',
    'assets/',
    'db/task_ex.db',
    'LICENSE',
]

# === Dependencies that might be missed automatically ===
packages = [
    'sqlalchemy',
    'sqlalchemy.dialects.sqlite',
    'PySide6',
    'PySide6.QtWidgets',
    'PySide6.QtGui',
    'PySide6.QtCore',
]

# === Main executable ===
base = "Win32GUI"

executables = [
    Executable(
        script="main.py",
        base=base,
        icon="icon.ico"
    )
]

# === Final setup ===
setup(
    name="TaskEnforcerX",
    version=VERSION,
    description=TITLE_DESCRIPTION,
    author="MwoNuZzz",
    options={
        'build_exe': {
            'include_files': include_files,
            'packages': packages,
            'excludes': ['tkinter'],  # Optional
            'optimize': 1,
        }
    },
    executables=executables
)

# python setup.py build > build_log.txt 2>&1