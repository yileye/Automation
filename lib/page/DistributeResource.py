__author__ = 'v-yily'
# -*- coding: utf-8 -*-
import os,sys,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from AbstractPage import AbstractPage
import random

class DistributeResource(AbstractPage):
    #分配客户给销售经理
    def distribute_sale(self):
        self.driver.find_element_by_xpath('//*[@id="menu_2dd87efb-ba56-b829-458a-82afd612840d"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="right_panel"]/div[1]/ul[2]/li/a').click()
        self.driver.find_element_by_xpath('//*[@id="d03450fe-91b2-b67f-4666-b37e28d71168"]').click()
        self.driver.find_element_by_xpath('//*[@id="add"]').click()
        li = self.driver.find_element_by_xpath('//*[@id="ddlHomeConsultant_list"]')
        print li
        time.sleep(2)
        all_li  = li.find_elements_by_tag_name('li')
        print all_li
        len_li = len(all_li)
        index  = random.randint(1,len_li)
        self.driver.find_element_by_xpath('//*[@id="ddlHomeConsultant"]/p').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="ddlHomeConsultant_list"]/li'+'['+str(index)+']'+'\'').click()

        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="txtHomeConsultant_ext"]/center/input[1]').click()


        #分配客户给置业顾问
        def distribute_properties(self):
            self.driver.find_element_by_xpath('//*[@id="right_panel"]/div[1]/ul[2]/li/a').click()
            self.driver.find_element_by_xpath('//*[@id="467c2f47-0b2f-ae93-4bd3-790d30f8d7d0"]').click()
            self.driver.find_element_by_id('add').click()
            self.driverfind_element_by_xpath('//*[@id="txtHomeConsultant_data"]')
            self.driver.find_element_by_xpath('//*[@id="ddlHomeConsultant_list"]')
            li = self.driver.find_element_by_id('id="ddlHomeConsultant_list"')
            time.sleep(2)
            all_li  = li.find_elements_by_tag_name('li')
            len_li = len(all_li)
            index  = random.randint(1,len_li)
            self.driver.find_element_by_xpath(' //*[@id="ddlHomeConsultant_list"]/li['+str(index)+']''').click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="txtHomeConsultant_ext"]/center/input[1]').click()


