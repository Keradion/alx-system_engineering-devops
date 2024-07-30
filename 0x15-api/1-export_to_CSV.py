#!/usr/bin/python3
"""
This script uses REST API and a given employee ID  to return information
about the TODO list progress of the employee.
"""
import csv
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
    user_name = user_response.json()['username']

    for each in todo_response:
        if each.get('userId') == employee_id and each.get('completed') is True:
            count = count + 1
            user_id = each.get('userId')

    print('Employee {} is done with tasks({}/20):'.format(
        employee_name, count))

    for each in todo_response:
        if each.get('userId') == employee_id and each.get('completed') is True:
            print('\t ', end='')
            print(each['title'])

        file_name = str(user_id) + '.csv'

        if each.get('userId') == employee_id:
            with open(file_name, 'a', newline='') as csv_file:
                writer_object = csv.writer(
                        csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
                writer_object.writerow([each.get(
                    'userId'), user_name, each.get(
                    'completed'), each.get('title')])
