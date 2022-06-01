#!/usr/bin/python3
'''Python script to get information and store in CSV file'''
import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(url, employee_id)).json()
    user_name = user['username']
    tasks = requests.get('{}/todos?userId={}'.format(url,
                                                     employee_id)).json()
    file_name = '{}.csv'.format(employee_id)

    with open(file_name, 'w') as f:
        for data in tasks:
            csv_write = csv.writer(f, quoting=csv.QUOTE_ALL)
            csv_write.writerow([data['userId'],
                                user_name,
                                data['completed'],
                                data['title']])
