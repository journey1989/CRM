from common.tool import testLogin
import unittest,json
from common.tool import Myrequest
from config.setting import *

class Crm_TmkAssginInfo(unittest.TestCase):

    def setUp(self):

        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/tmkWordBoard/getTmkAssignInfo'

    def test_tmkassgininfo(self):

        '''TMK面板：本月分配'''
        headers = {'Authorization': self.token}
        data = {
            'boardType': BOARDTYPE3
        }
        res = Myrequest.get(self.url, data, headers)
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
        c = Crm_TmkAssginInfo()
        c.test_tmkassgininfo()