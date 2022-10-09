# my Parsing tools
Этот проект учебный для парсинга сайтов по разовым запросам.
Код разрабытавется на Jupyter notebook, после этого стабильная версия 
переносится на этот проект для последующих использований и модификаций с отработкой OOP SOLID Test driven devolopments
# Installation
На данном этапе не требуется

# classes_dict.py
Файл с вспомогательными классами

## class Dicts()
Родителький класс для описания, логирования и сохранения результатов 
  - атрибут папка для сохранения folderlog = 'folder/' 
  - init требует словарь вида:
  dtask = {'name': 'ALROSA_diamonds_test-3',
           'domain': 'https://sunlight.net/',
           'links':[],
           'urls0': 'https://alrosadiamond.ru/diamonds/',
           'urlslast': 'https://alrosadiamond.ru/diamonds/pagen_3/',
           'descr': 'тестовый'}
  - save для сохранения словаря
  - load для загрузки
  
## class Dtask(Dicts):
Дочерний класс для задач
- атрибут папка для сохранения folderlog =  'tasklogs/'
- print для легкой печати словара задачи без ключа links
   
# parsing_sunlight # 

file main, Class Site()

# parcing ALROSA
file main_alrosa, Class Site_alrosa()
