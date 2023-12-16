#!/usr/bin/python3
"""Script that lists all state object from the database
"""

import sys
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """ Main execution """
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
    cities = session.query(City).order_by(City.id).all()

    """Print the results """
    for city in cities:
        state_name = session.query(State.name).filter_by(
                                   id=city.state_id).first()[0]
        print("{}: ({}) {}".format(state_name, city.id, city.name))
