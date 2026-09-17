name = "Vignesh"
skills = ["python", "sql", "flutter"]

#Conditional statement or control flow
if len(skills) > 2 and "python" in skills:
  salary = 30000
elif len(skills) > 1:
  salary = 18000
else:
  salary = None
  
print(f"Salary : {salary}")