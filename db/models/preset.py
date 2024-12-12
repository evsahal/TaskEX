from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.db_setup import Base

class JoinRallyPresetConfiguration(Base):
    """
    Represents a preset configuration bound to a profile for Join Rally.
    """
    __tablename__ = "jr_preset_configurations"

    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    general_preset_id = Column(Integer, ForeignKey("general_presets.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    profile = relationship("Profile", back_populates="jr_preset_configurations")
    general_preset = relationship("GeneralPreset", back_populates="jr_preset_configurations")

    options = relationship(
        "JoinRallyPresetOption",
        back_populates="preset_configuration",
        cascade="all, delete-orphan"
    )


class JoinRallyPresetOption(Base):
    """
    Represents the individual options for each preset in Join Rally.
    """
    __tablename__ = "jr_preset_options"

    id = Column(Integer, primary_key=True)
    preset_configuration_id = Column(Integer, ForeignKey("jr_preset_configurations.id", ondelete="CASCADE"), nullable=False)
    preset_number = Column(Integer, nullable=False)  # 1 to 8
    preset_selected = Column(Boolean, default=False)
    use_selected_generals = Column(Boolean, default=False)
    skip_no_general = Column(Boolean, default=False)
    reset_to_one_troop = Column(Boolean, default=False)

    # Relationships
    preset_configuration = relationship("JoinRallyPresetConfiguration", back_populates="options")
