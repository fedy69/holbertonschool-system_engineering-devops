#!/usr/bin/python3
'''Python script that returns information about TODO list based on emp ID'''
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(url, employee_id)).json()
    user_name = user.get('name')
    tasks_completed = []
    tasks_total = requests.get('{}/todos?userId={}'.format(url,
                                                           employee_id)).json()
    for task in tasks_total:
        if task['completed'] is True:
            tasks_completed.append(task['title'])

    print('Employee {} is done with tasks({}/{}):'.format(user_name,
                                                          len(tasks_completed),
                                                          len(tasks_total)))
    for task in tasks_completed:
        print('\t {}'.format(task))
