
def add_task():
    task = input("Enter your task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

    print("Task saved!")


def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("You have no tasks yet.")
        else:
            print("\nYour tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task.strip()}")

    except FileNotFoundError:
        print("You have no saved tasks yet.")


def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("You have no tasks to delete.")
            return

        print("\nYour tasks:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task.strip()}")

        try:
            choice = int(input("Enter the task number to delete: "))

            if 1 <= choice <= len(tasks):
                deleted_task = tasks.pop(choice - 1)

                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)

                print(f"Task deleted: {deleted_task.strip()}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    except FileNotFoundError:
        print("You have no saved tasks yet.")


while True:
    print("\n===== MY TO-DO APP =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Get outta here!")
        break
    else:
        print("Invalid choice. Choose 1, 2, 3, or 4.")
