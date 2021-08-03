# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:49:15 2021

@author: Loga
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, datetime

driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')

year=int(input("year: "))
mm=int(input("Enter Month: "))
dt=int(input("Enter Date: "))
hr=int(input("Enter Hour: "))
mins=int(input("Enter Mins: "))
secs=int(input("Enter Seconds: "))
milsec=int(input("Enter Mili Secs: "))

class Submit():    
    def sd(self):
        self.yy=year
        self.mm=mm
        self.dt=dt
        self.hr=hr
        self.mins=mins
        self.secs=secs
        self.milsec=milsec
        
        sd = datetime.datetime(self.yy, self.mm, self.dt, self.hr, self.mins, self.secs, self.milsec)
        while datetime.datetime.now() < sd:  
         time.sleep(1)

         driver.find_element_by_xpath('//button[@ class="button-submit"]').click()

def login():
        driver.get("https://www.nike.com/my/launch")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('tanlt4896@gmail.com')
        time.sleep(3)
        driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Nike1111')
        time.sleep(5)
        driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
        time.sleep(8)
        driver.get("https://www.nike.com/my/launch/t/air-jordan-1-dark-mocha?size=9&productId=94fc30a5-9916-50d5-8519-8f0903058887")
        time.sleep(8)
        
  
def delivery_add():
        driver.find_element_by_xpath('// *[@id="firstName"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
        time.sleep(2)
        driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
        time.sleep(2)
        driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('35,Jalan Putra Indah 9/22')  #id="addressLine1"
        time.sleep(2)
        driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Putra Heights,Selangor') # id="addressLine2"  id="postCode"  id="locality"
        time.sleep(2)
        driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47650') 
        time.sleep(2)
        driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Subang Jaya') 
        time.sleep(2)
        select = Select(driver.find_element_by_id('state'))
        select.select_by_visible_text('Kuala Lumpur')
        time.sleep(2)
        driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
        time.sleep(2)
        driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
        time.sleep(2)
        driver.find_element_by_xpath('//button[@ class="button-continue"]').click()      
        
   
def payment_card():
         time.sleep(2)   
         driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
         time.sleep(2)
         driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('4283322042240935')   
         time.sleep(2)
         driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("1222")         
         time.sleep(2)     
         driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("268")                                
         time.sleep(2)
         driver.switch_to_default_content()
         time.sleep(2)
         driver.find_element_by_xpath('//button[@ class="button-continue"]').click()
      

def consent_status():
    time.sleep(2)
    element = driver.find_element_by_class_name('gdpr-consent').find_element_by_class_name('gdprConsentCheckbox').find_element_by_class_name('container')
    time.sleep(2)
    if element.get_attribute('container isChecked') :
        pass
    elif element.get_attribute('container'):
        driver.find_element_by_class_name('gdpr-consent').find_element_by_class_name('gdprConsentCheckbox').find_element_by_class_name("checkmark").click()
        time.sleep(2)
        pass
    
    
    #https://www.nike.com/my/launch/t/air-force-1-valentines-day?size=9&productId=67aca436-e2c6-5b52-83bb-70f1b15d08de