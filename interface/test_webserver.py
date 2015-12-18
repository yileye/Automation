# -*- coding:utf-8 -*-
#编写接口自动化脚本
import unittest
import urllib,json
import random

class TestUserInfo(unittest.TestCase):  #类不是必须以test开头，但是建议以test开头，这样能很快看出是测试代码
    server_url='http://127.0.0.1:8972/'

    #getuserinfo 接口
    #查询成功，uid=1
    def test_userinfo_get_1(self):
        url = self.server_url + 'userinfo/get?'
        params = urllib.urlencode({'uid':1})
        res = urllib.urlopen(url + params).read()
        res = json.loads(res)
        self.assertEqual(0,res['errno'])
        self.assertEqual('',res['errmsg'])
        self.assertEqual(1,res['data'][0]['uid'])

    #查询成功，uid=1,2,3，其中1/2 存在，3不存在
    def test_userinfo_get_2(self):
        url = self.server_url + 'userinfo/get?'
        params = urllib.urlencode({'uid':'1,2,3'})
        res = urllib.urlopen(url + params).read()
        res = json.loads(res)
        self.assertEqual(0,res['errno'])
        self.assertEqual('',res['errmsg'])
        self.assertEqual(1,res['data'][0]['uid'])
        self.assertEqual(2,res['data'][1]['uid'])

    #查询失败，uid=''
    def test_userinfo_get_3(self):
        url = self.server_url + 'userinfo/get?'
        params = urllib.urlencode({'uid':None})
        res = urllib.urlopen(url + params).read()
        res = json.loads(res)
        self.assertEqual(999,res['errno'])
        self.assertEqual([],res['data'])

    #查询失败，uid=200 不存在
    def test_userinfo_get_4(self):
        url = self.server_url + 'userinfo/get?'
        params = urllib.urlencode({'uid':200})
        res = urllib.urlopen(url + params).read()
        res = json.loads(res)
        self.assertEqual(102,res['errno'])
        self.assertEqual('not exist user',res['errmsg'])
        self.assertEqual([],res['data'])

    #查询失败，uid='a' 是字母
    def test_userinfo_get_5(self):
        url = self.server_url + 'userinfo/get?'
        params = urllib.urlencode({'uid':'a'})
        res = urllib.urlopen(url + params).read()
        res = json.loads(res)
        self.assertEqual(999,res['errno'])
        self.assertEqual([],res['data'])



    # #setuserinfo 接口
    # def test_userinfo_set_1(self):
    #     name = 'xxx' + str(random.randint(1000,2000))
    #     url_get = self.server_url + 'userinfo/get?' + urllib.urlencode({'uid':1})
    #     url_set = self.server_url + 'userinfo/set?' + urllib.urlencode({'uid':1,'name':name})
    #     res_set = urllib.urlopen(url_set).read()
    #     res_set = json.loads(res_set)
    #     self.assertEqual(0,res_set['errno'])
    #     self.assertEqual('',res_set['errmsg'])
    #     res_get = urllib.urlopen(url_get).read()
    #     res_get = json.loads(res_get)
    #     self.assertEqual(0,res_get['errno'])
    #     self.assertEqual(name,res_get['data'][0]['name'])
