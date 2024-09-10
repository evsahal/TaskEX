from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QListWidget, QListWidgetItem

class FlowContainer(QListWidget):
    def __init__(self):
        super().__init__()
        # make it look like a normal scroll area
        self.viewport().setBackgroundRole(QPalette.Window)
        # display items from left to right
        self.setFlow(self.LeftToRight)
        # wrap items that don't fit the width of the viewport
        self.setWrapping(True)
        # prevent user repositioning
        self.setMovement(self.Static)
        # always re-layout items when the view is resized
        self.setResizeMode(self.Adjust)
        self.setHorizontalScrollMode(self.ScrollPerPixel)
        self.setVerticalScrollMode(self.ScrollPerPixel)
        self.setSpacing(3)

    def addWidgetItem(self, widget):
        """Generic method to add any widget to the flow layout."""
        item = QListWidgetItem()
        item.setFlags(item.flags() & ~(Qt.ItemIsSelectable | Qt.ItemIsEnabled))
        item.setSizeHint(widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, widget)
