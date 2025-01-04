from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from db.db_setup import get_session
from db.models import MonsterLevel


def get_join_rally_controls(main_window, index):
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

    session.close()

    for level in levels:
        # print(level.boss_monster.monster_logic_id)
        print(level.level,level.name)
