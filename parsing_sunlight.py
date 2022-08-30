from bs4 import BeautifulSoup
import requests
from requests import Request, Session
import pandas as pd
import re
import json
import datetime
import os


def mysoup(urls):
    response = requests.get(urls)
    return BeautifulSoup(response.text, 'lxml')


def getlinks_muiz(urls):
    quotes = mysoup(urls).find_all('div', class_="product")
    res = [q.find("a").get("href") for q in quotes]
    print(len(res), 'links is ready ', res[0], '...', res[-1])
    return res


def getlinks_sunl(urls):
    quotes = mysoup(urls).find_all('a', class_="cl-item-link js-cl-item-link js-cl-item-root-link")
    res = [q.get("href") for q in quotes]
    print(len(res), 'links is ready ', res[0], '...', res[-1])
    return res


def get_info_from_card(urls):
    card = mysoup(urls)
    return card.select(
        'body > div.grid > div > div > div.detail__item.detail__item--new > div.detail__item-col._3.position-relative > form > div:nth-child(8)')

def load_links(taskname, taskdescr):
    folderlink = 'links/'
    files = os.listdir(folderlink)
    print([e for e in enumerate(files)])
    i = int(input('введите номер файла'))
    with open(folderlink + files[i], 'r') as writefile:
        dlinks = json.load(writefile)
    return dlinks[taskname][1]

    print(taskname, taskdescr)


def parcing(links):

    for i in range(3):  # links)):
        try:
            row = len(data)
            urlcard = domain + links[i]
            card = mysoup(urlcard)
            data.loc[row, 'url'] = urlcard
            data.loc[row, 'h1'] = card.find("h1").text.strip()
            data.loc[row, 'art'] = card.find('div', class_="supreme-product-card__product-article-text").text.strip()
            data.loc[row, 'price'] = card.find('div',
                                               class_="supreme-product-card__price-discount-price").text.strip().replace(
                '\u202f', '').replace('\xa0', '')
            data.loc[row, 'price2'] = card.find('div', class_="supreme-product-card__price-old").text.strip().replace(
                '\u202f', '').replace('\xa0', '')
            a = card.find_all('p', class_="supreme-product-card__description supreme-product-card__description_default")
            data.loc[row, 'gold'] = ';'.join([x.text for x in a])
            data.loc[row, 'd1'] = "&".join(
                [t.text for t in card.find_all('span', class_="supreme-product-card-description__item-text")])
            data.loc[row, 'd0'] = "&".join(
                [t.text for t in card.find_all('a', class_="supreme-product-card-description__item-text")])
            # print(i, urlcard)
        except (AttributeError, TypeError) as e:
            print('error', e)
        except IndexError:
            print('indexerror len of = ', len(card.find_all('div', 'detail__item-option')))
        print(i, urlcard)


def byrepost():
    def gold(t, patt):
        f = re.search(patt, t)
        return f.group() if f else 're не найдено'

    pattern_gold = r'[Сс]ереб\w+|[Зз]олот\w*|[Сс]таль'
    pattern_diam = r'[Бб]риллиант\w*'
    pattern_probe = r'[\d]{,3}(?=\s*проб)'
    pattern_gramm = r'[\d.\d]{,5}(?=г;)'
    pattern_vst = r'вставк\w*'  # r'вставк\w*'
    pattern_type = r'(?<=;)\w+\s?\w*'

    data['diam'] = data.gold.apply(lambda x: gold(x, pattern_diam))
    data['goldsilv'] = data.h1.apply(lambda x: gold(x, pattern_gold))
    data['probe'] = data.gold.apply(lambda x: gold(x, pattern_probe))
    data['gramm'] = data.gold.apply(lambda x: gold(x, pattern_gramm))
    data['vst'] = data.gold.apply(lambda x: gold(x, pattern_vst))
    data['type'] = data.gold.apply(lambda x: gold(x, pattern_type))



taskname, taskdescr = 'бескаменка300822', 'все БК  8810'
domain = f'https://sunlight.net'
links = load_links(taskname, taskdescr)
#print(links)
data = pd.DataFrame(columns=['h1', 'art', 'price', 'price2', 'gold', 'gold2', 'weight', 'gems', 'gems2', 'url'])
parcing(links)
print(data)

