#!/usr/bin/python3
"""
This script uses REST API and a given employee ID  to return information
about the TODO list progress of all the employees.
"""
import json
import requests
import sys

if __name__ == '__main__':
    temp_dict = {}
    employee_dict = {}
    employee_list = []

    api_user_url = 'https://jsonplaceholder.typicode.com/users/'
    user_response = requests.get(api_user_url).json()

    api_todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    todo_response = requests.get(api_todo_url).json()
    for user in user_response:
        user_id = user.get('id')
        employee_list = []
        for todo in todo_response:
            if user_id == todo.get('userId'):
                temp_dict["username"] = user.get('username')
                temp_dict['task'] = todo.get('title')
                temp_dict['completed'] = todo.get('completed')
                employee_list.append(temp_dict)
                temp_dict = {}

        employee_dict[user_id] = (employee_list)

    with open('todo_all_employees.json', 'a') as json_file:
        json_object = json.dumps(employee_dict)
        json_file.write(json_object)
