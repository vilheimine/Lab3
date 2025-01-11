"""
File: student_sort_demo.py
Demonstration of sorting Student objects based on name.
"""

from random import shuffle

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Tests if this student equals another student based on name."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name

    def __lt__(self, other):
        """Tests if this student is less than another student based on name."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.name < other.name

    def __ge__(self, other):
        """Tests if this student is greater than or equal to another student based on name."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.name >= other.name

def main():
    """Creates a list of students, shuffles it, and demonstrates sorting."""
    # Create a list of students
    students = [
        Student("Alice", 3),
        Student("Bob", 3),
        Student("Charlie", 3),
        Student("David", 3),
        Student("Eve", 3)
    ]
    
    # Set some example scores for each student
    for student in students:
        student.setScore(1, 85)
        student.setScore(2, 90)
        student.setScore(3, 95)
    
    print("Original student list:")
    for student in students:
        print(student)
        print()  # Empty line for readability
        
    # Shuffle the list
    shuffle(students)
    
    print("\nShuffled student list:")
    for student in students:
        print(student)
        print()  # Empty line for readability
        
    # Sort the list
    students.sort()
    
    print("\nSorted student list:")
    for student in students:
        print(student)
        print()  # Empty line for readability

if __name__ == "__main__":
    main()
