from PySide6.QtWidgets import QFrame, QCheckBox, QDialog
from sqlalchemy import asc

from core.custom_widgets.FlowLayout import FlowLayout
from db.db_setup import get_session
from db.models import BossMonster, MonsterImage, MonsterCategory, MonsterLogic
from gui.widgets.MonsterEditDialog import MonsterEditDialog
from gui.widgets.MonsterProfileWidget import MonsterProfileWidget


def init_bm_monster_ui(main_window):
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
    session = get_session()

    # Query all records from the generals table
    # Sort by logic_id = 1 and category_id = 1
    sorted_logic_1_with_category_1 = (
        session.query(BossMonster)
        .join(MonsterImage)
        .join(MonsterCategory)
        .join(MonsterLogic)
        .filter(BossMonster.monster_logic_id == 1, BossMonster.monster_category_id == 1)
        .order_by(BossMonster.id)  # Sort by ID
        .all()
    )

    # Fetch remaining bosses with logic_id = 1 (but exclude category_id = 1), and bosses with logic_id = 2, 3 and 4, sorted by preview_name
    sorted_logic_1_except_category_1_and_logic_2_3_4 = (
        session.query(BossMonster)
        .join(MonsterImage)
        .join(MonsterCategory)
        .join(MonsterLogic)
        .filter(
            BossMonster.monster_logic_id.in_([1, 2, 3,4]),  # Logic IDs 1, 2, 3 and 4
            ~BossMonster.id.in_([boss.id for boss in sorted_logic_1_with_category_1])
            # Exclude bosses from logic_id=1 and category_id=1
        )
        .order_by(asc(BossMonster.preview_name))  # Sort by preview_name
        .all()
    )

    # Combine the results into one list in the desired order
    boss_monsters = sorted_logic_1_with_category_1 + sorted_logic_1_except_category_1_and_logic_2_3_4

    # Pass the data to add the widgets
    for boss in boss_monsters:
        # print(boss.monster_logic_id)
        add_monster_to_frame(main_window,boss)

    session.close()

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
    # Open the dialog and wait for a response (blocking call)
    if dialog.exec() == QDialog.Accepted:
        # Handle successful save
        print("Monster configuration saved!")
    else:
        # Handle cancel or rejection
        print("Monster configuration canceled!")

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
    # Get the frame ref
    monsters_list_frame = main_window.widgets.monsters_list_frame
    # loop through all the checkboxes in that
    for checkbox in monsters_list_frame.findChildren(QCheckBox):
        if checkbox.isChecked():
            checked_monsters.append(checkbox)

    # check if the checkbox contains any value or not
    if len(checked_monsters) == 0:
        # TODO
        print("Show error message saying to select some options")
        return False

    # TODO Convert those data to zip
    for checkbox in checked_monsters:
        print(f"Checkbox boss id: {checkbox.property("boss_id")}")

    # Toggle confirm frame
    main_window.widgets.export_monsters_btn.setChecked(False)
