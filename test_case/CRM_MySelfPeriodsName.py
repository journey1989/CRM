from common.tool import *
import unittest
from config.setting import *

class Crm_MySelfPeriodsName(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/getMySelfPeriodsName'

    def test_MySelfPeriodsName(self):
        '''体验营面板：获取我的营期'''
        data = {
            'type':BOARDTYPE1   #体验营type 3 特训营 4
        }

        headers = {
            'Authorization': self.token
        }

        res = Myrequest.get(self.url, data, headers)
        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s' %(self.url, self.token, res))

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_MySelfPeriodsName()
    c.test_MySelfPeriodsName()