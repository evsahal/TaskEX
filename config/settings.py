import os

# APP TEXTS
TITLE = "TaskEX"
TITLE_DESCRIPTION = "Ultimate Edition"
VERSION = "v2.0.0"
CREDITS = "By: MwoNuZzz"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Project base directory
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, '..', 'db', 'task_ex.db')}"


