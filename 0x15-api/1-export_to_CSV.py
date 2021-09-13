#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    USER_ID = argv[1]
    user_url = requests.get(url + 'users?id=' + USER_ID)
    user_response = user_url.json()
    USERNAME = user_response[0].get('username')

    todo_url = requests.get(url + 'todos?userId=' + USER_ID)
    todo_response = todo_url.json()
    status = []
    titles = []
    for content in range(len(todo_response)):
        status.append(todo_response[content].get('completed'))
        titles.append(todo_response[content].get('title'))
    filename = USER_ID + '.csv'
    with open(filename, mode='w') as file_:
        task = csv.writer(file_, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_ALL)
        for queue in range(len(status)):
            task.writerow([USER_ID, USERNAME, status[queue], titles[queue]])
