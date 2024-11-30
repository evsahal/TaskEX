import enum
from sqlalchemy import (
    Column, Integer, String, Enum, ForeignKey, Boolean, Float
)
from sqlalchemy.orm import relationship
from db.db_setup import Base


# Enum for GeneralPreset Categories
class GeneralCategory(enum.Enum):
    all = "All"
    military = "Military"
    development = "Development"
    duty = "Duty"
    subordinate_city = "Subordinate City"


# Enum for GeneralPreset Views
class GeneralView(enum.Enum):
    details_view = "Details View"
    list_view = "List View"


# Enum for GeneralPreset Filters
class GeneralFilter(enum.Enum):
    favorite = "Favorite"
    idle = "Idle"


# GeneralPreset Table
class GeneralPreset(Base):
    __tablename__ = 'general_presets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    general_category = Column(Enum(GeneralCategory), nullable=False, default=GeneralCategory.all)
    general_view = Column(Enum(GeneralView), nullable=False,default=GeneralView.details_view)
    general_filter = Column(String, nullable=True,default=None)  # Comma-separated or JSON
    swipe_attempts = Column(Integer, nullable=False, default=5)

    # Relationship with PresetGeneralAssignment
    assigned_generals = relationship(
        "PresetGeneralAssignment", cascade="all, delete", back_populates="preset"
    )
    # Relationship with JoinRallyPresetConfiguration
    jr_preset_configurations = relationship(
        "JoinRallyPresetConfiguration",
        back_populates="general_preset",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"<GeneralPreset(id={self.id}, name={self.name}, category={self.general_category.value}, "
            f"view={self.general_view.value}, filter={self.general_filter}, swipe_attempts={self.swipe_attempts})>"
        )


# PresetGeneralAssignment Table
class PresetGeneralAssignment(Base):
    __tablename__ = 'preset_general_assignment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    preset_id = Column(Integer, ForeignKey('general_presets.id', ondelete="CASCADE"))
    general_id = Column(Integer, ForeignKey('generals.id', ondelete="CASCADE"))
    is_main_general = Column(Boolean, nullable=False)

    # Relationships
    preset = relationship("GeneralPreset", back_populates="assigned_generals")
    general = relationship("General")

    def __repr__(self):
        return (
            f"<PresetGeneralAssignment(id={self.id}, preset_id={self.preset_id}, "
            f"general_id={self.general_id}, is_main_general={self.is_main_general})>"
        )
