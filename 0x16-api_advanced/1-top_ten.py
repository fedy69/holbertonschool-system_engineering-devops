#!/usr/bin/python3
"""Function that queriess Reddit API and returns top 10 hot posts """
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;\
                         rv:68.0) Gecko/20100101 FirefoxFirefox/68.0'}
    with requests.session() as client:
        info = client.get(url, headers=headers, allow_redirects=False).json()
        try:
            for i in info.get('data').get('children'):
                print(i.get("data").get("title"))
        except Exception:
            print(None)
