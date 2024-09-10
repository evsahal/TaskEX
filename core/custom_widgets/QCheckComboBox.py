import sys
from PySide6.QtCore import Qt, QEvent, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QComboBox, QListView, QStyledItemDelegate, QApplication, QStyle, QStyleOptionViewItem, \
    QStylePainter, QStyleOptionComboBox


class QCheckComboBox(QComboBox):
    """
    A QComboBox allowing multiple item selection.
    """

    class ComboItemDelegate(QStyledItemDelegate):
        """
        Helper styled delegate to draw checkboxes and item text properly, avoiding overlap.
        """

        def paint(self, painter, option, index):
            style = option.widget.style() if option.widget is not None else QApplication.style()

            option = QStyleOptionViewItem(option)
            option.showDecorationSelected = True

            # Get the rectangle for the checkbox
            if index.flags() & Qt.ItemIsUserCheckable:  # Ensure item is checkable
                check_rect = style.subElementRect(QStyle.SE_ItemViewItemCheckIndicator, option, option.widget)
                option.rect.setLeft(check_rect.right() + 5)  # Adjust the text rectangle
                # Draw the checkbox
                state = index.data(Qt.CheckStateRole)
                if state == Qt.Checked:
                    option.state |= QStyle.State_On
                else:
                    option.state |= QStyle.State_Off

                style.drawPrimitive(QStyle.PE_IndicatorCheckBox, option, painter)

            # Draw the text
            super(QCheckComboBox.ComboItemDelegate, self).paint(painter, option, index)

    def __init__(self, parent=None, placeholderText="", separator=", ", **kwargs):
        super(QCheckComboBox, self).__init__(parent, **kwargs)
        self.setFocusPolicy(Qt.StrongFocus)
        self.__popupIsShown = False
        self.__blockMouseReleaseTimer = QTimer(self, singleShot=True)
        self.__initialMousePos = None
        self.__separator = separator
        self.__placeholderText = placeholderText
        self.setView(QListView())  # Use QListView for the combo box drop-down
        self.__updateItemDelegate()
        self.update_checked_items()  # Ensure the placeholder text is initially set

    def showPopup(self):
        """Reimplemented."""
        super(QCheckComboBox, self).showPopup()
        view = self.view()
        view.installEventFilter(self)
        view.viewport().installEventFilter(self)
        self.__popupIsShown = True

    def hidePopup(self):
        """Reimplemented."""
        self.view().removeEventFilter(self)
        self.view().viewport().removeEventFilter(self)
        self.__popupIsShown = False
        self.__initialMousePos = None
        super(QCheckComboBox, self).hidePopup()
        self.view().clearFocus()

    def eventFilter(self, obj, event):
        """Reimplemented."""
        if self.__popupIsShown and event.type() == QEvent.MouseButtonRelease:
            model = self.model()
            index = self.view().currentIndex()
            state = model.data(index, Qt.CheckStateRole)
            model.setData(index, Qt.Checked if state == Qt.Unchecked else Qt.Unchecked, Qt.CheckStateRole)
            self.view().update(index)
            self.update_checked_items()  # Update the combo box text when the state changes
            return True
        return super(QCheckComboBox, self).eventFilter(obj, event)

    def update_checked_items(self):
        """Update the combo box display with selected items or placeholder text."""
        checked = self.checkedIndices()
        if checked:
            items = [self.itemText(i) for i in checked]
            self.setCurrentText(self.__separator.join(items))
        else:
            self.setCurrentText(self.__placeholderText)

    def paintEvent(self, event):
        """Reimplemented."""
        painter = QStylePainter(self)
        option = QStyleOptionComboBox()
        self.initStyleOption(option)
        painter.drawComplexControl(QStyle.CC_ComboBox, option)
        checked = self.checkedIndices()
        if checked:
            items = [self.itemText(i) for i in checked]
            option.currentText = self.__separator.join(items)
        else:
            option.currentText = self.__placeholderText
        option.currentIcon = QIcon()
        painter.drawControl(QStyle.CE_ComboBoxLabel, option)

    def itemCheckState(self, index):
        """
        Return the check state for item at `index`.
        """
        state = self.itemData(index, role=Qt.CheckStateRole)
        if isinstance(state, (int, Qt.CheckState)):
            return Qt.CheckState(state)
        return Qt.Unchecked

    def setItemCheckState(self, index, state):
        """
        Set the check state for item at `index` to `state`.
        """
        self.setItemData(index, state, Qt.CheckStateRole)

    def checkedIndices(self):
        """
        Return a list of indices of all checked items.
        """
        return [i for i in range(self.count()) if self.itemCheckState(i) == Qt.Checked]

    def setPlaceholderText(self, text):
        """
        Set the placeholder text.
        """
        if self.__placeholderText != text:
            self.__placeholderText = text
            self.update_checked_items()

    def placeholderText(self):
        """
        Return the placeholder text.
        """
        return self.__placeholderText

    def wheelEvent(self, event):
        """Reimplemented."""
        event.ignore()

    def __updateItemDelegate(self):
        self.setItemDelegate(QCheckComboBox.ComboItemDelegate(self))