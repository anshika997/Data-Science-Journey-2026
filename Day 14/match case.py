choice = 2

match choice:
    case 1:
        print("Addition")
    case 2:
        print("Subtraction")
    case 3:
        print("Multiplication")
    case 4:
        print("Division")
    case _:
        print("Invalid choice")

print("-" * 50)

day = 5

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

print("-" * 50)

num = 10

match num:
    case n if n % 2 == 0:
        print("Even")
    case _:
        print("Odd")

print("-" * 50)

x = 5
y = 3
op = "+"

match op:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        print(x / y)
    case _:
        print("Invalid operator")

print("-" * 50)

name = "Anshika"

match name:
    case "Anshika":
        print("Welcome Anshika")
    case "Admin":
        print("Welcome Admin")
    case _:
        print("Unknown user")

print("-" * 50)

print("Match case examples executed successfully")
