print("Welcome to my notes app!")

while True:
    print("\n1. Add a note")
    print("2. View all notes")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Write your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Your note has been saved!")

    elif choice == "2":
        print("\nAll your notes:")

        with open("notes.txt", "a+") as file:
            file.seek(0)
            notes = file.read()

            if notes:
                print(notes)
            else:
                print("No notes yet.")

    elif choice == "3":
        print("Peace out!")
        break

    else:
        print("Invalid option. Please try again.")