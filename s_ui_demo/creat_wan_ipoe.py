import mylib.lib
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


PATH = "C:/Users/Teddy/Desktop/chromedriver/chromedriver.exe"
IP = "http://192.168.1.1/"
DefaultUserName = "root"
DefaultPassword = "QWERTYU1"
delay = 3

driver = webdriver.Chrome(PATH)
driver.get(IP)
driver.maximize_window()
time.sleep(1)

mylib.lib.ui_login(driver,DefaultUserName,DefaultPassword)
time.sleep(delay)


mylib.lib.create_wan(driver)
time.sleep(delay)


