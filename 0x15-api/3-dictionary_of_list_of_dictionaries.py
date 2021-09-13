#!/usr/bin/python3
"""Script that given employee ID, return information about his list progress"""
import json
import requests
from sys import argv

from requests.api import get

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users')
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        all_dict = {}
        for user in users:
            user_dict = {}
            task_list = []
            tasks = requests.\
                get('https://jsonplaceholder.typicode.com/user/{}/todos'.
                    format(user.get('id'))).json()
        for task in tasks:
            new_task_dict = {}
            new_task_dict["username"] = user.get('username')
            new_task_dict["task"] = task.get('title')
            new_task_dict["completed"] = task.get('completed')
            task_list.append(new_task_dict)
        all_dict[user.get('id')] = task_list
    json.dump(all_dict, file)
