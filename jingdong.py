#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from common.requests_helper import make_session


class JingdongSpider:
    def __init__(self):
        self.session=make_session()
        self.page=1
        self.page_count=199
        self.size_page=13

    def visit_first(self):
        self.session('https://www.jd.com/')

    def visit_huahua(self,keyword,page,page_size):
        url='https://search.jd.com/Search'
        # headers={
        #     'Referer':'https://www.jd.com/?cu=true&utm_source=www.hao123.com&utm_medium=tuiguang&utm_campaign=t_1000003625_hao123mz&utm_term=395d4f1b5d394017a1c991202d92a999'
        # }
        params={
            'keyword':keyword,
            'enc': 'utf-8',
            'wq': keyword,
            'page':page,
            's':page_size
        }
        resp=self.session(url,params=params).text
        info=re.search(r'<ul class="gl-warp clearfix" data-tpl="3">(.*?)')

    def visit_last(self):
        for i in range(1,self.page_count):
            if i%2==1:
                page=i
                page_size=(i-1)*self.size_page+1
                self.visit_huahua(page, page_size)



if __name__=='__main__':
    keyword='花花公子'
    jingdong=JingdongSpider()
    jingdong.visit_first()
    jingdong.visit_last()