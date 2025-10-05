#print("hello, Python! Today is 22/09/2025.")

#x, y, z = ["orange", "banana", "avocado"]
#print(x,y,z)

#x = "python "
#y = "is "
#z = "awesome"

#print(x + y + z)

#X = 5
#y = 10
#print(X + y)


#x = "Eddy"

#def surname():
 #   x = "Chua"
 #   print("My surname is " + x)
#surname()
#print("My first name is " + x)

#name = "Edd" 
#age = 10 
#print(type(age))
#language = "python" 
#print ("My name is " + name + ", I am " + str(age) + " years old, and I am learning " + language)

#print(f"My name is {name}, I am {age} years old, and I am learning {language}.")

#for s in "banana":
 #   print(s)

# Q1. Strings & Integers
# Create two variables:
#   - name (your name)
#   - year_of_birth (an integer)
# Write a program that prints:
# "Hello, my name is <name>. I was born in <year_of_birth>."
name = "Edd"
year_of_birth = 2013
#print("Hello, my name is " + name + ". I was born in " + str(year_of_birth) + ".")
print(f"Hello, my name is {name}. I was born in {year_of_birth}.")

# Q2. Lists
# Create a list of 3 favorite foods.
# Print the second item in the list.

favs = ["Omena","Sembe","Waba"]
print(favs[1])

# Q3. Dictionaries
# Create a dictionary called student with keys: name, age, and grade.
# Print the values in one sentence. Example:
# "Edd is 10 years old and in Grade 4."

student = {"name": "Edd", "age": 10, "grade": 4}
print(f"{student['name']} is  {student['age']}  years old and in Grade {student['grade']}.")