from common.my_request import *
from common.tool import *
import unittest


class Crm_TransferLeads(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/classTeacher/panel/transferLeads'

    def test_transferleads(self):
        '''班主任面板：本月转介绍leads数据'''
        headers = {'Authorization': self.token}
        res = Myrequest.get(self.url, header=headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_TransferLeads()
    c.test_transferleads()
