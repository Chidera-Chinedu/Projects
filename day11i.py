student = {
    "name": "Abas",
    "age": 18,
    "country": "Nicaragua",
    "game": "FC"
}

for key, value in student.items():
    print(f"{key}: {value}")

    if student["age"] >= 18:
        print("The student is an adult.")
    else: 
        print("The student is a teenager.")
