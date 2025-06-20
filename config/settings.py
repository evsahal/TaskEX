import os
import sys
from pathlib import Path

# APP TEXTS
TITLE = "TaskEX"
TITLE_DESCRIPTION = "Ultimate Edition"
VERSION = "v0.0.0"
CREDITS = "By: MwoNuZzz"

# Project base directory
# BASE_DIR = Path(__file__).resolve().parent.parent

# DB URL
DATABASE_URL = f"sqlite:///{os.path.join(Path(__file__).resolve().parent.parent, 'db', 'task_ex.db')}"


