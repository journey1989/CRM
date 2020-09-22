from common.my_request import *
from common.tool import *
import unittest


class Crm_UpgradeStu(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/classTeacher/panel/upgradeStu'

    def test_upgradestu(self):
        '''班主任面板：本月升舱学员'''
        headers = {'Authorization': self.token}
        res = Myrequest.get(self.url, header=headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_UpgradeStu()
    c.test_upgradestu()
