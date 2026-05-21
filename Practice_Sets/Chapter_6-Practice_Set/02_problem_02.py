#Write a program to find out whether a student has passed or failed if it requires a total fo 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as input from the user.
# taking input from the user for marks in three subjects
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))      

# calculating total marks and percentage
total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100

# checking if the student has passed or failed
if percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("The student has passed.", percentage)
else:
    print("The student has failed.", percentage)