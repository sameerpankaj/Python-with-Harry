#Write a program to calculate the grade of a student from his marks from the following scheme: 90-100: Ex, 80-89: A, 70-79: B, 60-69: C, 50-59: D, <50: F. Take marks as input from the user.
# taking input from the user for marks
obtained_marks = int(input("Enter marks: ")) 
# calculating the grade based on the marks
if obtained_marks >= 90 and obtained_marks <= 100:
    grade = "Ex"  
elif obtained_marks >= 80 and obtained_marks < 90:
    grade = "A"   
elif obtained_marks >= 70 and obtained_marks < 80:
    grade = "B"
elif obtained_marks >= 60 and obtained_marks < 70:
    grade = "C"
elif obtained_marks >= 50 and obtained_marks < 60:
    grade = "D"
elif obtained_marks < 50:
    grade = "F" 
else:
    print("Invalid marks entered.")

print("Your grade is:", grade)