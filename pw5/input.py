from domains.student import Student
from domains.course import Course
from output import SelectCourse
import math

def InputNumber(name):
    return int(input(f"Input number {name}: "))
def InputStudentInfo(studentList:list, studentNumber:int):
    studentNumber=InputNumber("of student")
    if studentNumber > 0:
            for i in range(studentNumber):
                print(f"Input info for student {i + 1}:")
                temp = Student()
                studentList.append(temp)
                with open('C:\\Users\\namfg\\Documents\\GitHub\\pp2024\\pw5\\students.txt', 'a') as file:
                    file.write(f"ID: {temp.ID},Name: {temp.Name},DOB: {temp.Dob}\n")
    else:
        print("Please set the number of students first.")

def InputCourseInfo(courseList:list,courseNumber:int):
    courseNumber=InputNumber("of course")
    if courseNumber > 0:
            for i in range(courseNumber):
                print(f"Input info for course {i + 1}:")
                temp=Course()
                courseList.append(temp)
                with open('C:\\Users\\namfg\\Documents\\GitHub\\pp2024\\pw5\\courses.txt', 'a') as file:
                    file.write(f"ID: {temp.ID},Name: {temp.Name},Credit: {temp.Credits}\n")
    else:
        print("Please set the number of courses first.")

def InputMark(courseList:list, studentList:list):
    selectedCourse = SelectCourse(courseList, studentList)
    if selectedCourse:
        for student in studentList:
            raw_mark = float(input(f"Input mark for {student.Name}: "))
            rounded_mark = math.floor(raw_mark * 10) / 10
            selectedCourse._Mark[student.ID] = {"Name": student.Name, "Mark": rounded_mark}
            student.Courses[selectedCourse.ID] = {"Name": selectedCourse.Name, "Mark": rounded_mark, "Credits": selectedCourse.Credits}
            
            with open('C:\\Users\\namfg\\Documents\\GitHub\\pp2024\\pw5\\marks.txt', 'a') as file:
                file.write(f"Course: {selectedCourse.Name},Student name: {student.Name},Mark:{rounded_mark}\n")
            
    for student in studentList:
        student.CalculateGPA()
        

        