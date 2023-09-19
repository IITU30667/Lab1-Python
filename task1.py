print("task 1.1")
sequence = [4, 8, 15, 16, 23, 42]
final = ' '.join(map(str, sequence))
print(final)

print("\ntask 1.2")
for n in sequence:
    print(n)

print("\ntask 1.3")
try:
    n = int(input("Enter the first number: "))

    print(n)
    print(n+1)
    print(n+2)
except Exception as e:
    print(e)

print("\ntask 1.4")
try:
    num1 = int(input("first integer: "))
    num2 = int(input("second integer: "))
    num3 = int(input("third integer: "))
    total = num1 + num2 + num3
    print(total)
except Exception as e:
    print(e)

print("\ntask 1.5")
try:
    edge_length = float(input("Enter the length: "))
    volume = edge_length ** 3
    surface_area = 6 * (edge_length ** 2)
    print(f"Volume: {volume}")
    print(f"Surface area: {surface_area}")
except Exception as e:
    print(e)