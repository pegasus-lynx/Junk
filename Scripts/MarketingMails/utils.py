from bs4 import BeautifulSoup as bs
import selenium as sel
import pyautogui as pyg
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from store import *

def open_browser():
    browser = webdriver.Chrome()
    browser.get(MARKETING_DRIVE)

    elem = browser.find_element_by_name("identifier")
    elem.send_keys("dipesh.kumar.cse17@itbhu.ac.in")
    elem = browser.find_element_by_id("identifierNext")
    elem.click()

#     wait = WebDriverWait(browser, 10)
#     elem = wait.until(EC.element_to_be_selected())


    browser.implicitly_wait(20)

    elem = browser.find_element_by_xpath("//input[@name='password']")
    elem.send_keys("dkUMAR@14")
    elem = browser.find_element_by_id("passwordNext")
    elem.send_keys(Keys.RETURN)

#   First job would be how to use selenium
#   How to connect an existing session

    return browser


def make_deliverables(browser, company, pitch):
    for t in pitch:
        key = "DEL_" + t.upper()
        link = DEL_LINKS[key]
        name = DEL_NAMES[key]


        pyg.click(226,60)
        pyg.press(['ctrl','3'])
        pyg.press(['ctrl','a'])
        pyg.press('backspace')
        pyg.write(link)
        pyg.press('enter')

        time.sleep(10)

        pyg.click(46,302)
        pyg.press(['ctrl','h'])

        pyg.click(360,490)
        pyg.write("XXXXX")
        pyg.click(360,540)
        pyg.write(company)
        pyg.click(430,710)
        pyg.click(700,440)

        pyg.click(85,100)
        pyg.press(['ctrl', 'a'])
        pyg.write(name+":"+company)
        pyg.click(85,130)

        pyg.click(100,330)
        pyg.click(380,425)

        pyg.press(['ctrl', '2'])
        pyg.moveTo(128,1047)
        pyg.dragTo(542,936,button="left")

        time.sleep(10)

        pyg.click(400,400,button="right")
        pyg.click(524,548)
        pyg.click(375,680)
        pyg.click(401,435)
        pyg.click(402,663)
        pyg.click(262,415)
        pyg.click(277,785)
        pyg.click(364,468)
        pyg.click(260,734)

def create_mail(browser, company, links):
    pass

def verify(browser, company, pitch):
    pass

def delete_company_folder(company):
    pass