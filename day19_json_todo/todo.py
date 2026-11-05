import json
from pathlib import Path

FILE = Path("tasks.json")


def load_tasks():
    if not FILE.exists():
        return []

    try:
        with FILE.open("r") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            print("Error: Your tasks file has an invalid format.")
            return None

        return tasks

    except json.JSONDecodeError:
        print("Error: Your tasks file is damaged.")
        print("Restore a valid backup before continuing.")
        return None


def save_tasks(tasks):
    with FILE.open("w") as file:
        json.dump(tasks, file, indent=4)


def complete_task(tasks):
    if not tasks:
        print("No tasks to complete.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task['task']}")

    try:
        choice = int(input("Enter task number to complete: "))

        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not done"
        print(f"{number}. {task['task']} - {status}")

    try:
        choice = int(input("Enter task number to delete: "))

        if 1 <= choice <= len(tasks):
            deleted_task = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['task']}' deleted!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


tasks = load_tasks()

if tasks is None:
    print("Please fix or restore tasks.json, then run the app again.")
    raise SystemExit


while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark a task complete")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Task: ").strip()

        if name:
            tasks.append({
                "task": name,
                "completed": False
            })

            save_tasks(tasks)
            print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Not done"
                print(f"{number}. {task['task']} - {status}")

    elif choice == "3":
        complete_task(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")