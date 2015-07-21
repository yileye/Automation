__author__ = 'v-yily'
#-*-coding:utf-8-*-
import os,sys,unittest,time
from selenium import webdriver
from test_AbstractPage import TestAbstract
from lib.base.driver_manager import DriverManager
from lib.page.Register import Register

class TestRegisterProject(TestAbstract):
    def test_register_project_admin(self):
        try:
            register = Register(self.driver)
            register.super_admin_login()
            register.register_project_admin()
        except Exception ,e:
            self.save_screenshot()
            self.fail(e.message)


