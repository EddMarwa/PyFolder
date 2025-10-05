# Demonstrating the use of 'in' with a range object
#r = range(0, 10, 2)
#print(list(r))
#print(6 in r)
#print(7 in r)
#
#for i in range(3):
#    print(i)
#
#python lambda.py
import platform

x = platform.system()
print(x)

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

