#Function : block of code, call whenever we want

def greet():
  print("Welcome to Engineering Life")

greet()
greet()

def add(a:int, b:int=10) -> int:
  return a + b

print(add(10, 20))
print(add(10))