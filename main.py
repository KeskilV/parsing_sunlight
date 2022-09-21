import datetime
import json
import os
import re
import requests
from requests import Request, Session
from bs4 import BeautifulSoup
import pandas as pd

from classes_dict import Dtask, Dicts
from classes_site import Site
'''
dtask = {'name': 'ALROSA_diamonds',
         'domain': 'https://sunlight.net/',
         # 'links':[],
         'urls0': 'https://alrosadiamond.ru/diamonds/',
         'urlslast': 'https://alrosadiamond.ru/diamonds/pagen_35/',
         'descr': ''}

'''
dtask = {'name': 'SL_diamonds',
         'domain': 'https://sunlight.net/',
         # 'links':[],
         'urls0': 'https://sunlight.net/catalog/diamonds-all.html',
         'urlslast': 'https://sunlight.net/catalog/diamonds-all/page-104/',
         'descr': ''}

task = Dtask(dtask)
#task.load()
task.print()
site = Site()
site.getlinks(task)
#site.parcing(task, 0, 1251)

task.save()