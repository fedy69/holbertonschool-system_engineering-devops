#!/usr/bin/python3
'''Python script to get information and store in CSV file'''
import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_list = requests.get('{}/users'.format(url)).json()
    todo_list = requests.get('{}/todos'.format(url)).json()
    user_name = ''
    file_name = 'todo_all_employees.json'
    data = {}

    for task in user_list:
        data[task['id']] = []
        for todo in todo_list:
            if todo['userId'] == task['id']:
                data[task['id']].append({'task': todo['title'],
                                         'completed': todo['completed'],
                                         'username': task['username']})
    with open(file_name, 'w') as f:
        json.dump(data, f)
