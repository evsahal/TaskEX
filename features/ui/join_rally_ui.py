from tabnanny import check

from PySide6.QtWidgets import QCheckBox, QFrame, QVBoxLayout, QPushButton

from core.custom_widgets.FlowLayout import FlowLayout
from core.custom_widgets.QCheckComboBox import QCheckComboBox
from core.services.bm_monsters_service import fetch_boss_monster_data
from db.db_setup import get_session
from db.models import BossMonster


def load_join_rally_ui(instance_ui):
    # For Logic 1
    jr_monster_list1_frame = getattr(instance_ui, "jr_monster_list1_frame_")
    flow_layout_1 =  FlowLayout()
    jr_monster_list1_frame.setLayout(flow_layout_1)

    # For Other Logics
    jr_monster_list2_frame = getattr(instance_ui, "jr_monster_list2_frame_")
    flow_layout_2 =  FlowLayout()
    jr_monster_list2_frame.setLayout(flow_layout_2)
    session = get_session()

    # Fetch Logic 1, Category 1 (no sorting by preview_name, keep the order by ID)
    boss_monsters = fetch_boss_monster_data(session, 1, 1, None)
    # Fetch Logic 1, Other Categories (sorted by preview_name)
    boss_monsters += fetch_boss_monster_data(session, 1, None, BossMonster.preview_name)
    for boss in boss_monsters:
        if boss.monster_logic.id == 1:
            setup_logic_1(boss,instance_ui,flow_layout_1)

    # Fetch Logics 2, 3, and 4 (sorted by preview_name)
    boss_monsters = fetch_boss_monster_data(session, [2, 3, 4], None, BossMonster.preview_name)
    for boss in boss_monsters:
        # print(f"Name : {boss.preview_name} :: Logic : {boss.monster_logic.id}")
        if boss.monster_logic.id == 2:
            setup_logic_2(boss, instance_ui, flow_layout_2)
        elif boss.monster_logic.id == 3:
            setup_logic_3(boss, instance_ui, flow_layout_2)
        elif boss.monster_logic.id == 4:
            setup_logic_4(boss, instance_ui, flow_layout_2)

def setup_logic_1(boss,instance_ui,flow_layout):
    # print(f"Name : {boss.preview_name} :: Logic : {boss.monster_logic.id}")
    checkbox = QCheckBox(boss.preview_name)
    checkbox.setObjectName(f"jr_checkbox_boss{boss.id}___")
    # Custom property to store the boss id and logic
    checkbox.setProperty("boss_id", boss.id)
    checkbox.setProperty("logic", boss.monster_logic.id)
    setattr(instance_ui, checkbox.objectName(), checkbox)
    flow_layout.addWidget(checkbox)

def setup_logic_2(boss,instance_ui,flow_layout):
    frame = QFrame()
    vert_layout = QVBoxLayout()
    vert_layout.setContentsMargins(0, 0, 10, 5)

    # Add a checkbox for the boss
    checkbox = QCheckBox(boss.preview_name)
    checkbox.setObjectName(f"jr_checkbox_boss{boss.id}___")
    # Custom property to store the boss id and logic
    checkbox.setProperty("boss_id", boss.id)
    checkbox.setProperty("logic", boss.monster_logic.id)
    setattr(instance_ui, checkbox.objectName(), checkbox)
    checkbox.stateChanged.connect(lambda : switch_monster_checkbox(instance_ui,boss.id))
    vert_layout.addWidget(checkbox)

    # Add a QCheckComboBox for the boss's levels
    combo_box = QCheckComboBox(placeholderText="None")
    combo_box.setObjectName(f"jr_combobox_boss{boss.id}___")
    combo_box.setFixedHeight(40)
    combo_box.setMinimumWidth(150)
    setattr(instance_ui, combo_box.objectName(), combo_box)

    # Populate the QCheckComboBox with levels
    for level in boss.levels:
        combo_box.addItem(f"Level {level.level}")

    # Disable it by default
    combo_box.setDisabled(True)

    vert_layout.addWidget(combo_box)
    # Add the vertical layout to the frame
    frame.setLayout(vert_layout)

    # Add the frame to the flow layout
    flow_layout.addWidget(frame)

def setup_logic_3(boss,instance_ui,flow_layout):
    frame = QFrame()
    vert_layout = QVBoxLayout()
    vert_layout.setContentsMargins(0, 0, 10, 5)

    # Add a checkbox for the boss
    checkbox = QCheckBox(boss.preview_name)
    checkbox.setObjectName(f"jr_checkbox_boss{boss.id}___")
    # Custom property to store the boss id and logic
    checkbox.setProperty("boss_id", boss.id)
    checkbox.setProperty("logic", boss.monster_logic.id)
    setattr(instance_ui, checkbox.objectName(), checkbox)
    checkbox.stateChanged.connect(lambda : switch_monster_checkbox(instance_ui,boss.id))
    vert_layout.addWidget(checkbox)

    # Add a QCheckComboBox for the boss's levels
    combo_box = QCheckComboBox(placeholderText="None")
    combo_box.setObjectName(f"jr_combobox_boss{boss.id}___")
    combo_box.setFixedHeight(40)
    combo_box.setMinimumWidth(150)
    setattr(instance_ui, combo_box.objectName(), combo_box)

    # Populate the QCheckComboBox with levels
    for level in boss.levels:
        combo_box.addItem(level.name)

    # Disable it by default
    combo_box.setDisabled(True)

    vert_layout.addWidget(combo_box)
    # Add the vertical layout to the frame
    frame.setLayout(vert_layout)

    # Add the frame to the flow layout
    flow_layout.addWidget(frame)


def setup_logic_4(boss,instance_ui,flow_layout):
    frame = QFrame()
    vert_layout = QVBoxLayout()
    vert_layout.setContentsMargins(0, 0, 10, 5)

    # Add a checkbox for the boss
    check_box = QCheckBox(boss.preview_name)
    check_box.setObjectName(f"jr_checkbox_boss{boss.id}___")
    setattr(instance_ui, check_box.objectName(), check_box)
    check_box.stateChanged.connect(lambda: switch_monster_checkbox(instance_ui, boss.id,False))
    vert_layout.addWidget(check_box)

    # Add a Pushbutton for listing boss levels
    button = QPushButton("Select Levels")
    button.setObjectName(f"jr_button_boss{boss.id}___")
    button.setFixedHeight(40)
    button.setMinimumWidth(150)
    setattr(instance_ui, button.objectName(), button)

    # Disable it by default
    button.setDisabled(True)

    vert_layout.addWidget(button)
    # Add the vertical layout to the frame
    frame.setLayout(vert_layout)

    # Add the frame to the flow layout
    flow_layout.addWidget(frame)


def switch_monster_checkbox(instance_ui, boss_id, default=True):
    """
    Toggles the state of a combo box or a button based on the checkbox state.

    :param instance_ui: The UI instance containing the widgets.
    :param boss_id: The ID of the boss associated with the widgets.
    :param default: If True, handles the combo box. If False, handles the button.
    """
    checkbox = getattr(instance_ui, f"jr_checkbox_boss{boss_id}___")

    if default:  # Handle the combo box
        combobox = getattr(instance_ui, f"jr_combobox_boss{boss_id}___")
        if checkbox.isChecked():
            combobox.setDisabled(False)
        else:
            # Uncheck all items in the combo box when disabled
            for i in combobox.checkedIndices():
                combobox.setItemCheckState(i, False)
            combobox.setDisabled(True)
    else:  # Handle the button
        button = getattr(instance_ui, f"jr_button_boss{boss_id}___")
        button.setDisabled(not checkbox.isChecked())