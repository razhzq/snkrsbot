# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 12:42:44 2021

@author: Loga
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time, datetime
import logging
import threading
import time



year_date = input('Enter year: ')
month_date = input('Enter month: ')
datedate = input('Enter date: ')
hourhour = input('hour:')
mints = input('minutes: ')
sec = input('seconds: ')
msec = input('milli seconds: ')

yy = int(year_date) 
mm = int(month_date)
dd = int(datedate)
hh = int(hourhour)
mins = int(mints)
secs = int(sec)
milsecs = int(msec)

sd = datetime.datetime(yy, mm, dd, hh, mins, secs, milsecs)


def first_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')
#Hazeem.290902

  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('hazeem.iiskd@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Hazeem.290902')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18")
  time.sleep(8)
  #https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Hazeem')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Zed')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('no.27, Jalan Villa Putra 2')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Sg Buloh, Selangor') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Sungai Buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Selangor')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  except NoSuchElementException:
      
     time.sleep(2)   
     driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
     time.sleep(2)
     driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032127616486')   
     time.sleep(2)
     driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("0725")         
     time.sleep(2)     
     driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("604")                                
     time.sleep(2)
     driver.switch_to_default_content()
     time.sleep(2)
     driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
     
  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
  
  
def second_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')


  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('aquaville2471@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Hazeem.290902')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18")
  time.sleep(8)
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('no.27, Jalan Villa Putra 2 JX')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Sg Buloh, Selangor') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys(' Sungai Buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Kuala Lumpur')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
      time.sleep(2)  
  
  except NoSuchElementException:
      
      driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
      time.sleep(2)
      driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032127616486')   
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("0725")         
      time.sleep(2)     
      driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("604")                                
      time.sleep(2)
      driver.switch_to_default_content()
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()

  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
  
def third_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')


  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('roslina@arcitex.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Hazeem.290902')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18")
  time.sleep(8)
  #https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('no.27, Jalan Villa Putra 2, HV')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys(' Sg Buloh, Selangor') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Sungai Buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Kuala Lumpur')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  except NoSuchElementException:
      
     time.sleep(2)   
     driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
     time.sleep(2)
     driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032127616486')   
     time.sleep(2)
     driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("0725")         
     time.sleep(2)     
     driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("604")                                
     time.sleep(2)
     driver.switch_to_default_content()
     time.sleep(2)
     driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
     
  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
    
def fourth_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')


  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('ariennasofea20@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Hazeem.290902')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/air-jordan-1-dark-mocha?size=9&productId=94fc30a5-9916-50d5-8519-8f0903058887")
  time.sleep(8)
  #https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('no.27, Jalan Villa Putra 2 GB')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Sg Buloh, Selangor') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Sungai Buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Kuala Lumpur')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  except NoSuchElementException:
      
     time.sleep(2)   
     driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
     time.sleep(2)
     driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032127616486')   
     time.sleep(2)
     driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("0725")         
     time.sleep(2)     
     driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("604")                                
     time.sleep(2)
     driver.switch_to_default_content()
     time.sleep(2)
     driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
     
  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()  
 
def fifth_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')


  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('aqildanish384@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Hazeem.290902')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18")
  time.sleep(8)
  #https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('no.27, Jalan Villa Putra 2 BX')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Sg Buloh, Selangor') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Sungai Buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Kuala Lumpur')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  except NoSuchElementException:
      
     time.sleep(2)   
     driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
     time.sleep(2)
     driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032127616486')   
     time.sleep(2)
     driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("0725")         
     time.sleep(2)     
     driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("604")                                
     time.sleep(2)
     driver.switch_to_default_content()
     time.sleep(2)
     driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
     
  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()   
  
def six_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')


  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('muqhrizmarzuki@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Hazeem.290902')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18")
  time.sleep(8)
  #https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('no.27, Jalan Villa Putra 2 DC')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys(' Sg Buloh, Selangor') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Sungai Buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Kuala Lumpur')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  except NoSuchElementException:
      
     time.sleep(2)   
     driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
     time.sleep(2)
     driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032088637349')   
     time.sleep(2)
     driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("1223")         
     time.sleep(2)     
     driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("869")                                
     time.sleep(2)
     driver.switch_to_default_content()
     time.sleep(2)
     driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
     
  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
  
def seven_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')


  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('zedzariman@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Hazeem.290902')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18")
  time.sleep(8)
  #https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('no.27, Jalan Villa Putra 2 JJ')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys(' Sg Buloh, Selangor,') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Sungai buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Kuala Lumpur')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  except NoSuchElementException:
      
     time.sleep(2)   
     driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
     time.sleep(2)
     driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032088637349')   
     time.sleep(2)
     driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("1223")         
     time.sleep(2)     
     driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("869")                                
     time.sleep(2)
     driver.switch_to_default_content()
     time.sleep(2)
     driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
     
  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
  
def eight_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')


  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('luqman.haz@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Hazeem.290902')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18")
  time.sleep(8)
  #https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys(' no.27, Jalan Villa Putra 2,KD')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Sg Buloh, Selangor') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Sungai Buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Kuala Lumpur')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  except NoSuchElementException:
      
     time.sleep(2)   
     driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
     time.sleep(2)
     driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032088637349')   
     time.sleep(2)
     driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("1223")         
     time.sleep(2)     
     driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("869")                                
     time.sleep(2)
     driver.switch_to_default_content()
     time.sleep(2)
     driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
     
  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
  
def ninth_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')


  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('aidilrzk12@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Suzanna1')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18")
  time.sleep(8)
  #https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('no.27, Jalan Villa Putra 2 TY')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Sg Buloh, Selangor') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Sungai Buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Kuala Lumpur')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  except NoSuchElementException:
      
     time.sleep(2)   
     driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
     time.sleep(2)
     driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032088637349')   
     time.sleep(2)
     driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("1223")         
     time.sleep(2)     
     driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("869")                                
     time.sleep(2)
     driver.switch_to_default_content()
     time.sleep(2)
     driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
     
  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
  
def tenth_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')


  driver.maximize_window()
  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('itstiafarisha@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('@Nniikkee99')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18")
  time.sleep(8)
  #https://www.nike.com/my/launch/t/dunk-low-black?size=9&productId=d08c6e4f-777d-53eb-88ed-e6705d8feb18
  try:
      
      driver.find_element_by_xpath('// *[@id="firstName"]').click()
      time.sleep(2)
      driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('no.27, Jalan Villa Putra 2 DX')  #id="addressLine1"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Sg Buloh, Selangor') # id="addressLine2"  id="postCode"  id="locality"
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47000') 
      time.sleep(2)
      driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Sungai Buloh') 
      time.sleep(2)
      select = Select(driver.find_element_by_id('state'))
      select.select_by_visible_text('Kuala Lumpur')
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
      time.sleep(2)
      driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
      time.sleep(2)
      driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  except NoSuchElementException:
      
     time.sleep(2)   
     driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
     time.sleep(2)
     driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('5196032088637349')   
     time.sleep(2)
     driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("1223")         
     time.sleep(2)     
     driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("869")                                
     time.sleep(2)
     driver.switch_to_default_content()
     time.sleep(2)
     driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
     
  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
  
t1 = threading.Thread(target=first_account)
t2 = threading.Thread(target=second_account)
t3 = threading.Thread(target=third_account)
t4 = threading.Thread(target=fourth_account)
t5 = threading.Thread(target=fifth_account)
t6 = threading.Thread(target=six_account)
t7 = threading.Thread(target=seven_account)
t8 = threading.Thread(target=eight_account)
t9 = threading.Thread(target=ninth_account)
t10 = threading.Thread(target=tenth_account)



t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
  