#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy

from zhilian.items import ZhilianItem


class ZhilianSpider(scrapy.Spider):
    name='zhilian'
    start_urls=['https://www.zhaopin.com/']

    def parse(self,response):
        keyword=self.settings['KEYWORD']
        for page in range(1,5):
            url=f'https://sou.zhaopin.com/?p={page}&jl=530&kw={keyword}&kt=3'
            yield scrapy.Request(url,callback=self.parse_list,meta={'keyword':keyword})

    def parse_list(self,response):
        resp=response.text
        title=resp.xpath('div[@class="contentpile__content__wrapper__item clearfix]//span[@class="contentpile__content__wrapper__item__info__box__jobname__title]/@title"').extract()
        company=resp.xpath('div[@class="contentpile__content__wrapper__item clearfix]//a[@class="contentpile__content__wrapper__item__info__box__cname__title company_title]/text()"').extract()
        item=ZhilianItem()
        item['title']=title
        item['company']=company
        yield item