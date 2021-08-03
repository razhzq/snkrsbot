# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:41:13 2020

@author: Loga
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')
sd = ''

    
def submit_order_time():
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
        return sd
        
        
        


def login():
        driver.get("https://www.nike.com/my/launch")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('aidilrzk12@gmail.com')
        time.sleep(3)
        driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Suzanna1')
        time.sleep(5)
        driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
        time.sleep(8)
       
def early_links():
    driver.get("https://www.nike.com/my/launch/t/air-jordan-1-dark-mocha?size=9&productId=94fc30a5-9916-50d5-8519-8f0903058887")
    time.sleep(8)

def early_link_success():
    early = driver.find_element_by_xpath('// *[@id="firstName"]').is_displayed()
    if early == True:
        return True
    else:
        return False



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
         time.sleep(2)
      
  
def submit_order():
        while datetime.datetime.now() < sd:
         time.sleep(1)
         driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
         return
    
    
def consent_box():
    driver.find_element_by_class_name('gdpr-consent').find_element_by_class_name('gdprConsentCheckbox').find_element_by_class_name("checkmark").click()
    time.sleep(2)
    


def consent_status():
    element = driver.find_element_by_class_name('gdpr-consent').find_element_by_class_name('gdprConsentCheckbox').find_element_by_xpath('//label[@ class="container"]').is_displayed()
    if element == False:
        return False
    else:
        return True
          
def delete_cache():
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData')
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.switch_to.window(driver.window_handles[0]) # switch back





