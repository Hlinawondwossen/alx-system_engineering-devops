#!/usr/bin/python3
""" Exporting csv files"""

import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/Southern_Budget4358)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return 0

        data = response.json()

        return data['data']['subscribers']

    except Exception as e:
        return 0

