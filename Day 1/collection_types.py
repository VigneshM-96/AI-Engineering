#All are collection data types that means store more than one value.
#Those can be differentiate by ordered, mutable, allowing duplicates

#1. List with common operations
my_list = ["apple", 10, True, 40.2]
my_list.append(100)
my_list[0] = "banana"
print(my_list)
del my_list

#2. Tuple with common operations
test_tuple = 1,2
print(test_tuple)
print(test_tuple[0])
print(len(test_tuple))

#3. Sets with common operations
user_id = {100, 101, 102}
user_id.add(103)
print(user_id)

#4. Dictionary with common operations
employee_detail = {
  "name": "Vignesh M",
  "role": "AI Engineer",
  "skills": ["Python", "SQL"]
}

employee_detail["role"] = "Chief AI Officer"
employee_detail["salary"] = 80000
print(employee_detail["name"])