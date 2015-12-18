#-*-coding:utf-8-*-
import unittest
import urllib,json
import random

class TestUserInfo(unittest.TestCase):
    server_url='http://127.0.0.1:8972/'

    def test_userinfo_get_1(self):
        url = self.server_url + 'userinfo/get?'
        params = urllib.urlencode({'uid':1})
        res = urllib.urlopen(url + params).read()
        res = json.loads(res)
        print res['data'][0]['uid']
        self.assertEqual(0,res['errno'])
        self.assertEqual('',res['errmsg'])
        self.assertEqual(1,int(res['data'][0]['uid']))

    def test_userinfo_get_2(self):
        url = self.server_url+'userinfo/get?'
        params = urllib.urlencode({'uil':3})
        res = urllib.urlopen(url+params).read()
        res = json.loads(res)
        print res
