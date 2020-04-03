import requests
import ast
import json
import keyboard
from urllib.parse import urlparse
from art import *
import re
from lxml.html import fromstring

print(text2art("Karma Engine"))

while True:
    print("======================================================================")
    query = input("Search for anything: ")
    print("======================================================================")

    resp = requests.post('https://qxvxx2xw1g.execute-api.us-east-2.amazonaws.com/basic/search', json={"body":query})
    if resp.status_code != 200:
        # This means something went wrong.
        print("Something went wrong...")

    if resp.status_code == 200:
        try:
            data = json.loads(resp.content)
            print("------------------------------------------------------------------")
            for i in data["Items"]:
                parsed = urlparse(i["address"])
                response = requests.get(i["address"]).content
                title = fromstring(response).findtext(".//h1")
                if str(title) == "None":
                    print(str(parsed.netloc)+" | "+str(i["address"]))
                else:
                    print(str(parsed.netloc)+" - "+str(title)+" | "+str(i["address"]))
                print("------------------------------------------------------------------")

            print(str(len(data["Items"]))+" results")
        except:
            print("Something went wrong...")
