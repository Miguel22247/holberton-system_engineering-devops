#!/usr/bin/python3
"""Script that given employee ID, return information about his list progress"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    USER_ID = argv[1]
    getter = requests.get(url + 'users?id=' + USER_ID)
    getter_file = getter.json()
    USERNAME = getter_file[0].get('username')
    request = requests.get(url + 'todos?userId=' + USER_ID)
    request_file = request.json()
    status = []
    titles = []
    filename = USER_ID + '.csv'

    for content in range(len(request_file)):
        status.append(request_file[content].get('completed'))
        titles.append(request_file[content].get('title'))
    with open(filename, mode='w') as file_:
        task = csv.writer(file_, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_ALL)
        for w_table in range(len(status)):
            task.w_row([USER_ID, USERNAME, status[w_table], titles[w_table]])
