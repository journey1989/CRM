from common.tool import *
import unittest


class Crm_SaleAmountRanking(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/saleWordBoard/saleAmountRanking'

    def test_saleamountranking(self):
        '''cc面板：销售排行榜'''
        data = {
            'startTime':'2020-09-22',
            'endTime':'2020-09-23'
        }

        headers = { 'Authorization': self.token}

        res = Myrequest.get(self.url, data=data, header=headers)
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_SaleAmountRanking()
    c.test_saleamountranking()