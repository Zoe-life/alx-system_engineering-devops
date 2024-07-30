#!/usr/bin/python3

"""
This script fetches an employee's TODO list and exports it to a JSON file
"""

import json
import requests


def export_to_json(employee_id):
    """
    Fetches employee's TODO list and exports it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
    """

    # Fetch employee's name from a dedicated endpoint
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')

    # Fetch employee's todos
    t_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(t_url)
    todos = todos_response.json()

    # Create a dictionary to store the data
    data = {
        employee_id: [
            {
                "task": todo.get("title"), "completed": todo.get("completed"),
                "username": employee_name
            } for todo in todos
        ]
    }

    # Create JSON file
    filename = f"{USER_ID}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Error: Invalid employee ID. Please enter a positive integer.")
