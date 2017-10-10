student_list = []


class Student:

    schoolName = "SJA"
    def __init__(self, name, id=0):
        self.name = name
        self.id = id
        student_list.append(self)
        print(self.getSchool())

    def getSchool(self):
        return self.schoolName

    def printSelf(self):
        print(self)


class HighScoolStudent(Student):
    schoolName = "Welham's"
    def getSchool(self):
        return "This is a highSchool student"

    def getParentSchool(self):
        print(super().getSchool())
        schoolName = "Welham's"

    def printSelf(self):
        print(super().printSelf())


student = HighScoolStudent("singh")
student.printSelf()

student1 = Student("Apurv")
student1.printSelf()