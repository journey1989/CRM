from common.tool import *
import unittest


class Crm_saleAmountRanking(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/saleWordBoard/saleAmountRanking'

    def test_saleAmountRanking(self):
        '''cc面板：销售排行榜'''

        data = {

            'starttime': '2020-09-21',
            'endtime': '2020-09-22'
        }
        headers = {
            'Authorization': self.token

        }
        print('hello====', self.token)
        res = Myrequest.get(self.url,  data=data, header=headers)
        self.assertEqual(0, res.get('code'))


    def tearDown(self):
        pass

if __name__ == '__main__':
    c =  Crm_saleAmountRanking()
    c.test_saleAmountRanking()