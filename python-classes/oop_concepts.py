#!/usr/bin/python3
"""
Comprehensive OOP concepts demonstration
"""


class Student:
    """
    A Student class demonstrating various OOP concepts
    """
    
    # Class attribute
    school = "ALU"
    
    def __init__(self, name, age):
        """
        Initialize a Student instance
        
        Args:
            name (str): Student's name
            age (int): Student's age
        """
        # Public attributes
        self.name = name
        self.age = age
        
        # Protected attribute (convention: single underscore)
        self._student_id = None
        
        # Private attribute (name mangling: double underscore)
        self.__grade = None
    
    def get_info(self):
        """
        Public method to get student information
        
        Returns:
            str: Student information
        """
        return f"Student: {self.name}, Age: {self.age}"
    
    def _set_student_id(self, student_id):
        """
        Protected method (convention: single underscore)
        
        Args:
            student_id (str): Student ID to set
        """
        self._student_id = student_id
    
    def __calculate_gpa(self):
        """
        Private method (name mangling: double underscore)
        
        Returns:
            float: Calculated GPA
        """
        return 3.5  # Simplified calculation
    
    # Property example - Pythonic getter/setter
    @property
    def grade(self):
        """Getter for grade"""
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        """Setter for grade with validation"""
        if 0 <= value <= 100:
            self.__grade = value
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    def __str__(self):
        """String representation of the object"""
        return f"Student({self.name}, {self.age})"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Student(name='{self.name}', age={self.age})"


# Demonstration
if __name__ == "__main__":
    # Create instances
    student1 = Student("Alice", 20)
    student2 = Student("Bob", 22)
    
    print("=== Basic Usage ===")
    print(student1.get_info())
    print(student2.get_info())
    
    print("\n=== Class vs Instance Attributes ===")
    print(f"Class attribute - Student.school: {Student.school}")
    print(f"Instance attribute - student1.name: {student1.name}")
    
    print("\n=== Property Usage ===")
    student1.grade = 85
    print(f"Student1 grade: {student1.grade}")
    
    print("\n=== Dynamic Attribute Creation ===")
    student1.major = "Computer Science"  # Dynamic attribute
    print(f"Student1 major: {student1.major}")
    
    print("\n=== __dict__ Contents ===")
    print(f"student1.__dict__: {student1.__dict__}")
    print(f"Student.__dict__ keys: {list(Student.__dict__.keys())}")
    
    print("\n=== getattr Function ===")
    print(f"getattr(student1, 'name'): {getattr(student1, 'name')}")
    print(f"getattr(student1, 'nonexistent', 'default'): {getattr(student1, 'nonexistent', 'default')}")
    
    print("\n=== Attribute Access ===")
    print("Public attribute access:")
    print(f"student1.name: {student1.name}")
    
    print("Protected attribute access (by convention):")
    student1._set_student_id("ALU001")
    print(f"student1._student_id: {student1._student_id}")
    
    print("Private attribute access (name mangling):")
    print(f"student1._Student__grade: {student1._Student__grade}")
    
    print("\n=== String Representations ===")
    print(f"str(student1): {str(student1)}")
    print(f"repr(student1): {repr(student1)}")
