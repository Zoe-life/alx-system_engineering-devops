#!/usr/bin/python3

import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays employee TODO list progress from the API.

    Args:
        employee_id (int): The ID of the employee.
    """
    # Validate input
    if not isinstance(employee_id, int) or employee_id <= 0:
        print("Error: Invalid employee ID. Please enter a positive integer.")
        return

    # Build API URL
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Send GET request
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-2xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to retrieve data from API: {e}")
        return

    # Parse response data
    todos = response.json()

    # Calculate progress
    completed_tasks = sum(1 for todo in todos if todo.get("completed"))
    total_tasks = len(todos)

    # Print employee information
    # Use first todo title as name
    employee_name = todos[0].get("title", "Unknown")
    print(
        f"""Employee {employee_name} is done
         with tasks({completed_tasks}/{total_tasks}):""")

    # Print completed task titles
    for todo in todos:
        if todo.get("completed"):
            print(f"\t{todo.get('title', 'No Title')}")


# Script execution (if run directly)
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Invalid employee ID. Please enter a positive integer.")
