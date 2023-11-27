#!/usr/bin/python3
"""
Fetch and display employee TODO list progress using a REST API.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        user_data = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
        todos_data = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()

        completed_tasks = [task for task in todos_data if task["completed"]]
        num_done_tasks, total_tasks = len(completed_tasks), len(todos_data)

        print(f"Employee {user_data['name']} is done with tasks ({num_done_tasks}/{total_tasks}):")
        print(f"{user_data['name']}:", *([f"\n\t{task['title']}" for task in completed_tasks] or [" No completed tasks."]))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_script.py <employee_id>")
        sys.exit(1)

    get_employee_todo_progress(int(sys.argv[1]))
