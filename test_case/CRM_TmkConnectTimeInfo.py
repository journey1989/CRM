from common.tool import testLogin
import unittest,json
from common.tool import Myrequest
from config.setting import *
class Crm_TmkConnectTimeInfo(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/tmkWordBoard/getTmkConnectTimeInfo'

    def test_tmkconnecttimeinfo(self):
        '''TMK面板：本月通时'''

        headers = {'Authorization': self.token}
        data = {
            'boardType': BOARDTYPE3
        }
        res = Myrequest.get(self.url, data, headers )
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_TmkConnectTimeInfo()
    c.test_tmkconnecttimeinfo()