from common.tool import testLogin
import unittest,json
from common.tool import Myrequest
from config.setting import *
class Crm_TmkLeadsInfo(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/tmkWordBoard/getTmkLeadsInfo'

    def test_TmkLeadsInfo(self):
        '''TMK面板：今日待办leads24小时内'''

        headers = {'Authorization': self.token}
        # data = {
        #     'boardType': BOARDTYPE3
        # }
        res = Myrequest.get(self.url,  header=headers )
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_TmkLeadsInfo()
    c.test_TmkLeadsInfo()