import requests
import ast
import json

file = open("crawler_data.txt", "r")
links = file.read()
links = links.strip('][').split(', ')
i = 0
while True:
    i += 1000
    [print(p) for p in links[0:i]]
    resp = requests.post('https://qxvxx2xw1g.execute-api.us-east-2.amazonaws.com/basic/submit', json={"body":links[0:i]})
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
