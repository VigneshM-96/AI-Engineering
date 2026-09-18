#range - mainly used in for loop to control sequence. this is known as lazy evaluation.

print(list(range(1,10, 2)))

#syntax : range(start, stop, step)

items = ["laptop", "mouse", "keyboard"]
for i in range(len(items)):
  print(f"Item {i} : {items[i]}")