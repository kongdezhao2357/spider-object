#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from requests.cookies import RequestsCookieJar
from selenium.webdriver.common.by import By

def get_driver():
    driver=webdriver.Chrome()
    return driver

def input_clear_send_keys(driver,by_type,by_value,keys):
    ele=driver.find_element(by_type,by_value)
    ele.clear()
    ele.send_keys(keys)

def baidu_login(driver,username,password):
    driver.get('http://www.baidu.com')
    time.sleep(0.5)
    # driver.find_elements_by_name('tj_login')[1].click()
    driver.find_element_by_xpath('//*[@id="u1"]/a[@name="tj_login"]').click()
    time.sleep(0.5)
    driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
    time.sleep(0.5)
    input_clear_send_keys(driver,By.ID,'TANGRAM__PSP_10__userName',username)
    input_clear_send_keys(driver,By.ID,'TANGRAM__PSP_10__password',password)
    driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
    # time.sleep(1.5)
    # driver.find_element_by_id('TANGRAM__36__button_send_mobile').click()
    # time.sleep(30)
    # driver.find_element_by_id('TANGRAM__36__button_submit').click()

def save_cookies(driver,file_path):
    with open(file_path,'w',encoding='utf-8')as f:
        import json
        json.dump(driver.get_cookies(),f)

if __name__=='__main__':
    driver=get_driver()
    baidu_login(driver,'51508690@qq.com','mumu2018')
    time.sleep(0.5)
    save_cookies(driver,'save_baidu_login_cookies.txt')
    driver.quit()

