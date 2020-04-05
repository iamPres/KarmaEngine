import requests
import re
from urllib.parse import urlparse
import sys
import keyboard

url = "https://ifunny.co/"
file = open("links.txt", "a+")
visited = []
iteration = 0
start_index = 0

recursive_depth = -1

def scrape(links):
    global iteration

    output = []
    valid = True

    for link in links:
        if link not in visited or link == url:
            try:
                parsed = urlparse(link)
                base = f"{parsed.scheme}://{parsed.netloc}"
                html = requests.get(link)
                output = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', str(html.content))
                temp = []
                for i in output:
                    if i.find('/picture/') != -1:
                        temp.append(i)

                output = temp

                for o in range(len(output)):
                    if not urlparse(output[o]).netloc:
                        link_with_base = base + output[o]
                        output[o] = link_with_base
                file = open("links.txt", "a+")
                file.write(str(output))
                file.close()
            except:
                valid = False
                pass

            if valid == True:
                print("Scraped "+str(link))
                resp = requests.post('https://qxvxx2xw1g.execute-api.us-east-2.amazonaws.com/basic/submit', json={"body":output})
                print(output)
            visited.append(link)

            iteration += 1
            if iteration < recursive_depth:
                print("Recursion Reset.")
                iteration = 0
                scrape([url])

            scrape(output[start_index:])
        else:
            pass

scrape([url])
