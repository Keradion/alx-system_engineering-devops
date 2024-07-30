#!/usr/bin/python3
"""
This script uses REST API and a given employee ID  to return information
about the TODO list progress of the employee.
"""
import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    count = 0

    api_todo_url = 'https://jsonplaceholder.typicode.com/todos'
    api_user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)

    todo_response = requests.get(api_todo_url).json()
    user_response = requests.get(api_user_url)
    employee_name = user_response.json()['name']

    for each in todo_response:
        if each.get('userId') == employee_id:
            with open('USER_ID.csv', 'a', newline='') as file:
                writer_object = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
                writer_object.writerow([each.get('userId'), employee_name, each.get(
                    'completed'), each.get('title')])
