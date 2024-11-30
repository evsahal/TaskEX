from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.db_setup import Base

class Profile(Base):
    """
    Represents a profile.
    """
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Relationships
    jr_preset_configurations = relationship(
        "JoinRallyPresetConfiguration",
        back_populates="profile",
        cascade="all, delete-orphan"
    )