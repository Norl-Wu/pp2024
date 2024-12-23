import math
import numpy as np
from domains.student import Student
from domains.course import Course
from input import *
from output import *
from curses import wrapper

def SortStudentsByGPA(studentList):
    
    return sorted(studentList, key=lambda s: s.GPA, reverse=True)

studentNumber = 0
courseNumber = 0
studentList = []
courseList = []

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    
wrapper(main)
Decompress()

while True:
    print("\nList of possible actions:\n \
        1. Input student information\n \
        2. Input course information\n \
        3. Select a course and input marks\n \
        4. Print course list\n \
        5. Print student list\n \
        6. Print student marks\n \
        7. Sort student list by GPA\n \
        8. Exit"
        )
    action = int(input("Choose your action: "))

    if action == 1:
        InputStudentInfo(studentList,studentNumber)
    elif action == 2:
        InputCourseInfo(courseList, courseNumber)
    elif action == 3:
        InputMark(courseList, studentList)
    elif action == 4:
        if not courseList:
            print("Your course list is empty")
        else:
            PrintList(courseList)
    elif action == 5:
        if not studentList:
            print("Your student list is empty")
        else:
            PrintList(studentList)
    elif action == 6:
        PrintMark(courseList, studentList)
    elif action == 7:
        studentList = SortStudentsByGPA(studentList)
        print("Student list sorted by GPA:")
        PrintList(studentList)
    elif action == 8:
        CompressFiles()
        break
    else:
        print("Invalid choice.")
