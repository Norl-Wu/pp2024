from domains.course import Course
import zipfile
import os

def CompressFiles():
    with zipfile.ZipFile('C:\\Users\\namfg\\Documents\\GitHub\\pp2024\\pw5\\students.dat', 'w') as zipf:
        zipf.write('C:\\Users\\namfg\\Documents\\GitHub\\pp2024\\pw5\\marks.txt')
        zipf.write('C:\\Users\\namfg\\Documents\\GitHub\\pp2024\\pw5\\students.txt')
        zipf.write('C:\\Users\\namfg\\Documents\\GitHub\\pp2024\\pw5\\courses.txt')


def Decompress():
    if os.path.exists('C:\\Users\\namfg\\Documents\\GitHub\\pp2024\\pw5\\students.dat'):
        with zipfile.ZipFile('C:\\Users\\namfg\\Documents\\GitHub\\pp2024\\pw5\\students.dat', 'r') as zipf:
            zipf.extractall()

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

def PrintList(lst):
    for item in lst:
        print(item)
        
def PrintMark(courseList:list, studentList:list):
    selectedCourse = SelectCourse(courseList, studentList)
    if selectedCourse:
        selectedCourse.PrintMark()

