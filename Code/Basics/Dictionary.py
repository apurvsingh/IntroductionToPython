student = {
    "name" : "Homer",
    "age" : 45
}

all_students = [
    {'name': "Homer", "age" : 45},
    {'name': "Bart", "age" : 10}
]

if student["name"] == "Homer":
    print('Homer found!')


for students in all_students:
    if students["name"]=="Bart":
        print(f"{students} found!!")

try:
    last_name = student["last_name"]
except KeyError:
    print("Wrong ke entered")