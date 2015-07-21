__author__ = 'v-yily'
#-*-coding:utf-8-*-
import os,sys,unittest,time
from selenium import webdriver
from test_AbstractPage import TestAbstract
from lib.base.driver_manager import DriverManager
from lib.page.DistributeResource import DistributeResource
class TestDistributeResource(TestAbstract):
    def test_data(self):
        try:
            distributeresource = DistributeResource(self.driver)
            distributeresource.channel_manager_login()
            distributeresource.distribute_sale()
        except Exception ,e:
            self.save_screenshot()
            self.fail(e.message)
