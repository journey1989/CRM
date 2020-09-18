from common.my_request import *
from common.tool import *
import unittest
from config.setting import *
class Crm_SpecialOrdersAmount(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/getSpecialOrdersAmount'


    def test_SpecialOrdersAmount(self):
        '''特训营面板：本月成单总金额'''
        data = {
            'boardType':BOARDTYPE2
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url,data,headers)
        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s'%(self.url,self.token,res))

    def tearDown(self):
        pass



if __name__ == '__main__':
    c = Crm_SpecialOrdersAmount()
    c.test_SpecialOrdersAmount()

