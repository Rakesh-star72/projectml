# Student Grade Calculator

# Take student name
name = input("Enter student name: ")

# Take marks (0-100)
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Validate marks
if (0 <= mark1 <= 100) and (0 <= mark2 <= 100) and (0 <= mark3 <= 100):

    # Calculate total and average
    total = mark1 + mark2 + mark3
    average = total / 3

    # Assign grade
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Display result
    print("\n--- Result ---")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)

else:
    print("Error: Marks should be between 0 and 100.")