student_names = []
student_names.append("Apurv")
student_names.append("Homer")
student_names.append("Rupin")
student_names.append("Peter")

print(student_names[-1])
print("Homer" in student_names)
print(len(student_names))
print(student_names[1: -1])

for name in student_names:
    print(f"Student name:{name}")

for index in range(10):
    print(f"The index is {index}")

for index in range(2,10,3):
    print(f"The index value is {index}")

x = 0
while(x < 10):
    print(f"{x} is less than 10")
    x+=1