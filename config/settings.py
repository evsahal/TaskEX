import os
from pathlib import Path

# APP TEXTS
TITLE = "TaskEX"
TITLE_DESCRIPTION = "Ultimate Edition"
VERSION = "v2.0.0"
CREDITS = "By: MwoNuZzz"

# Project base directory
BASE_DIR = PROJECT_ROOT = Path(__file__).resolve().parent.parent
# DB URL
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'db', 'task_ex.db')}"


