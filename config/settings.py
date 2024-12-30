import os
import sys
from pathlib import Path

# APP TEXTS
TITLE = "TaskEX"
TITLE_DESCRIPTION = "Ultimate Edition"
VERSION = "v0.0.0"
CREDITS = "By: MwoNuZzz"
# Private variable (not directly accessible)
__EXPIRE = "2025-06-30"  # YYYY-MM-DD format

# Public getter to access the expiry date
def get_expire():
    return __EXPIRE

# Project base directory
# BASE_DIR = Path(__file__).resolve().parent.parent

# DB URL
DATABASE_URL = f"sqlite:///{os.path.join(Path(__file__).resolve().parent.parent, 'db', 'task_ex.db')}"


