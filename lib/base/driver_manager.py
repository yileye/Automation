__author__ = 'v-yily'
#-*-coding:utf-8-*-

from selenium import webdriver

class DriverManager():
    type = 'Chrome' #默认浏览器

    @staticmethod
    def getDriver(type = None):
        if type ==None:
            type = DriverManager.type

        if type =='Chrome':
            driver = webdriver.Chrome()

        elif type =='Firefox':
            driver =webdriver.Firefox()

        elif type =='ie':
            driver = webdriver.Ie()
        else:
            raise Exception('Error_:invalid driver type:'+type)

        driver.implicitly_wait(30)
        driver.maximize_window()
        return  driver