from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QFrame, QVBoxLayout, QPushButton
from core.custom_widgets.FlowLayout import FlowLayout
from core.custom_widgets.QCheckComboBox import QCheckComboBox
from core.services.bm_monsters_service import fetch_boss_monster_data
from db.db_setup import get_session
from db.models import BossMonster, MonsterLevel
from gui.widgets.LevelSelectionDialog import LevelSelectionDialog
from gui.widgets.MarchSpeedSelectionJRDialog import MarchSpeedSelectionJRDialog
from gui.widgets.PresetConfigDialog import PresetConfigDialog


def load_join_rally_ui(instance_ui,main_window,index):

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
            setup_logic_1(boss,instance_ui,main_window,flow_layout_1)

    # Fetch Logics 2, 3, and 4 (sorted by preview_name)
    boss_monsters = fetch_boss_monster_data(session, [2, 3, 4], None, BossMonster.preview_name)
    for boss in boss_monsters:
        # print(f"Name : {boss.preview_name} :: Logic : {boss.monster_logic.id}")
        if boss.monster_logic.id == 2:
            setup_logic_2(boss, instance_ui, main_window, flow_layout_2)
        elif boss.monster_logic.id == 3:
            setup_logic_3(boss, instance_ui, main_window, flow_layout_2)
        elif boss.monster_logic.id == 4:
            setup_logic_4(boss, instance_ui, main_window, flow_layout_2)

    ###--- Join Rally Settings ---###

    # Set the type as the property for the push button (profile saving logic)
    for i in range(1, 9):
        object_name = f"rotate_preset_{i}___"
        widget = getattr(instance_ui, object_name, None)  # Get the widget dynamically
        if widget:  # Check if the widget exists
            widget.setProperty("type", "checkable")  # Set the custom property

    # Connect the preset config dialog
    preset_config_btn = getattr(instance_ui, "jr_rotate_preset_settings_")
    preset_config_btn.clicked.connect(lambda :open_preset_settings(main_window,index))

    # Make Preset buttons checked for at least one preset option
    # Generate march preset button names dynamically
    button_names = [f"rotate_preset_{i}___" for i in range(1, 9)]

    # Find march preset buttons dynamically using the object names
    buttons = [getattr(instance_ui, name, None) for name in button_names]

    # Ensure all march preset buttons are valid
    buttons = [btn for btn in buttons if btn is not None]

    # Connect the toggled signal of each button to the on_button_toggled function
    for button in buttons:
        button.toggled.connect(lambda checked, btn=button: on_button_toggled(btn, buttons))

    # Set Auto Use Stamina Combobox
    auto_use_stamina_options = getattr(instance_ui,"jr_auto_use_stamina_options___")
    auto_use_stamina_options.addItem("Min Stamina",1)
    auto_use_stamina_options.addItem("Max Stamina",2)
    auto_use_stamina_options.setCurrentIndex(0)

    # Access the march speed config button
    march_speed_configure_btn = getattr(instance_ui, "jr_march_speed_configure___")
    march_speed_configure_btn.setProperty('type','value')

    # Initialize default settings for this button
    march_speed_configure_btn.setProperty('value',{
        "use_free_boost": True,
        "use_free_boost_gems": False,
        "boost_hours": 1,
        "boost_repeat_times": 9999,
    })

    # Connect boost march speed config button
    march_speed_configure_btn.clicked.connect(lambda: open_march_speed_config_settings(march_speed_configure_btn,main_window, index))

def on_button_toggled(button, buttons):
    # Perform the check only if the march preset button is being unchecked
    if not button.isChecked():
        # Check if all march preset buttons are unchecked
        if not any(btn.isChecked() for btn in buttons):
            # Re-check the march preset button being toggled off
            button.setChecked(True)


def open_preset_settings(main_window,index):
    preset_config_dialog = PresetConfigDialog(main_window,index)
    preset_config_dialog.show()

def open_march_speed_config_settings(btn,main_window,index):
    march_speed_config_dialog = MarchSpeedSelectionJRDialog(main_window,btn,index)
    march_speed_config_dialog.show()


def setup_logic_1(boss,instance_ui,main_window,flow_layout):
    # print(f"Name : {boss.preview_name} :: Logic : {boss.monster_logic.id}")
    checkbox = QCheckBox(boss.preview_name)
    checkbox.setObjectName(f"jr_checkbox_boss{boss.id}___")
    # Custom property to store the boss id and logic
    # checkbox.setProperty("boss_id", boss.id)
    checkbox.setProperty("level_id", boss.levels[0].id)
    # checkbox.setProperty("logic", boss.monster_logic.id)
    setattr(instance_ui, checkbox.objectName(), checkbox)
    flow_layout.addWidget(checkbox)

def setup_logic_2(boss,instance_ui,main_window,flow_layout):
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
    combo_box.setMinimumWidth(135)
    setattr(instance_ui, combo_box.objectName(), combo_box)

    # Populate the QCheckComboBox with levels
    for i,level in enumerate(boss.levels):
        combo_box.addItem(f"Level {level.level}")
        combo_box.setItemData(i, level.id)
        combo_box.setItemCheckState(i, Qt.Unchecked)

    # Disable it by default
    combo_box.setDisabled(True)

    vert_layout.addWidget(combo_box)
    # Add the vertical layout to the frame
    frame.setLayout(vert_layout)

    # Add the frame to the flow layout
    flow_layout.addWidget(frame)

def setup_logic_3(boss,instance_ui,main_window,flow_layout):
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
    combo_box.setMinimumWidth(135)
    setattr(instance_ui, combo_box.objectName(), combo_box)

    # Populate the QCheckComboBox with levels
    for i,level in enumerate(boss.levels):
        combo_box.addItem(level.name)
        combo_box.setItemData(i, level.id)
        combo_box.setItemCheckState(i, Qt.Unchecked)

    # Disable it by default
    combo_box.setDisabled(True)

    vert_layout.addWidget(combo_box)
    # Add the vertical layout to the frame
    frame.setLayout(vert_layout)

    # Add the frame to the flow layout
    flow_layout.addWidget(frame)


def setup_logic_4(boss,instance_ui,main_window,flow_layout):
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
    checkbox.stateChanged.connect(lambda: switch_monster_checkbox(instance_ui, boss.id,False))
    vert_layout.addWidget(checkbox)

    # Add a Pushbutton for listing boss levels
    button = QPushButton("Skip Levels")
    button.setObjectName(f"jr_button_boss{boss.id}___")
    button.setProperty("value", [])
    button.setFixedHeight(40)
    button.setMinimumWidth(135)
    button.setProperty("type", "value")  # Set the custom property
    setattr(instance_ui, button.objectName(), button)
    button.clicked.connect(lambda: open_level_dialog(button, boss.id))

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
            combobox.setCursor(Qt.ArrowCursor)  # Normal cursor
        else:
            # Uncheck all items in the combo box when disabled
            for i in combobox.checkedIndices():
                combobox.setItemCheckState(i, False)
            combobox.setDisabled(True)
            combobox.setCursor(Qt.ForbiddenCursor)  # Restricted cursor
    else:  # Handle the button
        button = getattr(instance_ui, f"jr_button_boss{boss_id}___")
        if checkbox.isChecked():
            button.setDisabled(False)
        else:
            button.setDisabled(True)
            # Clear the selected levels stored in the button
            button.setProperty("value", [])

def open_level_dialog(button, boss_id):
    """
    Open the level selection dialog and store selected levels in the button.
    """
    # Retrieve the previously selected IDs stored in the button
    selected_ids = button.property("value") or []

    # Get all the monster levels
    boss_levels = get_boss_levels(boss_id)

    # Open the dialog with selected IDs and level data
    dialog = LevelSelectionDialog(selected_ids, boss_levels,get_boss_preview_name(boss_id))
    dialog.update_group_checkbox_state()
    if dialog.exec():
        # Save the selected levels back to the button
        button.setProperty("value", list(dialog.selected_ids))  # Convert the set to a list
        # print(f"Selected Levels: {dialog.selected_ids}")



def get_boss_levels(boss_id):
    """
    Fetch all level details for a specific boss from the database.

    :param boss_id: ID of the boss to fetch levels for.
    :return: List of MonsterLevel objects.
    """
    with get_session() as session:
        # Query and return MonsterLevel instances
        levels = (
            session.query(MonsterLevel)
            .filter(MonsterLevel.boss_monster_id == boss_id)
            .order_by(MonsterLevel.level.asc())
            .all()
        )
        return levels

def get_boss_preview_name(boss_id):
    """
    Fetch the preview name of a boss by its ID.

    :param boss_id: ID of the boss.
    :return: Preview name of the boss or None if not found.
    """
    with get_session() as session:
        # Query the preview_name from the BossMonster table
        preview_name = (
            session.query(BossMonster.preview_name)
            .filter(BossMonster.id == boss_id)
            .scalar()
        )
        return preview_name
