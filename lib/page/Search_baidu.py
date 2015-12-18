#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by  import By
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__userName"]').send_keys('695084435@qq.com')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__password"]').send_keys('1990522yle')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__submit"]').click()
baidu_cookies = driver.get_cookies()