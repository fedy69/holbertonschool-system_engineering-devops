#!/usr/bin/python3
"""
reddit api that returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Subs of reddit """
    if type(subreddit) is not str or subreddir is None:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
    }
    resp = requests.get(url, headers=h, allow_redirects=False)
    resp.raise_for_status()
    if resp.status_code != 200:
        return 0
    resp_json = resp.json()
    if 'suscribers' not in resp_json.get('data'):
        return 0
    elif 'data' not in resp_json:
        return 0
    else:
        return resp_json['data']['subscribers']