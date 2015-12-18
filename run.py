__author__ = 'v-yily'

#coding:utf-8
import os,shutil
import unittest
import xmlrunner
from lib.base.Util import Util
from lib.base.test_manager import TestManager
from case.test_Register_project import TestRegisterProject
from case.test_Register_channel import TestRegisterChannel
from case.test_Maintain import TestMaintain

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestManager.getTest(TestRegisterProject,'Chrome'))
    suite.addTest(TestManager.getTest(TestRegisterChannel,'Chrome'))
    suite.addTest(TestManager.getTest(TestMaintain,'Chrome'))
    dir_screenshot = Util.getConfig('config/config.conf','save_screenshot','dir_screenshot')
    if(os.path.exists(dir_screenshot)):
        shutil.rmtree(dir_screenshot)
    os.mkdir(dir_screenshot)

    if(os.path.exists(os.path.dirname(__file__) + '/test-reports')):
        shutil.rmtree(os.path.dirname(__file__) + '/test-reports')
    runner = xmlrunner.XMLTestRunner(output='test-reports',verbose = 1)
    runner.run(suite)
