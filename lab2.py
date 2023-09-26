print("task 1")
try:
    number = input("Enter a four-digit number: ")

    if len(number) != 4 or not number.isdigit():
        raise ValueError("The input must be a four-digit number")

    first_digit = int(number[0])
    second_digit = int(number[1])
    third_digit = int(number[2])
    fourth_digit = int(number[3])

    if first_digit + fourth_digit == second_digit - third_digit:
        print("YES")
    else:
        print("NO")

except ValueError as e:
    print(e)

print("task 2\n")
try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Access allowed")
    else:
        print("Access denied")

except ValueError:
    print("Please enter a valid age")

print("task 3\n")
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    if b - a == c - b:
        print("YES")
    else:
        print("NO")

except ValueError:
    print("Please enter valid numbers.")

print("task 4\n")
try:
    x1 = int(input("Enter the column number for the first cell (1 to 8): "))
    y1 = int(input("Enter the row number for the first cell (1 to 8): "))
    x2 = int(input("Enter the column number for the second cell (1 to 8): "))
    y2 = int(input("Enter the row number for the second cell (1 to 8): "))

    if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
        if x1 == x2 or y1 == y2:
            print("YES")
        else:
            print("NO")
    else:
        print("Coordinates should be between 1 and 8.")

except ValueError:
    print("Please enter valid numbers between 1 and 8.")


print("task 5\n")
try:
    x1 = int(input("Enter the column number for the first cell (1 to 8): "))
    y1 = int(input("Enter the row number for the first cell (1 to 8): "))
    x2 = int(input("Enter the column number for the second cell (1 to 8): "))
    y2 = int(input("Enter the row number for the second cell (1 to 8): "))

    if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            print("YES")
        else:
            print("NO")
    else:
        print("Coordinates should be between 1 and 8.")

except ValueError:
    print("Please enter valid numbers between 1 and 8.")


print("task 6\n")
try:
    a = int(input())
    b = int(input())
    c = int(input())

    numbers = [a, b, c]
    numbers.sort()

    average = (numbers[0] + numbers[2]) / 2
    print(average)
except ValueError:
    print("Please enter valid integers.")

print("task 7\n")
try:
    month = int(input())

    if month < 1 or month > 12:
        raise ValueError("Invalid month number.")

    if month in [1, 3, 5, 7, 8, 10, 12]:
        print(31)
    elif month == 2:
        print(28)
    else:
        print(30)
except ValueError as e:
    print(e)

print("task 8\n")
try:
    weight = int(input())
    if weight <= 60:
        print("Light weight")
    elif weight <= 64:
        print("First welterweight")
    else:
        print("Welterweight")
except ValueError as e:
    print(e)

print("task 9\n")
password = input()
confirmation = input()

if password == confirmation:
    print("Password accepted")
else:
    print("Password not accepted")

print("task 10\n")
try:
    number = int(input())
    
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Please enter a valid integer.")

print("task 11\n")
try:
    a = int(input())
    b = int(input())

    print(min(a, b))
except ValueError:
    print("Please enter valid integers.")

print("task 12\n")
try:
    age = int(input())

    if age <= 13:
        print("childhood")
    elif age <= 24:
        print("youth")
    elif age <= 59:
        print("maturity")
    else:
        print("old age")
except ValueError:
    print("Please enter a valid age.")

print("task 13")
try:
    a = int(input())
    b = int(input())
    c = int(input())

    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Versatile")
except ValueError:
    print("Please enter valid side lengths.")
