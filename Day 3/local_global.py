
#local vs global variabls - local variable only allows to use inside the function but global variable can be use anywhere.

#local variable
import venv
def my_func():
  local_msg = "Im local one"
  print(local_msg)

my_func()
try:
  print(local_msg)
except:
  print("Something Error.")

#global variable
global_msg = "Im global one"
def my_func():
  print(global_msg)

my_func()
try:
  print(global_msg)
except:
  print("Something Error.")

#modify global
counter = 10
def counting():
  global counter
  counter += 10
  print(counter)
counting()
print(counter)