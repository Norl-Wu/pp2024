from domains.init import Init
import math

class Course(Init):
    def __init__(self):
        super().__init__()
        self._Mark = {}
        self.Credits = int(input("Input course credits: "))

    def __str__(self):
        return f"ID: {self.ID}, Name: {self.Name}, Credits: {self.Credits}"

    def InputMark(self, studentList: list):
        for student in studentList:
            raw_mark = float(input(f"Input mark for {student.Name}: "))
            rounded_mark = math.floor(raw_mark * 10) / 10
            self._Mark[student.ID] = {"Name": student.Name, "Mark": rounded_mark}
            student.Courses[self.ID] = {"Mark": rounded_mark, "Credits": self.Credits}

    def PrintMark(self):
        for key, value in self._Mark.items():
            print(f"ID: {key}, Name: {value['Name']}, Mark: {value['Mark']}")