from common.my_request import *
from common.tool import *
import unittest,json
from config.setting import *
from urllib.parse import quote
from ddt import *
@ddt
class Crm_ExperienceBoard(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/getExperienceBoard'

    @data(1,2,3,4,5)
    def test_ExperienceBoard(self,lessonnum):
        '''体验营面板：营期面板数据'''
        periods = quote('全部')
        data = {
            'type':BOARDTYPE1,
            'periods':periods,
            'lessonNum':lessonnum,
            'starttime':'2020-09-16',
            'endtime':'2020-09-16'
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url,data,headers)

        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s'%(self.url,self.token,res))

        load = str(res.get('data'))


    def tearDown(self):
        pass



if __name__ == '__main__':

     unittest.main()

