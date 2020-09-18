
from common.my_request import *
from common.tool import *
import unittest

class Crm_CrmUserTag(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = "https://ctest.putaoabc.net.cn/self_api/myUser/getCrmUserTag"


    def test_crmusertag1(self):
        '''我的全部用户查询条件：1所有查询条件'''
        headers = {
            'Authorization': self.token

        }

        data = {
            'type':1
        }

        res = Myrequest.get(self.url, header=headers, data=data)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))

    def test_crmusertag2(self):
        '''我的全部用户查询条件：2用户状态'''
        headers = {
            'Authorization': self.token

        }

        data = {
            'type':2
        }

        res = Myrequest.get(self.url, header=headers, data=data)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))

    def test_crmusertag3(self):
        '''我的全部用户查询条件：3跟进状态'''
        headers = {
            'Authorization': self.token

        }

        data = {
            'type':3
        }

        res = Myrequest.get(self.url, header=headers, data=data)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))

    def test_crmusertag4(self):
        '''我的全部用户查询条件：4用户级别'''
        headers = {
            'Authorization': self.token

        }

        data = {
            'type':4
        }

        res = Myrequest.get(self.url, header=headers, data=data)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))

    def test_crmusertag5(self):
        '''我的全部用户查询条件：5上课情况'''
        headers = {
            'Authorization': self.token

        }

        data = {
            'type':5
        }

        res = Myrequest.get(self.url, header=headers, data=data)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))

    def test_crmusertag6(self):
        '''我的全部用户查询条件：6上课情况下级查询条件'''
        headers = {
            'Authorization': self.token

        }

        data = {
            'type':6
        }

        res = Myrequest.get(self.url, header=headers, data=data)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))

    def tearDown(self):
        pass


if __name__ == '__main__':

    suite = unittest.TestSuite()
    test_case = suite.addTests[Crm_CrmUserTag('test_crmusertag1'),Crm_CrmUserTag('test_crmusertag2'),Crm_CrmUserTag('test_crmusertag3'),Crm_CrmUserTag('test_crmusertag4'),Crm_CrmUserTag('test_crmusertag5'),Crm_CrmUserTag('test_crmusertag6')]
    runner = unittest.TextTestRunner()
    runner.run(suite)