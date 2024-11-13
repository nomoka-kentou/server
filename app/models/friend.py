from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.settings import Base


class Friend(Base):
    __tablename__ = 'friend'

    id = Column(Integer, primary_key=True, index=True)
