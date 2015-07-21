__author__ = 'v-yily'
#-*-coding:utf-8-*-

from selenium import webdriver
import time ,os,sys
import ConfigParser
sys.path.append(r'D:\pyworkspace\work')
from lib.base.Util import Util
class AbstractPage(object):

    driver= None
    url = ''
    config_file = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\config\config.conf' #用os.path.dirname定位配置文件的绝对路径
    #print config_file
    super_admin = {}
    channel_manager_admin = {}
    Property_consultant_admin = {}

    def __init__(self,driver):
        self.driver = driver
        self.url = Util.getConfig(self.config_file,'broker','url')

        #获取用户的用户名，密码，昵称信息
        self.super_admin = self.getUser('super')
        self.project_admin = self.getUser('project')
        self.channel_manager_admin = self.getUser('channel_manager')



    def login(self,username,password):
        self.driver.get('http://mtest.sinooceanland.com/MobileBusiness/MobileBusiness.Manage.PassportService/Anonymous/SignInPage.aspx?ru=http%3a%2f%2fmtest.sinooceanland.com%2fMobileBusiness%2fMobileBusiness.ParternerPlatform.Manage2.0%2fFunctions%2fDefaut.aspx%3fmenuCode%3d&to=-2&aid=WaChatWebSite&ip=10.2.34.71&lou=http%3a%2f%2fmtest.sinooceanland.com%2fMobileBusiness%2fMobileBusiness.ParternerPlatform.Manage2.0%2fMCSAuthenticateLogOff.axd&m=HttpPost')
        self.driver.find_element_by_id('txtUserInfo').clear()
        self.driver.find_element_by_id('txtUserInfo').send_keys(username)
        self.driver.find_element_by_id('txtPassword').clear()
        self.driver.find_element_by_id('txtPassword').send_keys(password)
        self.driver.find_element_by_id('btnLogin').click()
        time.sleep(3)


    def super_admin_login(self):
        self.login(self.super_admin['username'], self.super_admin['password'])

    #项目管理员登录
    def project_admin_login(self):
        self.login(self.project_admin['username'], self.project_admin['password'])

    #渠道经理登录
    def channel_manager_login(self):
        self.login(self.channel_manager_admin['username'], self.channel_manager_admin['password'])


    #置业顾问登录
    def Property_consultant_login(self):
        self.login(self.Property_consultant_admin['username'], self.Property_consultant_admin['password'])

    #获取帐号信息，返回列表
    def getUser(self,type = 'super'):
        user = {}
        user['username'] = Util.getConfig(self.config_file,'broker',type+'_admin')
        user['password'] = Util.getConfig(self.config_file,'broker',type+'_pwd')
        #print user
        return user




