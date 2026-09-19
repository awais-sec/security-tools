import os

# Ask for student name and marks
name = input("Enter the student's name: ")
marks = int(input("Enter the marks out of 100: "))

# Check if marks are exactly 100
if marks == 100:
    print(f"Great job, {name}! Marks are 100. Program continues...")
else:
    print("Marks are less than 100. Opening CMD...")
    os.system("start cmd")  # This opens CMD
