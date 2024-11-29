def NumberOfStudent():
    return int(input("Number of students: "))

def NumberOfCourse():
    return int(input("Number of courses: "))

def InputStudentInfo(studentList: list, studentNumber: int):
    for i in range(studentNumber):
        studentInfo = {
            "ID": input("Input student ID: "),
            "Name": input("Input student name: "),
            "DoB": input("Input student DoB: ")
        }
        studentList.append(studentInfo)

def InputCourseInfo(courseList: list, courseNumber: int):
    for i in range(courseNumber):
        courseInfo = {
            "ID": input("Input course ID: "),
            "Name": input("Input course name: "),
            "Mark": {}
        }
        courseList.append(courseInfo)

def InputStudentMark(courseList: list, studentList: list):
    print("This is course list:")
    for course in courseList:
        print(f"ID: {course.get('ID')}, Name: {course.get('Name')}")
    
    selectedCourseID = input("Input ID of the course you want to update marks for: ")
    selectedCourse = None
    
    for course in courseList:
        if selectedCourseID == course.get('ID'):
            selectedCourse = course
            break
    
    if (selectedCourse == None):
        print("Invalid course ID")
        return
    else:
        print(f"You chose {selectedCourse.get('Name')} to update marks.")
    
    for student in studentList:
        selectedCourse['Mark'][student.get('ID')] = {
            "Name": student.get('Name'),
            "Mark": float(input(f"Input mark for {student.get('Name')}: "))
        }

def PrintListCourse(courseList: list):
    print("This is course list:")
    for course in courseList:
        print(f"ID: {course.get('ID')}, Name: {course.get('Name')}")

def PrintStudentList(studentList: list):
    print("This is student list:")
    for student in studentList:
        print(f"ID: {student.get('ID')}, Name: {student.get('Name')}, DoB: {student.get('DoB')}")

def PrintStudentMark(courseList: list):
    print("This is course list:")
    for course in courseList:
        print(f"ID: {course.get('ID')}, Name: {course.get('Name')}")
    
    selectedCourseID = input("Input ID of the course you want to print marks for: ")
    selectedCourse = None
    
    for course in courseList:
        if selectedCourseID == course.get('ID'):
            selectedCourse = course
            break
    
    if (selectedCourse == None):
        print("Invalid course ID")
        return
    else:
        print(f"You chose {selectedCourse.get('Name')} to print marks.")
    
    for key, value in selectedCourse.get('Mark', {}).items(): 
        print(f"Student ID: {key}, Student Name: {value['Name']}, Mark: {value['Mark']}")
          
        
studentList = []
courseList = []
studentNumber=0
courseNumber=0
while True:
    print("List of possible actions:\n \
        1. Input number of students in a class\n \
        2. Input student information\n \
        3. Input number of courses\n \
        4. Input course information\n \
        5. Select a course, input marks for student\n \
        6. Print course list\n \
        7. Print student list\n \
        8. Print student marks\n \
        9. Exit")
    action = int(input("Choose your action: "))
    
    if action == 1:
        studentNumber = NumberOfStudent()
    elif action == 2:
        InputStudentInfo(studentList, studentNumber)
    elif action == 3:
        courseNumber = NumberOfCourse()
    elif action == 4:
        InputCourseInfo(courseList, courseNumber)
    elif action == 5:
        InputStudentMark(courseList, studentList)
    elif action == 6:
        PrintListCourse(courseList)
    elif action == 7:
        PrintStudentList(studentList)
    elif action == 8:
        PrintStudentMark(courseList)
    elif action == 9:
        break
    else:
        print("Invalid choice")

    
    
    
    