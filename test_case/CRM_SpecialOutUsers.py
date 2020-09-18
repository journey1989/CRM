from common.my_request import *
from common.tool import *
import unittest
from config.setting import *
class Crm_SpecialOutUsers(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/getSpecialOutUsers'


    def test_SpecialOutUsers(self):
        '''特训营面板：营期外学员'''
        data = {
            'periods':'',
            'type':BOARDTYPE2,
            'startTime': '',
            'endTime': ''
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url,data,headers)
        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s'%(self.url,self.token,res))

    def tearDown(self):
        pass



if __name__ == '__main__':
    c = Crm_SpecialOutUsers()
    c.test_SpecialOutUsers()
