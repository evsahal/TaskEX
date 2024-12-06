from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.db_setup import Base
from db.models import Profile


class Instance(Base):
    """
    Represents an emulator instance.
    """
    __tablename__ = "instances"

    id = Column(Integer, primary_key=True)
    emulator_name = Column(String, nullable=True)
    emulator_port = Column(Integer, nullable=True)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    profile = relationship("Profile", back_populates="instances")

# Update the Profile class to include the relationship
Profile.instances = relationship(
    "Instance",
    back_populates="profile",
    cascade="all, delete-orphan"
)
