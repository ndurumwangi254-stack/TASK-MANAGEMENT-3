from datetime import datetime
from .validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    """Add a task. Validation errors raise ValueError."""
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    """Mark task by 1‑based index. Catch ValueError from invalid index."""
    try:
        idx = int(index) - 1
        if 0 <= idx < len(tasks):
            if tasks[idx]["completed"]:
                print("Task is already marked as complete.")
            else:
                tasks[idx]["completed"] = True
                print("Task marked as complete!")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")
    for i, task in enumerate(pending, start=1):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print()

def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed_count = sum(1 for t in tasks if t["completed"])
    return (completed_count / len(tasks)) * 100