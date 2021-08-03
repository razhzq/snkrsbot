# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:51:39 2020

@author: Loga
"""

from selenium import webdriver

driver = webdriver.Chrome(C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe)
#driver = webdriver.Firefox()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name('q').send_keys('Automation Step by Step')
driver.find_element_by_name('btnK').click()
time.sleep(4)
driver.quit()

