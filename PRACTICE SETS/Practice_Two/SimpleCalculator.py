# Taking two numbers from user and then performing operation

num1 = int(input("Enter the first number here: "))
num2 = int(input("Enter the second number here: "))

print("First Number:", num1)
print("Second Number:", num2)

print(
    "Menu:-\nFor Addition + \nFor Subtraction - \nFor Multiplication *\nFor Division /\nFor Finding Remainder %"
)

operator = input("Enter operator (+, -, *, /, %): ")

match operator:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            print("Result:", num1 / num2)
    case "%":
        if num2 == 0:
            print("Error: Modulo by zero is not allowed!")
        else:
            print("Result:", num1 % num2)
    case _:
        print("Invalid Input!")
