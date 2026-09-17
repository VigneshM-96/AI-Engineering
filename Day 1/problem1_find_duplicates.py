#Finding Duplicates on list

my_list = [19, 10, 12, 19, 11]

dups = []

for i in my_list:

  if my_list.count(i) > 1 and i not in dups:
    dups.append(i)

print(dups)