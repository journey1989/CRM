from common.my_request import *
from common.tool import *
import unittest
from config.setting import *
class Crm_SpecialSumData(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/getSpecialSumData'


    def test_SpecialSumData(self):
        '''特训营面板：全部营期数据汇总'''
        data = {
            'type':BOARDTYPE2,
            'periods':''
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url,data,headers)
        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s'%(self.url,self.token,res))

    def tearDown(self):
        pass



if __name__ == '__main__':
    c = Crm_SpecialSumData()
    c.test_SpecialSumData()
