# my Parsing tools
Этот проект учебный для парсинга сайтов по разовым запросам.
Код разрабытавется на Jupyter notebook, после этого стабильная версия 
переносится на этот проект для последующих использований и модификаций с отработкой OOP SOLID Test driven devolopments

# в папке jupyter_notebook блокнот parsing_alrosa_develop для разработки кода парсера, тестов для переноса в стабильную версию Pycharm Содержание блоков:

BLOCK to/from Pycharm - готовые и разрабатываемые блоки для переноса
TESTS тесты
DEVELOP - разработка

# Installation
На данном этапе не требуется

# classes_dict.py
Файл с вспомогательными классами

## class Dicts()
Родителький класс для описания, логирования и сохранения результатов 
  - атрибут папка для сохранения folderlog = 'folder/' 
  - init требует словарь вида:
  dtask ={'name': 'SL_diamonds',
         'domain': 'https://sunlight.net/',
         # 'links':[],
         'urls0': 'https://sunlight.net/catalog/diamonds-all.html',
         'urlslast': 'https://sunlight.net/catalog/diamonds-all/page-104/',
         'descr': ''}
  - save для сохранения словаря
  - load для загрузки
  
## class Dtask(Dicts):
Дочерний класс для задач
- атрибут папка для сохранения folderlog =  'tasklogs/'
- print для легкой печати словаря задачи без ключа links
   
# classes_site
Файл с классами для парсинга

## class Site():
Класс для парсинга sunlite
- атрибут папки для результатов folderres = 'results/'
- init не требует входных параметоров
- genlinks_sunl(task:class Dtask) генерирует ссылки на листы с карточками при заданной в 
словаре задач первой странице и последней: (пример)
    'urls0': 'https://alrosadiamond.ru/diamonds/',
    'urlslast': 'https://alrosadiamond.ru/diamonds/pagen_3/'
- getlinks(task:class Dtask)->None принимает словарь задач, добавляет в словарь 
полученные линки
- parcing(self, task:class Dtask, linknum0=None, linknum=None) парсинг по словарю
задачи по полученным линкам, настроен на sunlight, сохраняет пром перзультаты в папку результаты

## class Site_alrosa(Site)
Класс дочерний с переопределением методов с учетом специфики парсинга для алроса
Пример словаря задач:
dtask = {'name': 'ALROSA_diamonds_test-3',
         'domain': 'https://alrosadiamond.ru/',
         # 'links':[],
         'urls0': 'https://alrosadiamond.ru/diamonds/',
         'urlslast': 'https://alrosadiamond.ru/diamonds/pagen_3/',
         'descr': 'тестовый'}
# Tests
001 - тест класса Dtask 
