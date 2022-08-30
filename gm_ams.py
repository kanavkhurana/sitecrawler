import json
import requests
import bs4
import sys 
import smtplib, ssl

from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time

def sendemail1(month):
  smtp_server = "smtp.gmail.com"    
  port = 587  
  
  password = 'fmzburlxtqfcyhcp'
  sender_email = "kanavkhurana@gmail.com"
  context = ssl.create_default_context()
  try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls() # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    
    receiver_email = "kanavkhurana@gmail.com"
    header='To:'+receiver_email+'\n'+'From:' \
    +sender_email+'\n'+'subject:slot found\n'
    message = "Slot found for " + month
    message = header + message
    server.sendmail(sender_email, receiver_email, message)

  except Exception as e:
        # Print any error messages to stdou
        print(e)
  finally:
    server.quit() 

def sendemail2(month):
    msg = EmailMessage()

    msg['Subject'] = "Slot found for " + month + ". go to https://oap.ind.nl/oap/en/#/doc"
    msg['From'] = 'kanavkhurana@gmail.com'
    msg['To'] = 'kanavkhurana@gmail.com'
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


url = 'https://oap.ind.nl/oap/en/#/doc'

#commented this
#driver = webdriver.Firefox()
driver = webdriver.PhantomJS()
driver.get(url)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "desk"))
    )
finally:
    select = Select(driver.find_element_by_id('desk'))
    #AMS
    select.select_by_value('1: Object')
    #Den haag
    #select.select_by_value('2: Object')
    
    try:
        availableSlot = driver.find_element(By.CSS_SELECTOR, '.available')
        month = driver.find_element(By.CSS_SELECTOR,'strong')
        print('slot available in', month.text)
        sendemail1(month.text)
        driver.quit()
        
        sys.exit()
    except NoSuchElementException:
        nextbutton = driver.find_element(By.CSS_SELECTOR, '.btn-sm.pull-right')
        nextbutton.click()
        #in august
        try:
            availableSlot = driver.find_element(By.CSS_SELECTOR, '.available')
            month = driver.find_element(By.CSS_SELECTOR,'strong')
            print('slot available in', month.text)
            sendemail1(month.text)
            driver.quit()

            sys.exit()
        except NoSuchElementException:
            nextbutton = driver.find_element(By.CSS_SELECTOR, '.btn-sm.pull-right')
            nextbutton.click()
            #in sep
        try:
            availableSlot = driver.find_element(By.CSS_SELECTOR, '.available')
            month = driver.find_element(By.CSS_SELECTOR,'strong')
            print('slot available in', month.text)
            sendemail1(month.text)
            driver.quit()

            sys.exit()
        except NoSuchElementException:
            nextbutton = driver.find_element(By.CSS_SELECTOR, '.btn-sm.pull-right')
            nextbutton.click()
            #in oct
        try:
            availableSlot = driver.find_element(By.CSS_SELECTOR, '.available')
            month = driver.find_element(By.CSS_SELECTOR,'strong')
            print('slot available in', month.text)
            sendemail1(month.text)
            driver.quit()

            sys.exit()
        except:
            print('no slots available')
        finally:
            print('no slots available')
