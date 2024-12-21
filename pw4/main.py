import math
import numpy as np
from domains.student import Student
from domains.course import Course
from input import InputNumber
from output import PrintList
from curses import wrapper

def SelectCourse(courseList, studentList):
    if len(studentList) == 0 or len(courseList) == 0:
        print("Your student list or course list is empty")
        return None
    PrintList(courseList)
    selectedID = input("Input the course ID of the course you want to choose: ")
    for course in courseList:
        if selectedID == course.ID:
            return course
    print("Course not found")
    return None

def SortStudentsByGPA(studentList):
    for student in studentList:
        student.CalculateGPA()
    return sorted(studentList, key=lambda s: s.GPA, reverse=True)

studentNumber = 0
courseNumber = 0
studentList = []
courseList = []

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    
wrapper(main)

while True:
    print("\nList of possible actions:\n \
        1. Input number of students in a class\n \
        2. Input student information\n \
        3. Input number of courses\n \
        4. Input course information\n \
        5. Select a course and input marks\n \
        6. Print course list\n \
        7. Print student list\n \
        8. Print student marks\n \
        9. Sort student list by GPA\n \
        10. Exit")
    action = int(input("Choose your action: "))

    if action == 1:
        studentNumber = InputNumber("of students: ")
    elif action == 2:
        if studentNumber > 0:
            for i in range(studentNumber):
                print(f"Input info for student {i + 1}:")
                studentList.append(Student())
        else:
            print("Please set the number of students first.")
    elif action == 3:
        courseNumber = InputNumber("of courses: ")
    elif action == 4:
        if courseNumber > 0:
            for i in range(courseNumber):
                print(f"Input info for course {i + 1}:")
                courseList.append(Course())
        else:
            print("Please set the number of courses first.")
    elif action == 5:
        selectedCourse = SelectCourse(courseList, studentList)
        if selectedCourse:
            selectedCourse.InputMark(studentList)
    elif action == 6:
        if not courseList:
            print("Your course list is empty")
        else:
            PrintList(courseList)
    elif action == 7:
        if not studentList:
            print("Your student list is empty")
        else:
            PrintList(studentList)
    elif action == 8:
        selectedCourse = SelectCourse(courseList, studentList)
        if selectedCourse:
            selectedCourse.PrintMark()
    elif action == 9:
        studentList = SortStudentsByGPA(studentList)
        print("Student list sorted by GPA:")
        PrintList(studentList)
    elif action == 10:
        break
    else:
        print("Invalid choice.")
