#!/usr/bin/python3
"""Function that queries the reddit API"""
import requests


def top_ten(subreddit):
    """Returns the top ten"""
    url = 'https://www.reddit.com/r/' + subreddit + "/hot.json" + '?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows)'}
    res_status = requests.get(url, headers=headers, allow_redirects=False)

    if res_status.status_code == 200:
        posts = res_status.json()['data']['children']
        for title in posts:
            print(title['data']['title'])
    else:
        print(None)
