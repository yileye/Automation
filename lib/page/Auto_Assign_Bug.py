#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()            #窗口最大化，更多元素暴露出来
driver.get('http://127.0.0.1/zentao/bug-browse.html')
time.sleep(2)

driver.find_element_by_id('account').send_keys('cmtest1')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_id('submit').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="bugList"]/tbody/tr[1]/td[9]/a[2]/i').click()
time.sleep(1)
driver.switch_to_frame('modalIframe')
driver.find_element_by_xpath('//*[@id="assignedTo_chosen"]/a/div').click()
driver.find_element_by_xpath('//*[@id="assignedTo_chosen"]/div/div/input').send_keys('测试二'.decode('utf-8'))
driver.find_element_by_xpath('//*[@id="assignedTo_chosen"]/div/div/input').send_keys(Keys.ENTER)
driver.find_element_by_id('submit').click()
time.sleep(1)
driver.switch_to_default_content()

driver.quit()
