#!/usr/bin/python3
"""Script that deletes all state objects with a name containing the letters
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """ Database connectin paramaters """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ create the engine to interact with the database """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (username, password, database),
                           pool_pre_ping=True)

    """ create a configured  class """
    Session = sessionmaker(bind=engine)

    """ create a session instance """
    session = Session()

    """ Query the database to get the first object """
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    """ Commit the changes in it  """
    session.commit()
