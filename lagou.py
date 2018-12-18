#!/usr/bin/env python
# -*- coding: utf-8 -*-
# def lagou_login():
#     driver=webdriver.Chrome()
#     driver.get('https://passport.lagou.com/login/login.html')

from selenium import webdriver
from common.requests_helper import make_session
import hashlib
import re

class Lagou_login:
    def __init__(self,username,password):
        self.session=make_session()
        self.username=username
        self.password=password

    def visit_start(self):
        self.session.get('https://passport.lagou.com/login/login.html')

    def md5_password(self,password):
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        g="veenike" #找到盐
        password=g + password + g
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        return password

    def challenge(self):#找到动态值
        url='https://www.lgstatic.com/www/static/pkg/widgets_bf7295d.js'
        headers={
            'Referer':'https://www.lagou.com/'
        }
        params={
            'pt': '0',
            'gt': '66442f2f720bfc86799932d8ad2eb6c7'
        }
        resp=self.session.post(url,headers=headers,params=params).text
        print(resp)
        challenge=resp['challenge']
        return challenge

    def visit_grant(self,username,password,challenge):
        url='https://passport.lagou.com/grantServiceTicket/grant.html'
        headers={
            'Referer':'https://passport.lagou.com/login/login.html'
        }
        data={
            'isValidate': 'true',
            'username': username,
            'password': password,
            'request_form_verifyCode': '',
            'submit': '',
            'challenge': challenge
        }
        self.session.post(url,headers=headers,data=data)

    def visit_python(self,pn):
        for i in range(1,pn+1):
            pn = i
            if i==1:
                first='true'
            else:
                first='false'
            url='https://www.lagou.com/jobs/positionAjax.json?'
            headers={
                'refer':'https://www.lagou.com/jobs/list_python%20%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput='
            }
            params={
                'city': '北京',
                'needAddtionalResult': 'false'
            }
            data={
                'first': first,
                'pn': pn,
                'kd': 'python 爬虫'
            }
            resp = self.session.post(url, headers=headers, data=data,params=params).text
            work_info_text = resp['content']['positionResult']['result']
            for index,result in enumerate(work_info_text):
                print('{},职位:{},薪资:{},地点:{},公司:{}'.format(index+1,result['positionName'],result['salary'],result['district'],result['companyShortName']))

if __name__=='__main__':
    lagou=Lagou_login()
    lagou.visit_start()
    password=lagou.md5_password('kdz235711')
    challenge=lagou.challenge()
    lagou.visit_grant('15313851316',password,challenge)
    lagou.visit_python(3)