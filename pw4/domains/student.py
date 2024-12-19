from domains.init import Init
import math
import numpy as np

class Student(Init):
    def __init__(self):
        super().__init__()
        self.Dob = input("Input student DoB: ")
        self.Courses = {}
        self.GPA = 0

    def AddToList(self, studentList: list):
        studentList.append(self)

    def CalculateGPA(self):
        if self.Courses:
            marks = np.array([info["Mark"] * info["Credits"] for info in self.Courses.values()])
            credits = np.array([info["Credits"] for info in self.Courses.values()])
            self.GPA = round(sum(marks) / sum(credits), 2) if sum(credits) > 0 else 0

    def __str__(self):
        return f"ID: {self.ID}, Name: {self.Name}, DoB: {self.Dob}, GPA: {self.GPA}"