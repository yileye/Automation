uthor__ = 'lyi'

#-*-coding:utf-8-*-

import unittest

import xmlrunner



from test_webserver1 import TestUserInfo as test_userinfo_get_1




if __name__ == '__main__':

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(test_userinfo_get_1))

    #suite.addTest(unittest.makeSuite(test_userinfo_get_1))

    runner = xmlrunner.XMLTestRunner(output='test-reports')

    runner.run(suite)
