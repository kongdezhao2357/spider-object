#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from common.requests_helper import make_session
from requests.cookies import RequestsCookieJar
from urllib.parse import unquote, quote


class BaiduIndex:
    def __init__(self):
        self.session=make_session(True)

    def load_cookies(self,file_path):
        with open(file_path)as f:
            cookies=json.load(f)
        cookies_jar=RequestsCookieJar()
        for cookie in cookies:
            cookies_jar.set(cookie['name'],cookie['value'])
        self.session.cookies=cookies_jar

    def visit_index(self):
        self.session.get('https://index.baidu.com/')

    def visit_api_route(self,keyword):
        url='https://index.baidu.com/api/Route'
        headers={
            'Referer':'https://index.baidu.com/'
        }
        # fromu='https://index.baidu.com/v2/main/index.html#/trend/{}?words={}'.format(keyword,quote(keyword))
        params={
            'fromu':'https://index.baidu.com/v2/main/index.html#/trend/{}?words={}'.format(keyword,quote(keyword))
        }

        self.session.get(url,headers=headers,params=params)

if __name__=='__main__':
    baidu_index=BaiduIndex()
    baidu_index.load_cookies('save_baidu_login_cookies.txt')
    baidu_index.visit_index()
    baidu_index.visit_api_route('黄金')
