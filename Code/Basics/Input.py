student_list = []
student = {}
student_name = input("Enter student name: ")
student_id = input("Enter student id: ")

def addStudent(student_name, student_id=0):
    student = {"name": student_name, "student_id": student_id}
    student_list.append(student)

addStudent(student_name,student_id)
print(student_list)