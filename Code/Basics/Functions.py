student_list = []

def addStudent(name, id=0):
    student = {"name": name, "student_id": id}
    student_list.append(student)


def printStudentList():
    for student in student_list:
        print("The name of the student is " + student["name"]+ " and \nid = " + str(student["student_id"]))


addStudent("Bruce")

printStudentList()


def variable_args(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])

variable_args("Apurv", description="Liverpool fan", feedback=None)