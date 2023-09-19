print("task 2.1")
N = int(input("Enter the number of schoolchildren: "))
K = int(input("Enter the number of tangerines: "))
tangerines_per_student = K // N
remaining_tangerines = K % N
print(f"Each student will get {tangerines_per_student} whole tangerines.")
print(f"{remaining_tangerines} whole tangerines will remain in the basket.")

print("\ntask 2.2")
number = int(input("Enter a four-digit number: "))
if 1000 <= number <= 9999:
    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    ones = number % 10

    print(f"Thousands digit: {thousands}")
    print(f"Hundreds digit: {hundreds}")
    print(f"Tens digit: {tens}")
    print(f"Ones digit: {ones}")
else:
    print("Please enter a valid four-digit number.")

print("\ntask 2.3")
population = int(input("Enter the population of the universe: "))
if population % 2 == 0:
    survivors = population // 2
else:
    survivors = (population + 1) // 2
print(f"Number of survivors: {survivors}")

print("\ntask 2.4")
n = int(input("Enter a number: "))
result = n << 1
if result == 0:
    print("Warning: The result is zero.")
else:
    print(f"The result of {n} << 1 is: {result}")

print("\ntask 2.5")
try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    operation = input("Please choose the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '/':
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Please choose from +, -, *, /.")

except ValueError:
    print("Error")
except Exception as e:
    print(e)
