__author__ = 'v-yily'
# -*- coding: utf-8 -*-
import os,sys,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from AbstractPage import AbstractPage
import random
class Maintain(AbstractPage):

    def maintain_data (self):
        #随机选省
        option = self.driver.find_element_by_id('txtProvice')
        time.sleep(2)
        all_option  = option.find_elements_by_tag_name('option')
        len_Provice = len(all_option)
        index  = random.randint(1,len_Provice)-1
        # all_option[index].text
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="txtProvice"]/option['+str(index)+']''').click()
        time.sleep(1)
        #随机选市
        option = self.driver.find_element_by_id('txtCity')
        time.sleep(2)
        all_option  = option.find_elements_by_tag_name('option')
        len_City = len(all_option)
        index  = random.randint(1,len_City)
        # all_option[index].text
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="txtCity"]/option['+str(index)+']''').click()
        time.sleep(1)
        #随机选区
        option =self. driver.find_element_by_id('txtCounty')
        time.sleep(2)
        all_option  = option.find_elements_by_tag_name('option')
        len_County = len(all_option)
        index  = random.randint(1,len_County)

        County = all_option[index].text
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="txtCounty"]/option['+str(index)+']''').click()
        time.sleep(1)
        self.driver.find_element_by_id('txtDetailAddress').send_keys('\''+County+'\''.decode('utf-8'))
        time.sleep(3)

        self.driver.find_element_by_id('txtCompanyName').send_keys('远洋地产'.decode('utf-8'))
        self.driver.find_element_by_id('txtMembershipName').send_keys('远洋地产'.decode('utf-8'))
        self.driver.execute_script("window.scrollBy(0,200)","")
        self.driver.find_element_by_id('txtBusinessLicense').send_keys('1000000')
        self.driver.find_element_by_id('txtBusinessLicenseImg').send_keys('C:\Users\Public\Pictures\Sample Pictures\kaola.jpg')
        time.sleep(6)
        self.driver.find_element_by_id('txtOrganizationCode').send_keys('1000001')
        self.driver.find_element_by_id('txtOrganizationImg').send_keys('C:\Users\Public\Pictures\Sample Pictures\kaola.jpg')
        time.sleep(3)

        self.driver.find_element_by_id('txtCommissionRate').send_keys('100000')
        self.driver.find_element_by_xpath('//*[@id="Ruledata"]/tr/td[2]/select/option[5]').click()
        self.driver.find_element_by_xpath('//*[@id="Ruledata"]/tr/td[3]/select/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="Ruledata"]/tr/td[4]/input').send_keys('52000')
        self.driver.execute_script("window.scrollBy(0,200)","")

        self.driver.find_element_by_xpath('//*[@id="txtTotalPriceRange"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="txtRoomRange"]/option[3]').click()
        self.driver.find_element_by_id('txtAreaRrangeStart').send_keys('50')
        self.driver.find_element_by_id('txtAreaRrangeEnd').send_keys('200')
        self.driver.execute_script("window.scrollBy(0,200)","")

        self.driver.find_element_by_id('txtFirstPic1').send_keys('C:\Users\Public\Pictures\Sample Pictures\kaola.jpg')
        time.sleep(3)
        self.driver.find_element_by_id('txtFirstSmallPic').send_keys('C:\Users\Public\Pictures\Sample Pictures\kaola.jpg')
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,200)","")
        self.driver.execute_script("window.scrollBy(0,200)","")
        self.driver.find_element_by_id('txtSurveyTitle').send_keys('项目开张啦'.decode('utf-8'))
        self.driver.find_element_by_id('txtSurveyTel').send_keys('400-800-4569')
        self.driver.execute_script("window.scrollBy(0,200)","")
        self.driver.find_element_by_id('txtSurveyAvgMoney').send_keys('12100')
        self.driver.execute_script("window.scrollBy(0,200)","")
        self.driver.find_element_by_id('txtSurveyChartPic').send_keys('C:\Users\Public\Pictures\Sample Pictures\kaola.jpg')
        time.sleep(6)
        self.driver.execute_script("window.scrollBy(0,200)","")
        self.driver.find_element_by_id('txtSurveyActivity').send_keys('项目开张啦'.decode('utf-8'))
        self.driver.find_element_by_id('txtSurveyExplain').send_keys('项目开张啦'.decode('utf-8'))
        self.driver.find_element_by_id('txtSurveyIntroduction').send_keys('项目开张啦'.decode('utf-8'))
        self.driver.execute_script("window.scrollBy(0,200)","")


        self.driver.find_element_by_id('txtLocationTitle').send_keys('项目开张啦'.decode('utf-8'))
        self.driver.find_element_by_id('txtLocationPic').send_keys('C:\Users\Public\Pictures\Sample Pictures\kaola.jpg')
        time.sleep(3)
        self.driver.find_element_by_id('txtLocationExplain').send_keys('远洋地产'.decode('utf-8'))
        self.driver.execute_script("window.scrollBy(0,200)","")

        self.driver.find_element_by_id('txtFeatureTitle').send_keys('远洋地产'.decode('utf-8'))
        self.driver.find_element_by_id('txtFeaturePic').send_keys('C:\Users\Public\Pictures\Sample Pictures\kaola.jpg')
        time.sleep(3)
        self.driver.find_element_by_id('txtFeatureApartmentPic').send_keys('C:\Users\Public\Pictures\Sample Pictures\kaola.jpg')
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,200)","")
        self.driver.find_element_by_id('txtFeatureIntroduction').send_keys('远洋地产'.decode('utf-8'))
        #driver.find_element_by_id('btnSave').click()
        time.sleep(3)
    #审核项目
    def audit_data(self):
        self.driver.find_element_xpath('//*[@id="menu_8ef9a795-1fc4-89f8-41ac-c81ebb1d7252"]/a').click()
        self.driver.execute_script("window.scrollBy(0,10000)","")
        self.driver.find_element_id('txtAuditResult').send_keys('同意'.decode('utf-8'))
        self.driver.find_element_id('btnAuditSuccess')
        #self.driver.find_element_id('btnAuditNoSuccess')
        self.driver.switch_to_alert().accept()



