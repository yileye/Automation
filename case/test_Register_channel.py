__author__ = 'v-yily'
#-*-coding:utf-8-*-
import os,sys,unittest,time
from selenium import webdriver
from test_AbstractPage import TestAbstract
from lib.base.driver_manager import DriverManager
from lib.page.Register import Register

class TestRegisterChannel(TestAbstract):
    def test_register_channel_admin(self):
        try:
            register = Register(self.driver)
            register.project_admin_login()
            register.register_ChannelManager_admin()
        except Exception ,e:
            self.save_screenshot()
            self.fail(e.message)