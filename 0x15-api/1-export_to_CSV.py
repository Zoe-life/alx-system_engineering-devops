import requests
import csv


def export_to_csv(employee_id):
    """
    Fetches employee's TODO list and exports it to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
    """

    """ Fetch employee's name from a dedicated endpoint"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')

    # Fetch employee's todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Create CSV file
    filename = f"{USRER_ID}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                f'"{employee_id}"',
                f'"{employee_name"',
                f'"{"True" if todo.get('completed') else "False"}"',
                f'"{todo.get("title")}"'
            })


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID.csv>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Error: Invalid employee ID. Please enter a positive integer.")
