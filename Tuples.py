#thistuple = ("apple", "banana", "cherry")
#print(thistuple[1])

#thistuple = ("apple", "banana", "cherry")
#print(thistuple[-1])

#thistuple = ("apple", "banana", "cherry")
#if "apple" in thistuple:
 # print("Yes, 'apple' is in the fruits tuple")

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

#x = ("mercedes", "ferrari", "Mclaren")
#y = list(x)
#y[1] = "Haas"
#x = tuple(y)
#print(x)

import datetime



#x = datetime.datetime.now()
#print(x)

class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()


class Computer:
  def config(self):
    print("i5, 16GB, 1TB")

com1 = Computer()
print(type(com1))
Computer.config(com1)
com1.config()