#!/usr/bin/python3
'''Python script to get information and store in CSV file'''
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(url, employee_id)).json()
    user_name = user.get('username')
    tasks = requests.get('{}/todos?userId={}'.format(url,
                                                     employee_id)).json()
    file_name = '{}.json'.format(employee_id)
    data = {}
    data[employee_id] = []

    for task in tasks:
        data[employee_id].append({'task': task['title'],
                                  'completed': task['completed'],
                                  'username': user_name})
    with open(file_name, 'w') as f:
        json.dump(data, f)
