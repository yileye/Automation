__author__ = 'v-yily'
#-*-coding:utf-8-*-

#测试用例的基类，之后所有测试用例都要继承这个类
import os, sys, time, unittest
sys.path.append(r'D:\pyworkspace\work')
from lib.base.Util import Util
# from lib.page.AbstractPage import AbstractPage
from lib.base.driver_manager import DriverManager
from selenium import webdriver


class TestAbstract(unittest.TestCase):
    driver = None
    type = 'Chrome'
    config_file = os.path.dirname(os.path.dirname(__file__)) + '\config\config.conf'
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = DriverManager.getDriver(self.type)

    # def test_1(self):
    #     self.driver.get('http://www.sogou.com')
    #     time.sleep(1)
    #     self.save_screenshot()

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass

    #截图函数

    # def save_screenshot(self):
    #     dir  = Util.getConfig(self.config_file,'save_screenshot','dir_screenshot')
    #     file = dir + '/'+self.__class__.__name__+ '-'+self.__testMethodName+'.png'
    #     self.driver.save_screenshot(file)
    def save_screenshot(self):
		dir_screenshot = Util.getConfig(self.config_file,'save_screenshot','dir_screenshot')
		file_name = dir_screenshot + '/' + self.__class__.__name__ + '-' + self._testMethodName + '.png'
		self.driver.save_screenshot(file_name)



