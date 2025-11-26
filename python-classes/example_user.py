#!/usr/bin/python3
"""
Example User class to demonstrate OOP concepts
"""


class User:
    """
    A simple User class demonstrating class and instance attributes
    """
    # Class attributes (shared by all instances)
    id = 89
    name = "no name"
    __password = None  # Private class attribute

    def __init__(self, new_name=None):
        """
        Initialize a new User instance
 
        Args:
            new_name (str, optional): Name for the new user
        """
        self.is_new = True  # Public instance attribute
        if new_name is not None:
            self.name = new_name  # This creates an instance attribute


# Example usage and quiz answers:
if __name__ == "__main__":
    # Create instances
    u1 = User("John")
    u2 = User()
 
    print("Quiz Question Answers:")
    print(f"u1.name: {u1.name}")  # John
    print(f"u2.name: {u2.name}")  # no name
    print(f"u2.id: {u2.id}")      # 89
    print(f"u2.is_new: {u2.is_new}")  # True
  
    # Demonstrate class vs instance attributes
    print(f"\nClass attribute User.id: {User.id}")
    print(f"Instance attribute u1.id: {u1.id}")
    print(f"Instance attribute u2.id: {u2.id}")
  
    # Show __dict__ contents
    print(f"\nUser.__dict__: {User.__dict__}")
    print(f"u1.__dict__: {u1.__dict__}")
    print(f"u2.__dict__: {u2.__dict__}")
