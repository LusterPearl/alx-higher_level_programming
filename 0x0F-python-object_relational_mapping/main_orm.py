#!/usr/bin/python3
"""Script to connect to MySQL using SQLAlchemy ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, State  # Assuming you have a models.py file with your State class

# Connect to MySQL using SQLAlchemy engine
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

# Create a session
session = Session(engine)

# Query and print using ORM
for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

        # Close the session
        session.close()
