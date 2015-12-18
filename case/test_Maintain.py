__author__ = 'v-yily'
#-*-coding:utf-8-*-
import os,sys,unittest,time
from selenium import webdriver
from test_AbstractPage import TestAbstract
from lib.base.driver_manager import DriverManager
from lib.page.Register import Register
from lib.page.Maintain import Maintain
class TestMaintain(TestAbstract):
    def test_data(self):
        try:
            maintain = Maintain(self.driver)
            maintain.channel_manager_login()
            maintain.maintain_data()
        except Exception ,e:
            self.save_screenshot()
            self.fail(e.message)

