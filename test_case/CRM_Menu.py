
from common.tool import testLogin
import unittest
from common.tool import Myrequest


class Crm_menu(unittest.TestCase):


    def setUp(self):

        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/menu/person/menu'

    def test_menu(self):
        '''获取菜单'''
        headers = {
            'Authorization': self.token
        }

        res = Myrequest.get(self.url, header=headers)
        print("headers======", headers)
        self.assertEqual(0, res.get('code'), msg='请求地址%s 请求参数%s 响应数据%s' %(self.url, self.token, res))


    def tearDown(self):
        pass




if __name__ == '__main__':
    c = Crm_menu()
    c.test_menu()