from common.my_request import *
from common.tool import *
import unittest,json
from config.setting import *
from urllib.parse import quote
class Crm_ExperienceBoard(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/getExperienceBoard'


    def test_ExperienceBoard_1(self):
        '''体验营面板：一节课营期面板数据'''
        periods = quote('全部')
        data = {
            'type':BOARDTYPE1,
            'periods':periods,
            'lessonNum':1,
            'starttime':'2020-09-16',
            'endtime':'2020-09-16'
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url,data,headers)

        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s'%(self.url,self.token,res))

        load = str(res.get('data'))

        self.assertIn('一节课', load, msg='请求地址%s 断言数据%s 响应数据%s'%(self.url,load,res))


    def test_ExperienceBoard_2(self):
        '''体验营面板：二节营期面板数据'''
        periods = quote('全部')
        data = {
            'type':BOARDTYPE1,
            'periods':periods,
            'lessonNum':2,
            'starttime':'2020-09-16',
            'endtime':'2020-09-16'
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url,data,headers)
        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s'%(self.url,self.token,res))
        load = str(res.get('data'))
        self.assertIn('二节课', load, msg='请求地址%s 断言数据%s 响应数据%s' % (self.url, load, res))

    def test_ExperienceBoard_3(self):
        '''体验营面板：三节营期面板数据'''
        periods = quote('全部')
        data = {
            'type':BOARDTYPE1,
            'periods':periods,
            'lessonNum':3,
            'starttime':'2020-09-16',
            'endtime':'2020-09-16'
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url,data,headers)
        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s'%(self.url,self.token,res))
        load = str(res.get('data'))
        self.assertIn('三节课', load, msg='请求地址%s 断言数据%s 响应数据%s' % (self.url, load, res))

    def test_ExperienceBoard_4(self):
        '''体验营面板：四节营期面板数据'''
        periods = quote('全部')
        data = {
            'type':BOARDTYPE1,
            'periods':periods,
            'lessonNum':4,
            'starttime':'2020-09-16',
            'endtime':'2020-09-16'
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url,data,headers)
        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s'%(self.url,self.token,res))
        load = str(res.get('data'))
        self.assertIn('四节课', load, msg='请求地址%s 断言数据%s 响应数据%s' % (self.url, load, res))


    def test_ExperienceBoard_5(self):
        '''体验营面板：五节营期面板数据'''
        periods = quote('全部')
        data = {
            'type':BOARDTYPE1,
            'periods':periods,
            'lessonNum':5,
            'starttime':'2020-09-16',
            'endtime':'2020-09-16'
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url,data,headers)
        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s'%(self.url,self.token,res))
        load = str(res.get('data'))
        self.assertIn('五节课', load, msg='请求地址%s 断言数据%s 响应数据%s' % (self.url, load, res))

    def tearDown(self):
        pass



if __name__ == '__main__':

     unittest.main()

