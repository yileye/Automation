__author__ = 'v-yily'
#-*-coding:utf-8-*-

import os,sys,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import ConfigParser
from AbstractPage import AbstractPage

class Register(AbstractPage):
    config = ConfigParser.ConfigParser()
    config.read('D:\pyworkspace\work\config\config.conf')
    def register_project_admin(self):
        self.driver.get('http://mtest.sinooceanland.com/MobileBusiness/MobileBusiness.ParternerPlatform.Manage2.0/Functions/ProjectEdit.aspx?prevUrl=%2fMobileBusiness%2fMobileBusiness.ParternerPlatform.Manage2.0%2fFunctions%2fProjectList.aspx%3fmenuCode%3ddc9945d6-fb12-9beb-42fa-ea3e2d09b787&menuCode=dc9945d6-fb12-9beb-42fa-ea3e2d09b787')

        self.driver.find_element_by_id('txtMarkName').send_keys(self.config.get('broker','project_name').decode('utf-8'))
        self.driver.find_element_by_id('txtName').send_keys(self.config.get('broker','project_name').decode('utf-8'))
        self.driver.find_element_by_id('txtAdminName').click()
        self.driver.find_element_by_xpath('//*[@id="txtAdminName_data"]/div')
        self.driver.find_element_by_id('txtUserName').send_keys(self.config.get('broker','realname_project').decode('utf-8'))
        self.driver.find_element_by_id('txtUserPhone').send_keys(self.config.get('broker','project_admin'))
        self.driver.find_element_by_id('txtUserPwd').send_keys(self.config.get('broker','project_pwd'))
        self.driver.find_element_by_xpath('//*[@id="txtAdminName_ext"]/center/input[1]').click()
        self.driver.switch_to_alert().accept()
        #driver.find_element_by_id('txtDisplayState').click()
        time.sleep(6)
        self.driver.find_element_by_id('btnSave').click()
        time.sleep(6)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/a[2]').click()


    #注册渠道经理
    def register_ChannelManager_admin(self):
        self.driver.find_element_by_xpath('//*[@id="menu_88a8ed9f-2e0d-8a21-49f5-19c95a164424"]/a').click()

        self.driver.find_element_by_id('txtUserName').send_keys(self.config.get('broker','realname_channel_manage').decode('utf-8'))
        # self.driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(self.config.get('broker','realname_channel_manage'))

        self.driver.find_element_by_id('txtUserPhone').send_keys(self.config.get('broker','channel_manager_admin').decode('utf-8'))

        self.driver.find_element_by_id('txtUserPwd').send_keys(self.config.get('broker','channel_manager_pwd').decode('utf-8'))
        self.driver.find_element_by_id('btnSave').click()
        self.driver.switch_to_alert().accept()
        time.sleep(2)

    #添加销售经理
    def register_SalesManager(self):
         self.driver.find_element_by_xpath('//*[@id="menu_2dd87efb-ba56-b829-458a-82afd612840d"]/a').click()
         time.sleep(2)
         self.driver.find_element_by_id('addDiv').click
         time.sleep(2)
         self.driver.find_element_by_id('addDiv_data')
         self.driver.find_element_by_id('txtRealName').send_keys(self.config.get('broker','realname_sale_manager').decode('utf-8'))
         self.driver.find_element_by_id('txtTelphone').send_keys(self.config.get('broker','sale_manager_admin').decode('utf-8'))
         self.driver.find_element_by_id('txtCompanyName').send_keys(self.config.get('broker','sale_manager_pwd').decode('utf-8'))
         time.sleep(2)
         self.driver.find_element_by_xpath('//*[@id="addDiv_ext"]/center/input[1]').click()
         time.sleep(2)

    #添加置业顾问
    def register_PropertyConsultant(self):
        self.driver.find_element_by_xpath('//*[@id="menu_6c23dd24-de8c-8169-435f-72166ccec77f"]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right_panel"]/div[1]/ul[1]/li/a').click()
        time.sleep(2)
        self.driver.find_element_by_id('addDiv_data').click()
        self.driver.find_element_by_id('txtRealName').send_keys()
        self.driver.find_element_by_id('txtTelphone').send_keys()
        self.driver.find_element_by_id('txtCompanyName').send_keys()





