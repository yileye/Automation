__author__ = 'v-yily'
#-*-coding:utf-8-*-

import ConfigParser

class Util():
    #获取配置文件中配置内容的方法
    @staticmethod
    def getConfig(file,section,values):
        config = ConfigParser.ConfigParser()
        config.read(file)
        return  config.get(section,values)
#
#
# print Util.getConfig('D:\pyworkspace\work\config\config.conf','broker','realname')


