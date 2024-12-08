class methodManager:
    @staticmethod
    def addToList(obj, list):
        list.append(obj)
    
    @staticmethod
    def printList(list):
        for obj in list:
            print(obj)
    
    @staticmethod
    def _inputQuantity():
        return int(input("Enter the quantity you want: "))

    @staticmethod
    def InputQuantity():
        return methodManager._inputQuantity()
class Init:
    def __init__(self):
        self.Name=input("Input student name: ")
        self.ID=input("Input student ID: ")
        
class Student(Init):
    def __init__(self):
        super().__init__()
        self.Dob=input("Input student DoB: ")
    
    def AddToList(self, studentList: list):
        studentList.append(self)
        
    def __str__(self):
        return f"ID: {self.ID}, Name: {self.Name}, DoB: {self.Dob}"

class Course(Init):
    def __init__(self):
        super().__init__()
        self.Mark={}
        
    def __str__(self):
        return  f"ID: {self.ID}, Name: {self.Name}"
    
    def InputMark(self, studentList:list):
        for student in studentList:
            self.Mark[student.ID] = {
                "Name": student.Name,
                "Mark": float(input(f"Input mark for {student.Name}: "))
            }
    def PrintMark(self):
        for key,value in self.Mark.items():
            print(f"Id: {key}, Name: {value['Name']}, Mark: {value['Mark']}")

studentNumber=""
courseNumber=""
studentList=[]
courseList=[]
    
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
        studentNumber=methodManager.InputQuantity()
    elif action == 2:
        if studentNumber>0:
            for i in range(studentNumber):
                studentList.append(Student())
        else:
            print("You don't have number of student")
    elif action == 3:
        courseNumber=methodManager.InputQuantity()
    elif action == 4:
        if courseNumber>0:
            for i in range(courseNumber):
                courseList.append(Course())
        else:
            print("You don't have number of course")
    elif action == 5:
        if len(studentList) == 0 or len(courseList) == 0:
            print("Your student list or course list is empty")
        else:    
            methodManager.printList(courseList)
            selectedID = input("Input the course ID of the course you want to update mark: ")
            inList=0
            for course in courseList:
                if selectedID == course.ID:
                    inList=1
                    course.InputMark(studentList)
            if inList==0:
                print("Invalid ID")
            
    elif action == 6:
        if len(courseList) == 0:
            print("Your course list is empty")
        else:
            methodManager.printList(courseList)
    elif action == 7:
        if len(studentList) == 0:
            print("Your student list is empty")
        else:
            methodManager.printList(studentList)
    elif action == 8:
        if len(studentList) == 0 or len(courseList) == 0:
            print("Your student list or course list is empty")
        else:
            methodManager.printList(courseList)
            selectedID = input("Input the course ID of the course you want to print mark: ")
            inList=0
            for course in courseList:
                if selectedID == course.ID:
                    if len(course.Mark)!=0:
                        inList=1
                        course.PrintMark()
                        
                    else:
                        print("You haven't input mark for this course")
                        break
            if inList==0:
                print("Invalid ID")
    elif action == 9:
        break
    else:
        print("Invalid choice")

    
    

    