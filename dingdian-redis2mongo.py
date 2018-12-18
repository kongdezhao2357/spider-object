#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import pymongo
import redis


def redis2mongo():
    client=pymongo.MongoClient(host='127.0.0.1',port=27017)
    db=client['dingdian']
    coll=db['novel_info']

    redis_conn=redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)

    while 1:
        item=redis_conn.lpop('dingdian:items')
        item=json.loads(item)
        coll.insert(item)
        if not item:
            break
    client.close()

if __name__=='__main__':
    redis2mongo()