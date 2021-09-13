#!/usr/bin/python3
"""Script that given employee ID, return information about his list progress"""
import requests
from sys import argv
import csv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    USER_ID = argv[1]
    getter = requests.get(url + 'users?id' + USER_ID)
    file_getter = getter.json()
    USERNAME = file_getter[0].get('username')
    request = requests.get(url + 'todos?usersId' + USER_ID)
    request_file = request.json()
    status = []
    titles = []

    for file_content in range(len(request_file)):
        status.append(request_file[file_content].get('completed'))
        titles.append(request_file[file_content].get('title'))
    filename = USER_ID + ".csv"
    with open(filename, mode='w') as file_:
        task = csv.writer(file_, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_ALL)
        for w_table in range(len(status)):
            task.writerow([USER_ID, USERNAME, status[w_table], titles[w_table]])
