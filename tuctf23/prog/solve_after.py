import requests
from pwn import *

get_url = 'https://hacker-typer.tuctf.com/'
post_url = 'https://hacker-typer.tuctf.com/check_word'

s = requests.Session()
p1 = log.progress("Typing words: ")
while True:
    r = s.get(get_url)
    for x in str(r.text).split('\n'):
        if '<p>Type the word: <strong name="word-title">' in x:
            word = x[52:70].split('<')[0]
            data = {'word': word}
            p = s.post(post_url, data=data)
            p1.status(str(p.text))
            if 'TUCTF' in str(p.text):
                flag = str(p.text).split('You\'re fast!')[1].split("\"")[0]
                print('FLAG FOUND = '+ flag)
                exit()
            break
