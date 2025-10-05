print ("1 - Addition")
print ("2 - Subtraction")
print ("3 - Multiplication")
print ("4 - Division")

choice = input("Enter a choice: ")
num1 = input("Enter your first number: ")
num2 = input ("Enter your second number: ")

if choice == "1":
    print (num1 + num2)
elif choice == "2":
    print (num1 - num2)
elif choice == "3":
    print (num1 * num2)
elif choice == "4":
    print (num1 / num2)

else:
    print ("Invalid input")
# Simple calculator program
