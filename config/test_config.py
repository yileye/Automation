__author__ = 'v-yily'
#-*-coding:utf-*-

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.conf')
print config.get('broker','url')
print config.get('broker','realname')
print config.get('broker','super_admin')
print config.get('broker','super_pwd')

print config.get('broker','project_admin')
print config.get('broker','project_pwd')

print config.get('broker','channel_manager_admin')
print config.get('broker','channel_manager_pwd')
