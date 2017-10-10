number1 = 20
number2 = 10
stringLiteral = "Batman"
booleanLiteral = True
noneLiteral = None

print(f"Hello my name is {stringLiteral}")

print(int(booleanLiteral))

if number1 == number2:
    print(booleanLiteral)
else:
    print("Joker")

if not number1 - 20:
    print("This is falsy but prints because of the not")

if number2:
    print("Truthy")

if number1 - number2 != 0 and not noneLiteral:
    print("And example executed!")

print("Number1 is bigger") if number2>number1 else print("Number2 is bigger")