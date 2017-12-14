# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests

s = requests.Session()


class CSDN:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_url = 'https://passport.csdn.net/account/login'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK'
                          'it/537.36 (KHTML, like Gecko) Chrome/61.0.3163.1'
                          '00 Safari/537.36 OPR/48.0.2685.52',
            'Referer': 'http://my.csdn.net/my/mycsdn'
        }

    def login(self):
        params = {
            'from': 'http://my.csdn.net/my/mycsdn'
        }
        html = s.get(self.login_url, params=params, headers=self.headers)
        soup = BeautifulSoup(html.content, 'lxml')
        lt = soup.select('input[name="lt"]')[0].get('value')
        execution = soup.select('input[name="execution"]')[0].get('value')
        event_id = soup.select('input[name="_eventId"]')[0].get('value')
        data = {
            'username': self.username,
            'password': self.password,
            'rememberMe': 'true',
            'lt': lt,
            'execution': execution,
            '_eventId': event_id
        }
        r = s.post(self.login_url, data=data)
        self.headers['Referer'] = 'http://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn'
        resp = s.get('http://my.csdn.net/my/mycsdn', headers=self.headers)
        print(resp.text)


username = input('请输入账号：')
password = input('请输入密码：')
cs = CSDN(username, password)
cs.login()