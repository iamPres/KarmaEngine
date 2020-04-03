import requests
import ast
import json
import keyboard
from art import *

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
                print(i["address"])
                print("------------------------------------------------------------------")

            print(str(len(data["Items"]))+" results")
        except:
            print("Something went wrong...")
