#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    driver=webdriver.Chrome()
    return driver

def input_clear_send_keys(driver,by_type,by_value,keys):
    ele=driver.find_element(by_type,by_value)
    ele.clear()
    ele.send_keys(keys)

def login(driver,username,password):
    driver.get('https://passport.weibo.cn/signin/login')
    time.sleep(0.5)
    input_clear_send_keys(driver,By.ID,'loginName',username)
    time.sleep(0.5)
    input_clear_send_keys(driver,By.ID,'loginPassword',password)
    time.sleep(0.5)
    driver.find_element_by_id('loginAction').click()

def get_cookies(driver,file_path):
    with open(file_path,'w')as f:
        import json
        json.dump(driver.get_cookies(),f)


if __name__=='__main__':
    driver=get_driver()
    login(driver,'51508690@qq.com','mumu2018')
    get_cookies(driver,'weibo_co.txt')