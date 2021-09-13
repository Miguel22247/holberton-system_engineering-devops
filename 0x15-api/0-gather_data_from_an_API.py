#!/usr/bin/python3
"""Script that given employee ID, return information about his list progress"""
import requests
import sys
from sys import argv

if __name__ == '__main__':
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'

    values = url_todo.json()

    name_get = requests.get(url_user)
    user_name = name_get.json()
    real_name = ""
    for element in user_name:
        if element.get('id') == int(argv[1]):
            real_name = element.get('name')
            break

    full_list = []
    for dict in values:
        if dict.get('userId') == int(argv[1]):
            full_list.append(dict)

    true_elements = []
    for completed in full_list:
        if completed.get('completed'):
            true_elements.append(completed)

    print('Employee {} is done with tasks({}/{}):'.
          format(real_name, len(true_elements), len(full_list)))
    for task in true_elements:
        print('\t {}'.format(task.get('title')))