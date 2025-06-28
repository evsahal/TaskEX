import os
import shutil
from PySide6.QtWidgets import QMessageBox, QPushButton
from db.db_setup import get_session
from db.models import BlackMarket, BlackMarketItem
from core.custom_widgets.FlowLayout import FlowLayout
from gui.widgets.BlackMarketProfileWidget import BlackMarketProfileWidget

ASSETS_PATH = os.path.join("assets", "540p", "blackmarket")


def init_bm_blackmarket_ui(main_window):
    """Initialize the UI with existing black market items."""
    blackmarket_list_frame = main_window.widgets.blackmarket_list_frame
    flow_layout = FlowLayout(blackmarket_list_frame)
    flow_layout.setObjectName("blackmarket_list_flow_layout")
    setattr(main_window.widgets, flow_layout.objectName(), flow_layout)
    blackmarket_list_frame.setLayout(flow_layout)

    with get_session() as session:
        items = session.query(BlackMarket).all()
        for item in items:
            add_blackmarket_item_to_frame(main_window, item)

    # Add one empty profile widget by default
    add_blackmarket_item_to_frame(main_window)


def add_blackmarket_item_to_frame(main_window, data=None):
    """Add a new BlackMarketProfileWidget to the flow layout."""
    flow_layout = main_window.widgets.blackmarket_list_flow_layout
    widget = BlackMarketProfileWidget(flow_layout=flow_layout, data=data)
    setattr(main_window.widgets, widget.objectName(), widget)
    flow_layout.addWidget(widget)


