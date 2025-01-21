from sqlalchemy import Column, Integer, String

from db.db_setup import Base


class ScreenConfig(Base):
    __tablename__ = 'screen_config'

    id = Column(Integer, primary_key=True)
    screen_resolution = Column(String(20), nullable=False, unique=True)  # VARCHAR(20) NOT NULL UNIQUE
    dpi = Column(Integer, default=96)  # INTEGER DEFAULT 96

