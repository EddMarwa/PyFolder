#functions 
#def fn():
#    print("Hello from functions")
#fn()

#def fn2(fname, lname):
#    print(fname + " " + lname)
#fn2 ("Edd", "Mar")

#def fn3(country = "Kenya"):
 #   print("I am from " + country)

#fn3("tanzania")
#fn3("uganda")
#fn3()
#fn3("rwanda")

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


def tri_recursion(k):
    if k > 0:                     # condition to stop recursion
        result = k + tri_recursion(k - 1)   # function calls itself
        print("Returning:", result)
        return result
    else:
        return 0                   # base case: stop when k == 0

tri_recursion(3)
