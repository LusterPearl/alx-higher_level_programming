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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of Student instance.

        Args:
            attrs (list of str, optional): A list of attributes.
                If not provided or if attrs is not a list, all attributes.

        Returns:
            dict: A  dictionary containing the specified attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
