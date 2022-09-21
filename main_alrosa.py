import datetime
import json
import os
import re
import requests
from requests import Request, Session
from bs4 import BeautifulSoup
import pandas as pd

from classes_dict import Dtask, Dicts
from classes_site import *

dtask = {'name': 'ALROSA_diamonds_test-3',
         'domain': 'https://sunlight.net/',
         # 'links':[],
         'urls0': 'https://alrosadiamond.ru/diamonds/',
         'urlslast': 'https://alrosadiamond.ru/diamonds/pagen_3/',
         'descr': 'тестовый'}


task = Dtask(dtask)
#task.load()
task.print()
site = Site_alrosa()
site.getlinks(task)
#site.parcing(task, 0, 1251)

task.save()