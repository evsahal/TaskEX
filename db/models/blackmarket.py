from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.db_setup import Base

class BlackMarket(Base):
    __tablename__ = 'blackmarket'
    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    purchase_rss = Column(Boolean, default=False)
    purchase_gems = Column(Boolean, default=False)
    purchase_gold = Column(Boolean, default=False)
    system = Column(Boolean, default=False)

    items = relationship("BlackMarketItem", back_populates="blackmarket", cascade="all, delete-orphan")

class BlackMarketItem(Base):
    __tablename__ = 'blackmarket_item'
    id = Column(Integer, primary_key=True)
    blackmarket_id = Column(Integer,  ForeignKey('blackmarket.id', ondelete="CASCADE"))
    item_image = Column(String, nullable=False)

    blackmarket = relationship("BlackMarket", back_populates="items")
