# -*- coding: UTF-8 -*-.
# Coded by : Romi Afrizal
# facebook.com/romi.29.04.03
import re,time,datatime,requests,os,sys
from bff-2 import rom

class dump_grup:

    def __init__(self, cookies):
        self.glist = []
        self.cookies = cookies
        self.extract('https://m.facebook.com/groups/?seemore')

    def extract(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/groups/' in i.get('href'):
                if 'category' in i.get('href') or 'create' in i.get('href'):
                    continue
                else:
                    self.glist.append({'id': ('').join(bs4.re.findall('/groups/(.*?)\\?', i.get('href'))), 'name': i.text})

        if len(self.glist) != 0:
            print ' '
            print '\x1b[1;95m\xe2\x80\xa2 \x1b[1;96myou have %s groups found.' % len(self.glist)
            print '\x1b[1;95m\xe2\x80\xa2 \x1b[1;96mselect action '
            print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 1 \x1b[1;96mget grup by searching the name'
            print '\x1b[1;95m\xe2\x80\xa2\x1b[1;92m 2 \x1b[1;96minput group id (manual)\n'
            while True:
                c = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;92m \x1b[1;96mmenu\x1b[1;91m : \x1b[1;93m')
                if c == '':
                    continue
                elif c == '1':
                    self.search()
                    exit()
                elif c == '2':
                    self.manual()
                    exit()
                else:
                    print '\x1b[1;95m\xe2\x80\xa2\x1b[1;91m wrong input'

        else:
            exit('\x1b[1;95m\xe2\x80\xa2\x1b[1;91m no groups found')

    def manual(self):
        id = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;92m \x1b[1;96mgroup id\x1b[1;91m : \x1b[1;93m')
        if id == '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://m.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'konten tidak' in r.find('title').text.lower():
                exit('\x1b[1;95m\xe2\x80\xa2 \x1b[1;91minput id grup error')
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print '\x1b[1;95m\xe2\x80\xa2 \x1b[1;96mtarget\x1b[1;91m : \x1b[1;93m%s ' % self.listed.get('name')[0:20]
                self.dumps('https://m.facebook.com/groups/' + id)

    def search(self):
        whitelist = []
        q = raw_input('\x1b[1;95m\xe2\x80\xa2\x1b[1;92m \x1b[1;96mmenu\x1b[1;91m : \x1b[1;93m').lower()
        if q == '':
            self.search()
        else:
            print '-' * 30
            for e, i in enumerate(self.glist):
                if q in i.get('name').lower():
                    whitelist.append(i)
                    print '  %s. %s' % (
                     len(whitelist),
                     i.get('name').lower().replace(q, '%s%s%s' % (G, q, N)))

            if len(whitelist) == 0:
                print '\x1b[1;91m\xe2\x80\xa2 mno result found with this query : %s' % q
                self.search()
            else:
                print ''
                self.choice(whitelist)

    def choice(self, whitelist):
        try:
            self.listed = whitelist[(input('\x1b[1;95m\xe2\x80\xa2 \x1b[1;96mselect group\x1b[1;91m :\x1b[1;93m ') - 1)]
            self.f()
            print '\x1b[1;95m\xe2\x80\xa2 \x1b[1;96mtarget\x1b[1;91m : \x1b[1;93m%s' % self.listed.get('name')
            self.dumps('https://m.facebook.com/groups/' + self.listed.get('id'))
        except Exception as e:
            print '\x1b[1;95m\xe2\x80\xa2 \x1b[1;93m%s' % e
            self.choice(whitelist)

    def f(self):
        self.fl = raw_input('\x1b[1;95m\xe2\x80\xa2 \x1b[1;96mresult filename \x1b[1;91m:\x1b[1;93m ').replace(' ', '_')
        if self.fl == '':
            self.f()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print '\r\x1b[1;95m\xe2\x80\xa2 \x1b[1;96mdump \x1b[1;93m(\x1b[1;92m%s\x1b[1;93m)  wait bro ! ' % len(open(self.fl).read().splitlines()),
        sys.stdout.flush()
        for i in r.find_all('h3'):
            try:
                if len(bs4.re.findall('\\/', i.find('a', href=True).get('href'))) == 1:
                    ogeh = i.find('a', href=True)
                    if 'profile.php' in ogeh.get('href'):
                        a = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            continue
                    else:
                        a = ('').join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
            except:
                continue

        for i in r.find_all('a', href=True):
            if 'Lihat Postingan Lainnya' in i.text:
                while True:
                    try:
                        self.dumps('https://m.facebook.com/' + i.get('href'))
                        break
                    except Exception as e:
                        print '\r\x1b[1;95m\xe2\x80\xa2\x1b[1;96m %s, \x1b[1;93mretrying' % e
                        continue

        exit('\n\x1b[1;92m\xe2\x80\xa2 successfully dump %s id from group %s' % (len(open(self.fl).read().splitlines()), self.listed.get('name')[0:20]))
© 2021 GitHub, Inc.
