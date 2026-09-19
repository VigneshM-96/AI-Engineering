#print vs return

#print simply displays the text but return passes the value to the program.

#using print
def add_print(a, b):
  result = a + b
  print(result)

result = add_print(3, 5)

try:
  print(result + 2)
except TypeError as e:
  print("Something error :",e)

#using return
def add_print(a, b):
  return a + b
result = add_print(3, 5)

try:
  print(result + 2)
except TypeError as e:
  print("Something error :",e)
  