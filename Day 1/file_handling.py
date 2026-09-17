#File Handling : create, read, write and delete files

with open("test.txt", "w") as file:
  print("File Created, Successfully.")
  file.write("Hey, AI Engineer.")
  file.close()

with open('test.txt', "r") as file:
  print(file.read())
  file.close()