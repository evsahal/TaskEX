from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from db.db_setup import get_session
from db.models import MonsterLevel, JoinRallyPresetOption, PresetGeneralAssignment, GeneralPreset, \
    JoinRallyPresetConfiguration


def get_join_rally_controls(main_window, index):

    # GET MONSTER DATA TO JOIN
    jr_monster_list1_frame = getattr(main_window.widgets,f"jr_monster_list1_frame_{index}")
    jr_monster_list2_frame = getattr(main_window.widgets,f"jr_monster_list2_frame_{index}")
    selected_level_ids = []

    # Iterate over all widgets in the jr_monster_list1_frame to get all the logic 1 bosses
    for checkbox in jr_monster_list1_frame.findChildren(QCheckBox):
        if not checkbox.isChecked():  # Not skipped (unchecked)
            level_id = checkbox.property("level_id")
            if level_id :
                selected_level_ids.append(level_id)

    # Iterate over all widgets in the jr_monster_list1_frame to get all the other logic bosses
    session = get_session()
    for checkbox in jr_monster_list2_frame.findChildren(QCheckBox):
        # Get the boss_id from the checkbox
        boss_id = int(checkbox.property("boss_id"))
        if not checkbox.isChecked():  # None skipped (unchecked)
            # if checkbox not checked, then include all the levels of that boss
            level_ids = session.execute(select(MonsterLevel.id).where(
                boss_id == MonsterLevel.boss_monster_id)).scalars().all()
            selected_level_ids.extend(level_ids)
        else:
            # if checkbox is checked, then find and skip the selected levels of that boss
            logic_id = int(checkbox.property("logic"))
            if logic_id in (2,3): # for logic 2 and 3
                # Fetch the corresponding combo box
                check_combo_box = getattr(main_window.widgets,f"jr_combobox_boss{checkbox.property('boss_id')}___{index}")
                for i in range(check_combo_box.count()):
                    if check_combo_box.itemCheckState(i) == Qt.Unchecked:
                        level_id = check_combo_box.itemData(i)  # Get the level ID
                        selected_level_ids.append(level_id)
            elif logic_id == 4: # for logic 4
                # Fetch the corresponding button
                button = getattr(main_window.widgets,f"jr_button_boss{checkbox.property('boss_id')}___{index}")
                skipped_levels = button.property('selected_ids')
                remaining_levels = session.execute(
                    select(MonsterLevel.id).where(
                        boss_id == MonsterLevel.boss_monster_id,MonsterLevel.id.notin_(skipped_levels))
                ).scalars().all()
                selected_level_ids.extend(remaining_levels)


    # get the level details based on the selected levels for the rallies
    levels = session.execute(
        select(MonsterLevel)
        .options(joinedload(MonsterLevel.boss_monster))  # Load BossMonster relationship
        .where(MonsterLevel.id.in_(selected_level_ids))
    ).scalars().all()



    # for level in levels:
    #     # print(level.boss_monster.monster_logic_id)
    #     print(level.level,level.name)

    # GET JOIN RALLY SETTINGS
    settings = {"selected_presets": {"presets": {}, "general_preset_config": None, "main_generals": None, "assistant_generals": None}}

    # Selected presets and its settings
    selected_presets = []
    # Start capturing march preset settings
    for preset_number in range(1, 9):  # Iterate through all 8 presets
        preset_button = getattr(main_window.widgets, f"rotate_preset_{preset_number}___{index}")
        if preset_button.isChecked():  # Check if the preset is selected
            selected_presets.append(preset_number)

    # Fetch preset options from the database for the selected presets
    try:
        profile_id = getattr(main_window.widgets, f"emu_profile_{index}").currentData()
        preset_config = session.query(JoinRallyPresetConfiguration).filter_by(profile_id=profile_id).first()
        preset_options = session.query(JoinRallyPresetOption).filter(
            JoinRallyPresetOption.preset_configuration_id == preset_config.id,
            JoinRallyPresetOption.preset_number.in_(selected_presets)
        ).all()

        # Process each selected preset's options
        use_selected_generals_flag = False

        for option in preset_options:
            # Add preset settings under 'presets' key with the preset number as key
            settings["selected_presets"]["presets"][option.preset_number] = {
                "use_selected_generals": option.use_selected_generals,
                "skip_no_general": option.skip_no_general,
                "reset_to_one_troop": option.reset_to_one_troop,
            }

            # Check if any selected preset has 'use_selected_generals' enabled
            if option.use_selected_generals:
                use_selected_generals_flag = True

        # If 'use_selected_generals' is enabled, fetch GeneralPreset and PresetGeneralAssignment data
        if use_selected_generals_flag:
            general_preset = session.query(GeneralPreset).filter_by(id=preset_config.general_preset_id).first()
            if general_preset:
                settings["selected_presets"]["general_preset_config"] = {
                    "id": general_preset.id,
                    "name": general_preset.name,
                    "general_category": general_preset.general_category.value,
                    "general_view": general_preset.general_view.value,
                    "general_filter": general_preset.general_filter,
                    "swipe_attempts": general_preset.swipe_attempts
                }

                main_generals = session.query(PresetGeneralAssignment).filter_by(
                    preset_id=general_preset.id,
                    is_main_general=True
                ).all()

                assistant_generals = session.query(PresetGeneralAssignment).filter_by(
                    preset_id=general_preset.id,
                    is_main_general=False
                ).all()

                settings["selected_presets"]["main_generals"] = [
                    {
                        "id": gen.general.id,  "name": gen.general.name,  "details_image_name": gen.general.details_image_name,
                        "list_image_name": gen.general.list_image_name
                    }
                    for gen in main_generals
                ]

                settings["selected_presets"]["assistant_generals"] = [
                    {
                        "id": gen.general.id, "name": gen.general.name,
                        "details_image_name": gen.general.details_image_name,
                        "list_image_name": gen.general.list_image_name
                    }
                    for gen in assistant_generals
                ]


    except Exception as e:
        print(e)

    finally:
        session.close()


    # Auto use stamina
    auto_use_stamina_checkbox = getattr(main_window.widgets, f"jr_auto_use_stamina___{index}")
    auto_use_stamina_combobox = getattr(main_window.widgets, f"jr_auto_use_stamina_options___{index}")
    settings["auto_use_stamina"] = {
        "enabled": auto_use_stamina_checkbox.isChecked(),  # Checkbox value
        "option": None if not auto_use_stamina_checkbox.isChecked() else auto_use_stamina_combobox.currentText()
    }

    # March Speed Boost
    march_speed_boost_checkbox = getattr(main_window.widgets, f"jr_march_speed___{index}")
    march_speed_boost_config_btn = getattr(main_window.widgets, f"jr_march_speed_configure___{index}")
    settings["march_speed_boost"] = {
        "enabled": march_speed_boost_checkbox.isChecked(),  # Checkbox value
        "option": None if not march_speed_boost_checkbox.isChecked() else march_speed_boost_config_btn.property('config_values')
    }

    # combine the dict to return the values
    join_rally_controls = {
        "data": levels,
        "settings": settings
    }

    return join_rally_controls

def get_game_settings_controls(main_window,index):

    kick_reload_spinbox = getattr(main_window.widgets, f"kick_reload_spinbox___{index}")
    game_settings = {'kick_reload':kick_reload_spinbox.value()}
    return game_settings
