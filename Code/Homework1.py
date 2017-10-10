choice = True
student_list = []
student_details = {}
def add_student(name, id):
    student_details ={"name: " + name, "id: " + id}
    student_list.append(student_details)

def printStudentList():
    for student in student_list:
        print(student)

while choice:
    choice= input("Do you want to add a student? Press Y to continue, N to exit. ")
    if choice == "Y":
        student_name = input("Enter a name: ")
        student_id = input("Enter an id: ")
        add_student(student_name, student_id)

    if choice == "N":
        printStudentList()
        break

    else:
        choice = True
        continue
