#!/usr/bin/python3
""" A class with student first_name and last_name. """


class Student:
    """
    Represents a student with first_name, last_name and age attribute.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of Student instance.

        Returns:
            dict: A  dictionary containing the attributes of the Student.
        """
        return self.__dict__
