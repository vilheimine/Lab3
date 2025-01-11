"""
File: student.py
Resources to manage a student's name and test scores.
"""

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
    """Tests the comparison operators of the Student class."""
    # Create some test students
    student1 = Student("Alice", 3)
    student2 = Student("Bob", 3)
    student3 = Student("Alice", 3)

    # Test equality
    print("Testing equality:")
    print(f"student1 == student2: {student1 == student2}")  # Should be False
    print(f"student1 == student3: {student1 == student3}")  # Should be True

    # Test less than
    print("\nTesting less than:")
    print(f"student1 < student2: {student1 < student2}")    # Should be True
    print(f"student2 < student1: {student2 < student1}")    # Should be False

    # Test greater than or equal to
    print("\nTesting greater than or equal to:")
    print(f"student1 >= student2: {student1 >= student2}")  # Should be False
    print(f"student2 >= student1: {student2 >= student1}")  # Should be True
    print(f"student1 >= student3: {student1 >= student3}")  # Should be True

if __name__ == "__main__":
    main()
