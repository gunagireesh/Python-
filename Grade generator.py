def generate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

score = float(input("Enter the score (0-100): "))

if 0 <= score <= 100:
    grade = generate_grade(score)
    print(f"The grade for a score of {score} is: {grade}")
else:
    print("Invalid score! Please enter a number between 0 and 100.")
