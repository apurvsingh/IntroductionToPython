student_list = []


class Student:
    def __init__(self, name, id=0):
        student_details = {"name": name, " id": id}
        student_list.append(student_details)

student = Student("Apurv", 22)
print(student_list)