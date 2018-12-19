#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import quote

from common.requests_helper import make_session
from common.util import get_13_time


class Toutiao:
    def __init__(self):
        self.session=make_session()

    def visit_first(self):
        self.session.get('https://www.toutiao.com/')

    def visit_ex(self):
        url='https://p.tanx.com/ex?i=mm_32479643_3494618_56064454'
        headers={
            'Referer':'https://www.toutiao.com/'
        }
        self.session.get(url,headers=headers)

    def visit_content(self,keyword):
        url='https://www.toutiao.com/search_content/'
        headers={
            'Referer':'https://www.toutiao.com/search/?keyword=%E9%9B%BE%E6%8E%A8%E7%90%86'
        }
        params={
            'offset': '0',
            'format': 'json',
            'keyword': quote(keyword),
            'autoload': 'true',
            'count': '20',
            'cur_tab': '1',
            'from': 'search_tab',
            'pd': 'synthesis'
        }
        resp=self.session.get(url,headers=headers,params=params)
        json_data=resp.json()

    def visit_article(self):
        t=get_13_time()
        url='https://www.toutiao.com/c/user/article/'
        headers={
            'Referer':'https://www.toutiao.com/c/user/56654489607/'
        }
        params={
            'page_type': '1',
            'user_id': '56654489607',
            'max_behot_time':t,
            'count': '20',
            'as': 'A105DCF003A4247',
            'cp': '5C035412A4A72E1',
            '_signature': 'aSGH2hAYNSY-Fs-BeDJWyWkhh8'
        }
        resp=self.session.get(url, headers=headers, params=params)
        json_info=resp.json()

        print()


if __name__=='__main__':
    toutiao=Toutiao()
    keyword='雾推理'
    toutiao.visit_first()
    toutiao.visit_ex()
    toutiao.visit_content(keyword)
    toutiao.visit_article()
