students = [
    {
        "name": "Sami",
        "age": 16,
        "score": 79
    },
    {
        "name": "Cody",
        "age": 14,
        "score": 94
    },
    {
        "name": "Leo",
        "age": 18,
        "score": 66
    }
]

for student in students:
    for key, value in student.items():
        print(f"{key}: {value}")

    if student["score"] >= 80:
        print("Excellent!")
    elif student["score"] >= 50:
        print("Good")
    else:
        print("Needs Improvement.")

    print("----------------")