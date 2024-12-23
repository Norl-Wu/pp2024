from domains.init import Init
import math

class Course(Init):
    def __init__(self):
        super().__init__()
        self._Mark = {}
        self.Credits = int(input("Input course credits: "))

    def __str__(self):
        return f"ID: {self.ID}, Name: {self.Name}, Credits: {self.Credits}"

    def PrintMark(self):
        for key, value in self._Mark.items():
            print(f"ID: {key}, Name: {value['Name']}, Mark: {value['Mark']}")