from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta 

engine = create_engine('sqlite:///stati.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# User Interactions

if session.query(Status).all() == []:
    status = Status(label="feeder", state="up", string="Dog feeder is ")
    session.add(status)
    session.commit()

def set_status(state, label="feeder"):
    status = session.query(Status).filter_by(label=label).first()
    status.state = state
    session.add(status)
    session.commit()

def get_status(label="feeder"):
    return session.query(Status).filter_by(label=label).first()
