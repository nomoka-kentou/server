from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.settings import Base


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), nullable=False)
