from PySide6.QtWidgets import QFrame

from core.custom_widgets.FlowLayout import FlowLayout


def init_bm_monster_ui(main_window):
    # Connect the export button to toggle the confirmation frame
    getattr(main_window.widgets, f"export_monsters_btn").toggled.connect(lambda :toggle_frame(main_window))
    # Hide the confirmation frame
    getattr(main_window.widgets, f"export_monster_confirm_frame").setVisible(False)

    # Set up the Layout for monsters
    monsters_list_frame = getattr(main_window.widgets, "monsters_list_frame")

    # Use the existing monsters_list_frame as the container
    flow_layout = FlowLayout(monsters_list_frame)
    flow_layout.setObjectName("monsters_list_flow_layout")
    setattr(main_window.widgets, flow_layout.objectName(), flow_layout)

    # Set the flow layout to the container frame (monsters_list_frame)
    monsters_list_frame.setLayout(flow_layout)

    # # Create and add multiple frames in a loop
    for i in range(40):  # Adjust the number of frames as needed
        frame = QFrame()
        frame.setFixedSize(200, 200)  # Set the size (width, height)
        frame.setStyleSheet(f"background-color: rgb({i * 5}, 0, 0);")
        flow_layout.addWidget(frame)


def toggle_frame(main_window):
    getattr(main_window.widgets, f"export_monster_confirm_frame").setVisible(getattr(main_window.widgets, f"export_monsters_btn").isChecked())