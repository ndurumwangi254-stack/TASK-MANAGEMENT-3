from datetime import datetime

def validate_task_title(title):
    """Validate task title: non-empty string, otherwise raise ValueError."""
    if not title or not isinstance(title, str) or title.strip() == "":
        raise ValueError("Task title cannot be empty.")
    return True

def validate_task_description(description):
    """Validate task description: non-empty and length ≤ 500."""
    if not description or not isinstance(description, str) or description.strip() == "":
        raise ValueError("Task description cannot be empty.")
    if len(description) > 500:
        raise ValueError("Task description is too long (max 500 characters).")
    return True

def validate_due_date(due_date):
    """Validate due date: format YYYY-MM-DD and not in the past."""
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d")
        if parsed_date.date() < datetime.now().date():
            raise ValueError("Due date cannot be in the past.")
        return True
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")