from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
NOTE_TYPES = ['prescription', 'appointment']

class Status(Base):
    __tablename__ = "note_types"
    id = Column(Integer, primary_key=True)
    label = Column(String)
    state = Column(String)
