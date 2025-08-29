# grade based on the score:
# If score > 90: Grade A
# If score > 80: Grade B
# If score > 70: Grade C
# If score > 60: Grade D
# Else: Grade F
# Use nested if-else.

input_score = 88
grade = "NA"

if input_score > 90:
    grade = "GradeA"
elif input_score > 80:
    grade = "GradeB"
elif input_score > 70:
    grade = "GradeC"
elif input_score > 60:
    grade = "GradeD"
else:
    grade = "GradeF"        

print(f"Score- {input_score}, {grade}")
