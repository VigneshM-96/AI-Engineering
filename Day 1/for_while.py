#Python loops

#reverse 10 to 1
for i in range(10, 0, -1):
  print(i)

#store elements until stop
store = []
while True:
  user_input = input("store something :")
  if user_input != "stop":
    store.append(user_input)
  else:
    print(store)
    break