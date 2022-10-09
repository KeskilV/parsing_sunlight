import unittest

from classes_dict import Dtask, Dicts
from classes_site import *


class TestDtask(unittest.TestCase):
    def test_init_tasks(self):
        dtask = {'name': 'ALROSA_diamonds_test-3',
                 'domain': 'https://alrosadiamond.ru/',
                 # 'links':[],
                 'urls0': 'https://alrosadiamond.ru/diamonds/',
                 'urlslast': 'https://alrosadiamond.ru/diamonds/pagen_3/',
                 'descr': 'тестовый'}
        task = Dtask(dtask)
        task.save()
        self.assertEqual(True, True)  # add assertion here

    def test_load_tasks(self):
        control_dtask = {'name': 'ALROSA_diamonds_test-3',
                 'domain': 'https://alrosadiamond.ru/',
                 # 'links':[],
                 'urls0': 'https://alrosadiamond.ru/diamonds/',
                 'urlslast': 'https://alrosadiamond.ru/diamonds/pagen_3/',
                 'descr': 'тестовый'}
        control_dtask2 = {'name': 'ALROSA_diamonds_test-32022-10-09-16-07',
                          'domain': 'https://alrosadiamond.ru/',
                          'urls0': 'https://alrosadiamond.ru/diamonds/',
                          'urlslast': 'https://alrosadiamond.ru/diamonds/pagen_3/',
                          'descr': 'тестовый', 'datestr0': '2022-10-09-16-07',
                          'datestr': '2022-10-09-16-07'}

        dtask = {}
        task = Dtask(dtask)
        task.load()#'d_ALROSA_diamonds_test-32022-10-09-16-03_2022-10-09-16-03.json')
        #print(task.dict)
        self.assertEqual(len(control_dtask2), len(task.dict))  # add assertion here


if __name__ == '__main__':
    unittest.main()
