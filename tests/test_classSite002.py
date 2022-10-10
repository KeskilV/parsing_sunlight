import unittest

import classes_dict
import classes_site


class TestSite(unittest.TestCase):
    def test_getlinks(self):
        dtask = {'name': 'ALROSA_diamonds_test-3',
                 'domain': 'https://alrosadiamond.ru/',
                 # 'links':[],
                 'urls0': 'https://alrosadiamond.ru/diamonds/',
                 'urlslast': 'https://alrosadiamond.ru/diamonds/pagen_3/',
                 'descr': 'тестовый'}
        task = classes_dict.Dtask(dtask)
        # task.load()
        site = classes_site.Site_alrosa()
        site.getlinks(task)
        task.save()
        self.assertEqual(True, True)  # add assertion here



if __name__ == '__main__':
    unittest.main()
