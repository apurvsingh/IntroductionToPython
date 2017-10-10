student_list = []


class Student:

    schoolName = "SJA"
    def __init__(self, name, id=0):
        self.name = name
        self.id = id
        student_list.append(self)
        print(self.getSchool())

    def __str__(self):
        return "This overrides the memory instance message for student :" + self.name

    def getNameCapitalize(self):
        return self.name.capitalize()

    def getSchool(self):
        return self.schoolName

student = Student("Apurv", 22)

print(student)
print(Student.schoolName)