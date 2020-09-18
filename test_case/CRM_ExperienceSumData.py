from common.my_request import *
from common.tool import *
import unittest
from config.setting import *
class Crm_ExperienceSumData(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/getExperienceSumData'


    def test_ExperienceSumData(self):
        '''体验营面板：全部营期数据汇总'''
        data = {
            'type':BOARDTYPE1,
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
    c = Crm_ExperienceSumData()
    c.test_ExperienceSumData()
