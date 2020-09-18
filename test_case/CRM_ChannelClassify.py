from common.tool import *
import unittest
from config.setting import *

class Crm_ChannelClassify(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/myUser/getChannelClassify'

    def test_channelclassify(self):
        '''我的全部用户：获取渠道'''
        headers = {
        'Authorization': self.token

    }

        res = Myrequest.get(self.url, header=headers)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))
    def tearDown(self):
        pass


if __name__ == '__main__':
    c =Crm_ChannelClassify()
    c.test_channelclassify()

