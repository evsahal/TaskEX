from PySide6.QtWidgets import QFrame, QCheckBox

from core.custom_widgets.FlowLayout import FlowLayout
from gui.widgets.MonsterProfileWidget import MonsterProfileWidget


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
    for i in range(25):
        widget = MonsterProfileWidget(flow_layout=getattr(main_window.widgets, f"monsters_list_flow_layout"))
        # Set the size of the widget to its size hint
        widget.setFixedSize(widget.sizeHint())
        flow_layout.addWidget(widget)


def toggle_frame(main_window):
    # Get monsters_list_frame and export_monsters_btn references
    monsters_list_frame = getattr(main_window.widgets, "monsters_list_frame")
    export_monsters_btn = getattr(main_window.widgets, "export_monsters_btn")

    # Toggle checkbox visibility and handle unchecking if the button is not checked
    is_checked = export_monsters_btn.isChecked()

    for checkbox in monsters_list_frame.findChildren(QCheckBox):
        checkbox.setVisible(is_checked)
        # Uncheck all boxes if the button is unchecked
        if not is_checked:
            checkbox.setChecked(False)

    # Toggle confirm frame
    getattr(main_window.widgets, f"export_monster_confirm_frame").setVisible(export_monsters_btn.isChecked())