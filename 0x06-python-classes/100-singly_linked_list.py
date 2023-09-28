#!/usr/bin/python3
"""Module that defines a Square class."""


class Node:
    """Node class for a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the list.
        """

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance.

        Args:
            data (int): The data (integer) to store in the node.
            next_node (Node, optional): The next node in the list.
                Defaults to None.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in the node.

        Args:
            value (int): The data (integer) to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list.

        Args:
            value (Node): The next node to set.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

   class SinglyLinkedList:
        """
        SingyLinkedlist class represents a singly linked list.

        Attributes:
            head (Node): The head of the linked list.
        """

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The data to store in the new node.
        """

        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            prev_node = self.__head
            for current in self.__iter__():
                if current.data >= value:
                    prev_node.next_node = new_node
                    new_node.next_node = current
                    break
                prev_node = current

    def __str__(self):
        result = []
        for current in self.__iter__():
            result.append(str(current.data))
        return "\n".join(result)

    def __iter__(self):
        current = self.__head
        while current:
            yield current
            current = current.next_node
