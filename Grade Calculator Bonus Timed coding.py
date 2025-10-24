#Purpose of this program
print("Grade Calculator")

# initialize total
total_earned = 0
total_possible = 0
#ask for user input on number of assignments
num_assignments = int(input("Enter the number of assignments: "))
#loop through each assignment
for i in range(num_assignments):
    earned = float(input(f"points earned for assignment: {i+1}"))
    possible = float(input(f"points possible for assignment: {i+1}"))
    total_earned += earned
    total_possible += possible
#validate input from user 
if total_possible <= 0:
    print("Error: total points must be greater than zero")
    exit()
#calculate percentage
percentage = (total_earned / total_possible) *100

#determin letter grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"
#display result
print(f"/ Final Grade: {grade} ({percentage:.2f}%)")
