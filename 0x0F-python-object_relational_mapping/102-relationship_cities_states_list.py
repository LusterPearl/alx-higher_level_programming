#!/usr/bin/python3
"""
Script that creates californai and san francisco
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ Database connection paramatets """
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
    states_states = session.query(City).join(State).order_by(City.id).all()

    """ Loop through the results and print the output """
    for city in cities_states:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    """ commit the changes to the database """
    session.close()
