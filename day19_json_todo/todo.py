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


tasks = load_tasks()

if tasks is None:
    print("Please fix or restore tasks.json, then run the app again.")
    raise SystemExit

if tasks is None:
    print("The application cannot continue.")
    raise SystemExit

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark a task complete")
    print("4. Exit")

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
        if not tasks:
            print("No tasks to complete.")
        else:
            for number, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Not done"
                print(f"{number}. {task['task']} - {status}")

            try:
                task_number = int(input("Enter task number to complete: "))

                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")