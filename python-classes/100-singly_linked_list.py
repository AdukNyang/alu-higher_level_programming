#!/usr/bin/python3
"""Module that defines a Node and SinglyLinkedList."""


class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node.
  
        Args:
            data: The data value for the node.
            next_node: The next node in the list.
            """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data value."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value.
    
        Args:
            value: The data value to set.
    
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value: The next node to set.
    
        Raises:
            TypeError: If value is not None or a Node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position.
  
        Args:
            value: The value to insert.
        """
        new_node = Node(value)
  
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
 
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
 
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return string representation of the list."""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
