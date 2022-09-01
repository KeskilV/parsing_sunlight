import datetime
import json
import os

class Dlinks():
    '''v0002 save(self, taskname, links, urls, domain, taskdescr, datestr=None)'''


    folderlinks = 'links/'

    def save(self, taskname, links, urls, domain, taskdescr, datestr=None):
        self.taskname = taskname
        self.links = links
        self.urls = urls
        self.domain = domain
        self.taskdescr = taskdescr
        print(datestr,'now:', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') )
        if datestr == None:
            self.datestr = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        else:
            self.datestr = datestr
        dlinks = {'taskname': self.taskname,
                  'links': self.links,
                  'datestr': self.datestr,
                  'urls': self.urls,
                  'domain': self.domain,
                  'taskdescr': self.taskdescr}

        with open(self.folderlinks + 'dlinks_' + self.taskname + '_' + self.datestr + '.json', 'w') as writefile:
            json.dump(dlinks, writefile)
            print('линки записаны: ', self.folderlinks + 'dlinks_' + self.taskname + '_' + self.datestr + '.json')

    def load(self):
        files = os.listdir(self.folderlinks)
        print([e for e in enumerate(files)])
        i = int(input('введите номер файла: '))
        with open(self.folderlinks + files[i], 'r') as writefile:
            dlinks = json.load(writefile)
        self.taskname = dlinks['taskname']
        self.links = dlinks['links']
        self.urls = dlinks['urls']
        self.domain = dlinks['domain']
        self.taskdescr = dlinks['taskdescr']
        self.datestr = dlinks['datestr']
        print(f'линки загружены с :{self.folderlinks + files[i]},\n всего\
        {len(self.links)} линков,\n загружены атрибуты {dlinks.keys()} \
        {self.taskname, self.urls, self.domain, self.taskdescr, self.datestr}')
        return self.links
