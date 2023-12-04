import requests
import json
from time import sleep

url = 'https://hacker-typer.tuctf.com/check_word'
body = {'word': '<the-first-word>'}
cookies = {'uuid': '<uuid-from-webpage-cookies>'}

while True:
    # sleep(0.5) added because of early server infra problems
    r = requests.post(url, data=body, cookies=cookies)
    print(r.text)
    data = json.loads(r.text)

    try:
        body["word"] = data["next_word"]
    except KeyError:
        print("err") # shoudln't really happen, again, server infra problems
