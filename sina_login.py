#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
from common.requests_helper import make_session
import urllib3

urllib3.disable_warnings()


class SinaSpider:

    def __init__(self, username, password):
        self.session = make_session()
        self.username = username
        self.password = password
        self.index = 1

    def visit_start(self):
        self.session.get('https://passport.weibo.cn/signin/login')
        print('first s')

    def visit_login(self):
        url = 'https://passport.weibo.cn/sso/login'
        headers = {
            'Referer': 'https://passport.weibo.cn/signin/login'
        }
        data = {
            'username': self.username,
            'password': self.password,
            'savestate': '1',
            'r': '',
            'ec': '0',
            'pagerefer': '',
            'entry': 'mweibo',
            'wentry': '',
            'loginfrom': '',
            'client_id': '',
            'code': '',
            'qq': '',
            'mainpageflag': '1',
            'hff': '',
            'hfp': ''
        }
        resp = self.session.post(url, headers=headers, data=data)
        json_data = resp.json()
        # if json_data['retcode']==2000000:
        #     print('success')
        # else:
        #     print('fail')
        # print(resp.text)

    def visit_friends(self, next_cursor=None):
        if next_cursor :
            url = 'https://m.weibo.cn/feed/friends?'
        else:
            url = 'https://m.weibo.cn/feed/friends?max_id' + str(next_cursor)
        headers = {
            'Referer': 'https://m.weibo.cn/'
        }
        resp = self.session.get(url, headers=headers)
        json_data = resp.json()
        # print(json_data)
        statuses = json_data['data']['statuses']
        next_cursor = json_data['data']['next_cursor']
        for statuse in statuses:
            print('{},博主：{},内容：{}'.format(self.index, statuse['user']['screen_name'], statuse['text'][:10]))
            self.index += 1
        return next_cursor

    def visit_next(self, page_count):
        next_cursor = None
        for i in range(page_count):
            next_cursor=self.visit_friends(next_cursor)


if __name__ == '__main__':
    sina = SinaSpider('51508690@qq.com', 'mumu2018')
    sina.visit_start()
    sina.visit_login()
    sina.visit_friends()
    sina.visit_next(5)
