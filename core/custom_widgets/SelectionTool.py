from PySide6.QtWidgets import (
    QGraphicsView, QGraphicsScene, QGraphicsPixmapItem,
    QRubberBand, QVBoxLayout
)
from PySide6.QtCore import Qt, QRect, QSize, QPoint, Signal, QTimer
from PySide6.QtGui import QPixmap

class SelectionTool(QGraphicsView):
    area_selected = Signal(int, int, int, int)  # Signal to emit the selected area coordinates

    def __init__(self, q_image, full_preview=False, parent=None):
        super().__init__(parent)

        self.read_only = False  # Track read-only state
        self.selection_active = False  # Track if selection is active
        self.q_image = q_image  # Store the image
        self.is_panning = False  # Track panning state
        self.full_preview = full_preview  # Full preview mode flag
        self.origin = QPoint()  # Origin for selection
        self.pan_start = QPoint()  # Start point for panning

        # Set up the scene and pixmap
        self.scene = QGraphicsScene(self)
        self.pixmap_item = QGraphicsPixmapItem(QPixmap.fromImage(q_image))
        self.scene.addItem(self.pixmap_item)
        self.setScene(self.scene)

        # Configure scroll bars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Configure rubber band for selection
        self.rubber_band = QRubberBand(QRubberBand.Rectangle, self)

        # Adjust the view once after the widget is shown
        QTimer.singleShot(0, self.adjust_view)

    def adjust_view(self):
        """Adjust the view based on the mode and parent widget size."""
        parent = self.parentWidget()

        if self.full_preview and self.scene is not None:
            self.fitInView(self.pixmap_item, Qt.KeepAspectRatio)  # Adjust to fit in view
        elif parent is not None:
            parent_size = parent.size()
            self.resize(parent_size)  # Resize to match parent size

    def resizeEvent(self, event):
        """Handle resizing to keep the view consistent."""
        self.adjust_view()  # Adjust the view after resize
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.read_only:
            if event.modifiers() & Qt.ShiftModifier:
                self.is_panning = True
                self.pan_start = event.pos()
            else:
                self.origin = event.pos()
                self.rubber_band.setGeometry(QRect(self.origin, QSize()))
                self.rubber_band.show()
                self.selection_active = True

    def mouseMoveEvent(self, event):
        if self.is_panning:
            delta = self.pan_start - event.pos()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + delta.y())
            self.pan_start = event.pos()
        elif self.selection_active:
            self.rubber_band.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.is_panning:
                self.is_panning = False
            elif self.selection_active:
                selected_rect = self.rubber_band.geometry()
                x = selected_rect.x() + self.horizontalScrollBar().value()
                y = selected_rect.y() + self.verticalScrollBar().value()
                width = selected_rect.width()
                height = selected_rect.height()

                print(f"[DEBUG] Selection finalized: x={x}, y={y}, width={width}, height={height}")
                self.area_selected.emit(x, y, width, height)
                self.selection_active = False

    def set_read_only(self, value: bool):
        """Enable or disable read-only mode."""
        self.read_only = value

    def is_selection_made(self):
        """Check if a selection has been made."""
        return self.rubber_band.isVisible()

    def clear_selection(self):
        """Clear the current selection."""
        self.rubber_band.hide()
        self.selection_active = False
