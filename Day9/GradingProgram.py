student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}





for key, value in student_scores.items(): 
    if value < 70:
        student_grades[key] = "Failed"
    elif value > 70 and value < 80:
        student_grades[key] = "Acceptable"
    elif value > 80 and value < 90: 
        student_grades[key] = "Exceeds expectation"
    else: 
        student_grades[key] = "Outstanding performance!" 


print(student_grades)