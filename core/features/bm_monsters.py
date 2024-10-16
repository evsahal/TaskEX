from sqlalchemy import asc
from sqlalchemy.orm import joinedload
from db.db_setup import get_session
from db.models import BossMonster, MonsterImage, MonsterCategory, MonsterLogic

def get_all_boss_monster_data():
    # Get all the bosses
    session = get_session()

    # Eagerly load the related MonsterImage, MonsterCategory, and MonsterLogic using joinedload
    sorted_logic_1_with_category_1 = (
        session.query(BossMonster)
        .join(MonsterImage)
        .join(MonsterCategory)
        .join(MonsterLogic)
        .options(
            joinedload(BossMonster.monster_image),  # Eagerly load monster_image
            joinedload(BossMonster.monster_category),  # Eagerly load monster_category
            joinedload(BossMonster.monster_logic)  # Eagerly load monster_logic
        )
        .filter(BossMonster.monster_logic_id == 1, BossMonster.monster_category_id == 1)
        .order_by(BossMonster.id)  # Sort by ID
        .all()
    )

    sorted_logic_1_except_category_1_and_logic_2_3_4 = (
        session.query(BossMonster)
        .join(MonsterImage)
        .join(MonsterCategory)
        .join(MonsterLogic)
        .options(
            joinedload(BossMonster.monster_image),  # Eagerly load monster_image
            joinedload(BossMonster.monster_category),  # Eagerly load monster_category
            joinedload(BossMonster.monster_logic)  # Eagerly load monster_logic
        )
        .filter(
            BossMonster.monster_logic_id.in_([1, 2, 3, 4]),
            ~BossMonster.id.in_([boss.id for boss in sorted_logic_1_with_category_1])
        )
        .order_by(asc(BossMonster.preview_name))  # Sort by preview_name
        .all()
    )

    # Combine the results
    boss_monsters = sorted_logic_1_with_category_1 + sorted_logic_1_except_category_1_and_logic_2_3_4

    session.close()
    return boss_monsters
