student_scores = {
    "harry": 30,
    "Draco": 79,
    "Neville": 89,
    "Rishav": 12
}
student_grades = {}


for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"



print(student_grades)
