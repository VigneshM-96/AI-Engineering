#Nested List and dictionary : list inside dictionay or dictionay inside list

student = {
  "name": "Vignesh",
  "courses": ["python", "java"],
  "scores": [98, 90]
}

print(student["courses"][1])
student["scores"].append(100)

print(student)

company = {
  "HR" : {
    "name": "nandhini",
    "age": 25
  },

  "Tech": {
    "name": "Vignesh",
    "age": 22
  }
}

print(company.get("Tech", {}))
print(company.get("Tech", {}).get("name", "none"))