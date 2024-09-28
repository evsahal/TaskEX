from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.db_setup import Base

# Monster Category Table
class MonsterCategory(Base):
    __tablename__ = 'monster_categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Monster Image Table
class MonsterImage(Base):
    __tablename__ = 'monster_images'
    id = Column(Integer, primary_key=True)
    preview_image = Column(String, nullable=True)
    img_540p = Column(String, nullable=True)
    img_threshold = Column(Float, nullable=True)
    click_pos = Column(String, nullable=True)

# Monster Logic Table
class MonsterLogic(Base):
    __tablename__ = 'monster_logics'
    id = Column(Integer, primary_key=True)
    logic = Column(String, nullable=False)
    description = Column(String, nullable=False)

# Monster Level Table
class MonsterLevel(Base):
    __tablename__ = 'monster_levels'
    id = Column(Integer, primary_key=True)
    boss_monster_id = Column(Integer, ForeignKey('boss_monsters.id'))
    level = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    power = Column(String, nullable=False)
    boss_monster = relationship("BossMonster", back_populates="levels")

# Boss Monster Table
class BossMonster(Base):
    __tablename__ = 'boss_monsters'
    id = Column(Integer, primary_key=True)
    preview_name = Column(String, nullable=False)
    monster_category_id = Column(Integer, ForeignKey('monster_categories.id'))
    monster_image_id = Column(Integer, ForeignKey('monster_images.id'))
    monster_logic_id = Column(Integer, ForeignKey('monster_logics.id'))
    enable_map_scan = Column(Boolean, default=True)
    system = Column(Boolean, default=False)

    # Relationships
    monster_category = relationship("MonsterCategory")
    monster_image = relationship("MonsterImage")
    monster_logic = relationship("MonsterLogic")
    levels = relationship("MonsterLevel", back_populates="boss_monster")
