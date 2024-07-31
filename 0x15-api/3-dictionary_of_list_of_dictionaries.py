#!/usr/bin/python3
"""
This script uses REST API and a given employee ID  to return information
about the TODO list progress of the employee.
"""
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    count = 0
    temp_dict = {}
    employee_dict = {}
    employee_list = []

    api_todo_url = 'https://jsonplaceholder.typicode.com/todos'
    api_user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)

    todo_response = requests.get(api_todo_url).json()
    user_response = requests.get(api_user_url)
    employee_name = user_response.json()['name']

    for each in todo_response:
        if each.get('userId') == employee_id and each.get('completed') is True:
            count = count + 1

    print('Employee {} is done with tasks({}/20):'.format(
        employee_name, count))

    for each in todo_response:
        if each.get('userId') == employee_id and each.get('completed') is True:
            print('\t ', end='')
            print(each['title'])

    api_user_url = 'https://jsonplaceholder.typicode.com/users/'
    user_response = requests.get(api_user_url).json()

    api_todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    todo_response = requests.get(api_todo_url).json()
    for user in user_response:
        user_id = user['id']
        employee_list = []
        for todo in todo_response:
            if user_id == todo['userId']:
                temp_dict["username"] = user['username']
                temp_dict['task'] = todo.get('title')
                temp_dict['completed'] = todo.get('completed')
                employee_list.append(temp_dict)
                temp_dict = {}

        employee_dict[user_id] = (employee_list)

    with open('todo_all_employees.json', 'a') as json_file:
        json_object = json.dumps(employee_dict)
        json_file.write(json_object)
