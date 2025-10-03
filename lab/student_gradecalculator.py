# Student Grade Calculator

# Step 1: Input marks for 5 subjects
marks = []
for i in range(5):
    while True:
        try:
            score = float(input(f"Enter marks for subject {i+1}: "))
            if 0 <= score <= 100:  # ensure marks are within 0-100
                marks.append(score)
                break
            else:
                print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Step 2: Calculate total and percentage
total = sum(marks)
percentage = (total / 500) * 100   # total max marks = 5*100

# Step 3: Decide grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Step 4: Display results
print("\n--- Student Result ---")
print("Total Marks:", total)
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
