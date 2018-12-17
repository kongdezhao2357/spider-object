#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from zhilian.spiders.zhilian import ZhilianSpider

settings=get_project_settings()
process=CrawlerProcess(settings=settings)

process.crawl(ZhilianSpider)
process.start()