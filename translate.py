import requests
import re
from randomly import randoml


def translate_word():
    randomly = randoml()
    page = requests.get(f'https://www.diki.pl/slownik-angielskiego?q={randomly}')
    # f = open('data.txt', 'w')
    # f.write(page.text)            find your pattern from file
    pattern = r'po polsku? - (^([a-z]*,{0,1}){0,}$);'
    obj = re.search(pattern, page.text)
    return obj.group(1)