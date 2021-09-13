#!/usr/bin/python3
"""Script that given employee ID, return information about his list progress"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    USER_ID = argv[1]
    filename = USER_ID + '.json'
    getter = requests.get(url + 'users?id=' + USER_ID)
    getter_file = getter.json()
    USERNAME = getter_file[0].get('username')
    request = requests.get(url + 'todos?userId=' + USER_ID)
    request_file = request.json()
    json_dict = {}
    task_list = []

    for tasks in range(len(request_file)):
        new_dict = {}
        new_dict["task"] = request_file[tasks].get('title')
        new_dict["completed"] = request_file[tasks].get('completed')
        new_dict["username"] = USERNAME
        task_list.append(new_dict)
    json_dict[USER_ID] = task_list
    with open(filename, 'w') as outfile:
        json.dump(json_dict, outfile)
