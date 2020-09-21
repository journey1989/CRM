from common.tool import *
import unittest


class Crm_report(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/saleWordBoard/report'

    def test_report(self):
        '''cc面板：指标统计'''

        data = {

            'starttime': '',
            'endtime': ''
        }
        headers = {
            'Authorization': self.token
        }

        res = Myrequest.get(self.url, header=headers, data=data)
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c =  Crm_report()
    c.test_report()