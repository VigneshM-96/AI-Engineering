#student processor

students = [
  {"id":100, "name":"venkatesh", "marks":[14, 7, 10]},
  {"id":101, "name":"vetriselvan", "marks":[90, 90, 96]},
  {"id":102, "name":"vignesh", "marks":[93, 100, 96]},
  {"id":103, "name":"kumar", "marks":[34, 55, 30]},
]

#High marks student

max = 0
min = sum(students[0]["marks"])
for s in students:
  total = sum(s["marks"])
  if total > max:
    max = total
    student = s["name"]
  if total <= min:
    min = total
    student_l = s["name"]
print(f"High mark student : {student} with mark {max}")
print(f"Low mark student : {student_l} with mark {min}")
