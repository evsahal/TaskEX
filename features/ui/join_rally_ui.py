from tabnanny import check

from PySide6.QtWidgets import QCheckBox, QFrame, QVBoxLayout

from core.custom_widgets.FlowLayout import FlowLayout
from core.custom_widgets.QCheckComboBox import QCheckComboBox
from core.services.bm_monsters_service import fetch_boss_monster_data
from db.db_setup import get_session
from db.models import BossMonster


def load_join_rally_ui(instance_ui):
    jr_monster_list_frame = getattr(instance_ui, "jr_monster_list_frame_")
    flow_layout =  FlowLayout()
    jr_monster_list_frame.setLayout(flow_layout)
    session = get_session()

    # Fetch Logic 1, Category 1 (no sorting by preview_name, keep the order by ID)
    boss_monsters = fetch_boss_monster_data(session, 1, 1, None)
    # Fetch Logic 1, Other Categories (sorted by preview_name)
    boss_monsters += fetch_boss_monster_data(session, 1, None, BossMonster.preview_name)
    for boss in boss_monsters:
        if boss.monster_logic.id == 1:
            setup_logic_1(boss,instance_ui,flow_layout)

    # Fetch Logics 2, 3, and 4 (sorted by preview_name)
    boss_monsters = fetch_boss_monster_data(session, [2, 3, 4], None, BossMonster.preview_name)
    for boss in boss_monsters:
        # print(f"Name : {boss.preview_name} :: Logic : {boss.monster_logic.id}")
        if boss.monster_logic.id == 2:
            setup_logic_2(boss, instance_ui, flow_layout)
        elif boss.monster_logic.id == 3:
            setup_logic_3(boss, instance_ui, flow_layout)
        elif boss.monster_logic.id == 4:
            setup_logic_4(boss, instance_ui, flow_layout)

def setup_logic_1(boss,instance_ui,flow_layout):
    # print(f"Name : {boss.preview_name} :: Logic : {boss.monster_logic.id}")
    cbox = QCheckBox(boss.preview_name)
    cbox.setObjectName(f"jr_checkbox_boss{boss.id}___")
    setattr(instance_ui, cbox.objectName(), cbox)
    flow_layout.addWidget(cbox)

def setup_logic_2(boss,instance_ui,flow_layout):
    frame = QFrame()
    vert_layout = QVBoxLayout()
    vert_layout.setContentsMargins(0, 0, 10, 5)

    # Add a checkbox for the boss
    check_box = QCheckBox(boss.preview_name)
    check_box.setObjectName(f"jr_checkbox_boss{boss.id}___")
    setattr(instance_ui, check_box.objectName(), check_box)
    check_box.stateChanged.connect(lambda : switch_monster_checkbox(instance_ui,boss.id))
    vert_layout.addWidget(check_box)

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
    check_box = QCheckBox(boss.preview_name)
    check_box.setObjectName(f"jr_checkbox_boss{boss.id}___")
    setattr(instance_ui, check_box.objectName(), check_box)
    check_box.stateChanged.connect(lambda : switch_monster_checkbox(instance_ui,boss.id))
    vert_layout.addWidget(check_box)

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
    check_box.stateChanged.connect(lambda: switch_monster_checkbox(instance_ui, boss.id))
    vert_layout.addWidget(check_box)




def switch_monster_checkbox(instance_ui,boss_id):
    checkbox = getattr(instance_ui, f"jr_checkbox_boss{boss_id}___")
    combobox = getattr(instance_ui, f"jr_combobox_boss{boss_id}___")
    if checkbox.isChecked():
        combobox.setDisabled(False)
    else:
        for i in combobox.checkedIndices():
            combobox.setItemCheckState(i, False)
        combobox.setDisabled(True)