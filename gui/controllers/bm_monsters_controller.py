import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QCheckBox, QDialog, QWidget, QMessageBox

from core.custom_widgets.FlowLayout import FlowLayout
from core.services.bm_monsters_service import export_selected_bosses, \
    get_all_boss_monster_data_for_bm
from db.db_setup import get_session
from db.models import BossMonster
from gui.widgets.MonsterEditDialog import MonsterEditDialog
from gui.widgets.MonsterProfileWidget import MonsterProfileWidget
from gui.widgets.MonsterUploadDialog import MonsterUploadDialog
from utils.constants_util import logic_colors


def init_bm_monster_ui(main_window):
    # Connect the upload button to open the dialog
    main_window.widgets.upload_monsters_btn.clicked.connect(lambda :open_upload_dialog(main_window))
    # Connect the export button to toggle the confirmation frame
    main_window.widgets.export_monsters_btn.toggled.connect(lambda :toggle_frame(main_window))
    # Cancel button signal connect
    main_window.widgets.cancel_export_btn.clicked.connect(lambda :main_window.widgets.export_monsters_btn.setChecked(False))
    # Export Confirm button connect
    main_window.widgets.confirm_export_btn.clicked.connect(lambda :confirm_export_monsters(main_window))


    # Hide the confirmation frame
    main_window.widgets.export_monster_confirm_frame.setVisible(False)

    # Set up the Layout for monsters
    monsters_list_frame = main_window.widgets.monsters_list_frame

    # Use the existing monsters_list_frame as the container
    flow_layout = FlowLayout(monsters_list_frame)
    flow_layout.setObjectName("monsters_list_flow_layout")
    setattr(main_window.widgets, flow_layout.objectName(), flow_layout)

    # Set the flow layout to the container frame (monsters_list_frame)
    monsters_list_frame.setLayout(flow_layout)

    # Get all the bosses
    boss_monsters = get_all_boss_monster_data_for_bm()

    # Pass the data to add the widgets
    for boss in boss_monsters:
        # print(boss.monster_logic_id)
        add_monster_to_frame(main_window,boss)


def add_monster_to_frame(main_window,boss):
    flow_layout = main_window.widgets.monsters_list_flow_layout

    widget = MonsterProfileWidget(flow_layout=flow_layout, data=boss)
    setattr(main_window.widgets, widget.objectName(), widget)

    # Setup Configure/Edit Monster
    widget.ui.configure_monster_btn.clicked.connect(lambda :configure_monster(main_window,widget.ui.checkBox.property("boss_id")))

    # Set the size of the widget to its size hint
    widget.setFixedSize(widget.sizeHint())
    flow_layout.addWidget(widget)

def configure_monster(main_window,boss_id):
    # Create an instance of the MonsterEditDialog and show it
    dialog = MonsterEditDialog(monster_id=boss_id, parent=main_window)
    # Connect the signal to the update function
    dialog.monster_updated.connect(lambda updated_id: update_monster_profile_ui(main_window, updated_id))
    # Open the dialog and wait for a response (blocking call)
    if dialog.exec() == QDialog.Accepted:
        # Handle successful save
        # print("Monster configuration saved!")
        pass



def update_monster_profile_ui(main_window, boss_id):
    """Update the monster profile UI for the given monster ID."""
    # Access the monster profile widget by ID
    monster_profile_widget = main_window.findChild(QWidget, f"monster_profile_{boss_id}")

    if monster_profile_widget:
        with get_session() as session:
            # Fetch updated monster data (e.g., from the database or dialog)
            updated_monster = session.query(BossMonster).filter(BossMonster.id == boss_id).one()

            # Update the UI with the new data
            preview_path = os.path.join('assets', 'preview')

            # Setup Monster Preview
            monster_profile_widget.ui.monster_name_label.setText(updated_monster.preview_name)
            monster_preview = os.path.join(str(preview_path), updated_monster.monster_image.preview_image)
            if not os.path.isfile(monster_preview):
                monster_preview = os.path.join(str(preview_path), "default_preview.png")
            pixmap = QPixmap(monster_preview)
            pixmap = pixmap.scaledToHeight(92)
            monster_profile_widget.ui.monster_icon_label.setPixmap(pixmap)

            # Update the frame
            # Get the corresponding color for the logic ID
            logic_color = logic_colors.get(updated_monster.monster_logic_id, '#000000')  # Default to black if not found

            # Setup the Monster Bottom Frame Color
            monster_profile_widget.ui.bottom_color_frame.setStyleSheet(f"""
                        background-color: rgb(29, 33, 38);
                        border-bottom: 2px solid {logic_color};
                    """)

def open_upload_dialog(main_window):
    # Create an instance of the dialog class
    dialog = MonsterUploadDialog(main_window)
    dialog.exec()

def toggle_frame(main_window):
    # Get monsters_list_frame and export_monsters_btn references
    monsters_list_frame = main_window.widgets.monsters_list_frame
    export_monsters_btn = main_window.widgets.export_monsters_btn

    # Toggle checkbox visibility and handle unchecking if the button is not checked
    is_checked = export_monsters_btn.isChecked()

    # Update the checkbox visibility
    for checkbox in monsters_list_frame.findChildren(QCheckBox):
        checkbox.setVisible(is_checked)
        # Uncheck all boxes if the button is unchecked
        if not is_checked:
            # print(f"Checkbox boss id: {checkbox.property("boss_id")}")
            checkbox.setChecked(False)

    # Toggle confirm frame
    main_window.widgets.export_monster_confirm_frame.setVisible(export_monsters_btn.isChecked())


def confirm_export_monsters(main_window):
    checked_monsters = []
    monsters_list_frame = main_window.widgets.monsters_list_frame

    # Loop through checkboxes to get selected bosses
    for checkbox in monsters_list_frame.findChildren(QCheckBox):
        if checkbox.isChecked():
            boss_id = checkbox.property("boss_id")
            checked_monsters.append(boss_id)

    if len(checked_monsters) == 0:
        QMessageBox.warning(main_window, "No Selection", "Please select at least one monster to export.")
        return False

    # Export selected monsters
    export_selected_bosses(checked_monsters)

    # Toggle confirm frame
    main_window.widgets.export_monsters_btn.setChecked(False)
