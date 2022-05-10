from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Status(Base):
    __tablename__ = "stati"
    id = Column(Integer, primary_key=True)
    label = Column(String)
    string = Column(String)
    state = Column(String)
