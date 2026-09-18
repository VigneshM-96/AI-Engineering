#List Comprehension : shorter and more readable syntax to create new list.

#noramy way
squares = []
for i in range(1, 6):
  squares.append(i**2)
print(squares)

#by list Comprehension
squares = [i**2 for i in range(1, 6)]
print(squares)