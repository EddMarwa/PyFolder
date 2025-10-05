print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter a choice (1/2/3/4): ")

# Convert inputs to float for general numeric operations
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if choice == "1":
    print(f"The result is: {num1 + num2}")
elif choice == "2":
    print(f"The result is: {num1 - num2}")
elif choice == "3":
    print(f"The result is: {num1 * num2}")
elif choice == "4":
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input")
