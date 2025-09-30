#a = 33
#b = 33
#if b > a:
#  print("b is greater than a")
#elif a == b:
#  print("a and b are equal")


#a = 200
#b = 33
#if b > a:
#  print("b is greater than a")
#elif a == b:
#  print("a and b are equal")
#else:
 # pass

#PYTHON MATCH STATEMENT

day = 40
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Invalid day")


day = 8
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
  case _:
    print("Not in a week!")