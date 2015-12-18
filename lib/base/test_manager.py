__author__ = 'v-yily'
# -*- coding: utf-8 -*-
from new import classobj
import unittest
class TestManager:

    @staticmethod
    def getTest(clz,type):
        new_classname = str(clz.__name__) + '_' + str(type).capitalize()
        new_clz=classobj(new_classname,(clz,) , {'type':type})
        return unittest.makeSuite(new_clz)