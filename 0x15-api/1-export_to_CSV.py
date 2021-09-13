
#!/usr/bin/python3
""" This script dumps a dict into a CSV file
"""
import requests
from sys import argv


if __name__ == '__main__':
    USER_ID = argv[1]
    filename = USER_ID + '.csv'
    user_name = requests.get('https://jsonplaceholder.typicode.com/users/{}/'.
                             format(USER_ID).json().get('username'))
    user_tasks = requests.\
        get('https://jsonplaceholder.typicode.com/users/{}/todos'.
            format(int(argv[1]))).json()

    with open('{}.csv'.format(argv[1]), mode='w') as file:
        for item in user_tasks:
            file.write('"{}","{}","{}","{}"\n'.
                       format(argv[1], user_name, item.
                              get('completed'), item.get('title')))
