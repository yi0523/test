import time
from xml.sax import default_parser_list
import selenium
import os
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from mylib.html_markup import *

delay = 3
log = time.strftime('\n::::: %Y/%m/%d_%H:%M:%S ')


def ui_login(driver, un, pw):
    driver.find_element(By.ID, 'username').clear()
    driver.find_element(By.ID, 'username').send_keys(un)
    driver.find_element(By.ID, 'password').clear()
    driver.find_element(By.ID, 'password').send_keys(pw)
    driver.find_element(By.ID, 'loginbutton').click()
    print(log ,'.....login')


def click_dropdown_menu(driver, markup = DROPDOWN_Network):
    driver.find_element("xpath", markup).click()
    time.sleep(1)
    driver.find_element("link text", "Connection").click()
    time.sleep(delay)


def create_wan(driver):

    click_dropdown_menu(driver)

    driver.find_element(By.ID, "wan_ifs").click()
    dropdown = driver.find_element(By.ID, "wan_ifs")
    dropdown.find_element(By.XPATH, "//option[. = '[ Create New PVC ]']").click()
    driver.find_element(By.ID, "wan_conn_name").click()
    driver.find_element(By.ID, "wan_conn_name").send_keys("new")
    driver.find_element(By.ID, "vlan_id").click()
    driver.find_element(By.ID, "vlan_id").send_keys("400")
    driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(29) .btn").click()
    print(log ,'.....creat a new wan successfully')
    time.sleep(delay*2)

    driver.find_element(By.CSS_SELECTOR, "#status_anchor > span").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Network").click()
    time.sleep(1)
    driver.find_element(By.ID, "wan_ifs").click()
    dropdown = driver.find_element(By.ID, "wan_ifs")
    dropdown.find_element(By.XPATH, "//option[. = 'new']").click()
    print(log ,'.....show new wan information')


