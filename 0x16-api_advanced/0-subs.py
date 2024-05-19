#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    # Define the base URL and headers for the Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/yourusername)'}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the response status code is not 200, return 0
        if response.status_code != 200:
            return 0
        
        # Parse the JSON response
        data = response.json()
        
        # Return the number of subscribers
        return data['data']['subscribers']
    
    except:
        # If there is any error, return 0
        return 0
