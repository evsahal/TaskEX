from core.custom_widgets.FlowLayout import FlowLayout
from gui.widgets.BlackMarketProfileWidget import BlackMarketProfileWidget
from gui.widgets.MonsterProfileWidget import MonsterProfileWidget


def init_bm_blackmarket_ui(main_window):

    # Set up the Layout for black market items
    blackmarket_list_frame = main_window.widgets.blackmarket_list_frame

    # Use the existing blackmarket_list_frame as the container
    flow_layout = FlowLayout(blackmarket_list_frame)
    flow_layout.setObjectName("blackmarket_list_flow_layout")
    setattr(main_window.widgets, flow_layout.objectName(), flow_layout)

    # Set the flow layout to the container frame (blackmarket_list_frame)
    blackmarket_list_frame.setLayout(flow_layout)



    # Pass the data to add the widgets
    for i in range(20):
        # print(boss.monster_logic_id)
        add_blackmarket_item_to_frame(main_window)

def add_blackmarket_item_to_frame(main_window):
    flow_layout = main_window.widgets.blackmarket_list_flow_layout

    widget = BlackMarketProfileWidget(flow_layout=flow_layout)
    setattr(main_window.widgets, widget.objectName(), widget)

    # Set the size of the widget to its size hint
    # widget.setFixedSize(widget.sizeHint())
    flow_layout.addWidget(widget)