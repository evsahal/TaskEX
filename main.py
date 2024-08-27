import sys
from PySide6.QtWidgets import QApplication

from PySide6.QtGui import QIcon

from core.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())