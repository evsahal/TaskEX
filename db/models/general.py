import enum

from sqlalchemy import Column, Integer, String, Enum, Float

from db.db_setup import Base


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
    details_image_name = Column(String, nullable=False)  # Image from the details view
    list_image_name = Column(String, nullable=True)  # Image from the list view (nullable initially)
    image_resolution = Column(Enum(ImageResolution), nullable=False, default=ImageResolution.p540)  # Default to 540p
    type = Column(Enum(GeneralType), nullable=False)
    scale = Column(Float, nullable=True)

    def __repr__(self):
        return f"<General(id={self.id},name={self.name}, type={self.type.value}, resolution={self.image_resolution.value}, details_image={self.details_image_name},list_image={self.list_image_name},scale={self.scale})>"

    @classmethod
    def find_pending_list_view_generals(cls, session, general_type=None):
        """
        Find generals that have a NULL scale, indicating that a list view scan is pending.
        Optionally filter by the general type (epic, legendary, or both).

        :param session: The SQLAlchemy session to use for the query.
        :param general_type: Optional filter for the general's type (epic, legendary, or None for both).
        :return: A list of General objects with NULL scale (pending list view scans).
        """
        query = session.query(cls).filter(cls.scale.is_(None))  # Base query for pending generals

        if general_type:
            query = query.filter(cls.type == general_type)  # Filter by specific type if provided

        return query.all()

    @classmethod
    def get_all_valid_general_names(cls, session):
        """
        Find all generals where the scale field is not null.

        :param session: The SQLAlchemy session to use for the query.
        :return: A list of General objects with a non-null scale.
        """
        results = session.query(cls.name).filter(cls.scale.isnot(None)).all()
        return [name[0] for name in results]  # Extract the name from each tuple