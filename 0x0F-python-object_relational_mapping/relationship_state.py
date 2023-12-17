#!/usr/bin/python3
"""
Module containing the class definition of a State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base, City


class State(Base):
    """
    State class that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(256), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
