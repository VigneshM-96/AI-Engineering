#dictionaly : an key value pair (key is immutable) while value is immutable

#creating
employee_data = {
  "name":"Vignesh M",
  "role":"AI Engineer",
  "age":22
}

#accessing
print(employee_data["name"])

#accessing with safe method
print(employee_data.get("email")) #None
print(employee_data.get("email", "N/A"))

#modifying and adding element
employee_data["location"] = "Chennai"

#updating
employee_data["age"] = 24

#merging
employee_data.update({'status':"Active", 'age':25})

print(employee_data)

#Removing element
del employee_data["location"]
age = employee_data.pop("age") #supports default also
last_item = employee_data.popitem()
employee_data.clear()

car = {
  "name":"Ford",
  "model":"Mustang",
  "year":1964
}

for k, v in car.items():
  print(f"{k} : {v}")

#checking existence
inventory = {
  "chip-1":10,
  "chip-2":20
}

if "chip-1" in inventory and inventory.get("chip-1") > 0:
  print(f"We have chip-1 with qty. {inventory["chip-1"]}")