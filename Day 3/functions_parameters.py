#Functions : an block of code, create once use many times

#Function Creation
def greet():
  print("Hello, Team!")

#Function Calling
greet()
greet()
greet()

def add(a:int, b:int) -> int: #parameter
  return a + b

print(add(10, 10)) #arguments
print(add(14, 16))