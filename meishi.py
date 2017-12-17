#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:31:43 2017

@author: python
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

def search():
    browser.get('https://www.taobao.com')
    input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
    )
    submit = 