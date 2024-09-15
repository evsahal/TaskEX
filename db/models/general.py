from sqlalchemy import Column, Integer, String, Enum
from db.db_setup import Base
import enum


# Enum for General Types
class GeneralType(enum.Enum):
    legendary = "Legendary Historic General"
    epic = "Epic Historic General"


# Enum for Image Resolutions
class ImageResolution(enum.Enum):
    p540 = "540p"
    p1080 = "1080p"


class General(Base):
    __tablename__ = 'generals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)  # Set name as unique
    image_name = Column(String, nullable=False)
    image_resolution = Column(Enum(ImageResolution), nullable=False, default=ImageResolution.p540)  # Default to 540p
    type = Column(Enum(GeneralType), nullable=False)

    def __repr__(self):
        return f"<General(name={self.name}, type={self.type.value}, resolution={self.image_resolution.value})>"
