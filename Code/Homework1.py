choice = True
student_list = []
student_details = {}

def add_student(name, id):
    student_details ={"name: " + name, "id: " + id}
    student_list.append(student_details)


def saveToFile(student):
    try:
        file = open("student.txt", 'a')
        file.write(student + "\n")
        print("Added\n")
        file.close();

    except Exception:
        print("Could not save file")


def readFromFile():
    try:
        def add_student(student):
            student_list.append(student)
        file = open('student.txt', "r")
        for student in file.readlines():
            print(student)
        file.close()

    except:
        print("Could not read from file")


def printStudentList():
    for student in student_list:
        print(student)

while choice:
    choice= input("Do you want to add a student? Press Y to continue, N to exit. ")
    if choice == "Y":
        student_name = input("Enter a name: ")
        student_id = input("Enter an id: ")
        add_student(student_name, student_id)
        saveToFile(student_name)

    if choice == "N":
        printStudentList()
        readFromFile()
        break

    else:
        choice = True
        continue



