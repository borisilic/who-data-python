import requests

r = requests.post('https://api.github.com/events', data={'1': '2'})
print(r.text)
