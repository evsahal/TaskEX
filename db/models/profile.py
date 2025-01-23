from sqlalchemy import Column, Integer, String, ForeignKey, JSON
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

    instances = relationship(
        "Instance",
        back_populates="profile"
    )

    profile_data = relationship(
        "ProfileData",
        back_populates="profile",
        cascade="all, delete-orphan",
        uselist=False  # One-to-one relationship
    )

class ProfileData(Base):
    """
    Represents profile-specific settings for a profile.
    """
    __tablename__ = "profile_data"

    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    settings = Column(JSON, nullable=False)  # Stores settings as JSON

    # Relationships
    profile = relationship("Profile", back_populates="profile_data")