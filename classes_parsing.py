class Dlinks():
    '''taskname, links, urls, domain, taskdescr, datestr=None'''

    folderlinks = 'links/'

    def save(self, taskname, links, urls, domain, taskdescr, datestr=None):
        import datetime
        import json
        import os
        self.taskname = taskname
        self.links = links
        self.urls = urls
        self.domain = domain
        self.taskdescr = taskdescr
        if datestr:
            self.datestr = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        else:
            self.datestr = datestr
        dlinks = {'taskname': taskname,
                  'links': links,
                  'datestr': datestr,
                  'urls': urls,
                  'domain': domain,
                  'taskdescr': taskdescr}

        with open(self.folderlinks + 'dlinks_' + self.taskname + '_' + datestr + '.json', 'w') as writefile:
            json.dump(dlinks, writefile)
        print('линки записаны: ', self.folderlinks + 'dlinks_' + self.taskname + '_' + datestr + '.json')

    def load(self):
        import datetime
        import json
        import os
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
