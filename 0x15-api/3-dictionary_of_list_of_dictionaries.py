#!/usr/bin/python3

"""
This script fetches TODO lists for all employees and exports them
to a JSON file
"""

import json
import requests


def export_all_todos_to_json():
    """
    Fetches todos for all users and exports to a JSON file.
    """

    all_todos = {}
    for user_id in range(1, 11):  # Assuming users from 1 to 10
        t_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todos_response = requests.get(t_url)
        todos = todos_response.json()

        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()
        username = user_data.get('name', 'Unknown')

        all_todos[user_id] = [{
            "username": username,
            "task": todo.get("title"),
            "completed": todo.get("completed")
        } for todo in todos]

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_todos, jsonfile, indent=4)


if __name__ == "__main__":
    export_all_todos_to_json()
