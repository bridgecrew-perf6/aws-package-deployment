import requests


def ping_google(event=None, context=None):
    res = requests.get("https://www.google.com/")
    if res.status_code == 200:
        return "It was successful"
