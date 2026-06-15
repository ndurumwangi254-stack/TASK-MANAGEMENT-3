from datetime import datetime

def validate_task_title(title):
    """Validate task title: non-empty string."""
    if not title or not isinstance(title, str) or title.strip() == "":
        print("Error: Task title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    """Validate task description: non-empty string."""
    if not description or not isinstance(description, str) or description.strip() == "":
        print("Error: Task description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    """Validate due date: format YYYY-MM-DD and not in the past."""
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d")
        if parsed_date.date() < datetime.now().date():
            print("Error: Due date cannot be in the past.")
            return False
        return True
    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format.")
        return False