
#import json

# some JSON:
#x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:
#print(y["city"])

import time

start = time.time()  # Start timer

# --- Code block you want to measure ---
total = 0
for i in range(1_000_000_000_000_000_000_000_000):
    total += i
# -------------------------------------

end = time.time()  # End timer

print(f"Execution time: {end - start:.5f} seconds")

