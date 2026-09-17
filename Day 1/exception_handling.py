#Exception handling : handling the error scenario
#Core structure : try, except, else, finally

try:
  with open("secret_text.txt", "r") as file:
    data = file.read()
except FileNotFoundError:
  print("Oops file was not exist!")

#raising own Exception
def set_age(age):
  if age < 0:
    raise ValueError("Age must be positive")
  print(f"Age set to {age}")

try:
  set_age(-10)
except ValueError as e:
  print(f"Facing Error : {e}")