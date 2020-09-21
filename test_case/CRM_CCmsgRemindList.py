from common.tool import *
import unittest
from config.setting import *

class Crm_MsgRemindList(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/saleWordBoard/msg_remind_list'

    def test_MsgRemindList(self):
        '''cc面板：消息提醒'''


        headers = {
            'Authorization': self.token,
            'pageIndex':'1',
            'pageSize':'10'
        }

        res = Myrequest.get(self.url,header=headers)
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_MsgRemindList()
    c.test_MsgRemindList()