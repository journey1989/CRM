from common.my_request import *
from common.tool import *
import unittest


class Crm_WaitAssignUserList(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/myUser/waitAssignUserList'

    def test_waitassignuserlist(self):
        '''待分配leads池'''
        headers = {'Authorization': self.token}


        res = Myrequest.get(self.url, header=headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_WaitAssignUserList()
    c.test_waitassignuserlist()
