from common.my_request import *
from common.tool import *
import unittest


class Crm_CourseList(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/user_course_situation/course_list'

    def test_courselist(self):
        '''我的全部用户完课情况'''
        headers = {'Authorization': self.token}

        data = {
            'startTime':'2020-09-21',
            'endTime':'2020-09-21',
            'pageIndex':'1',
            'pageSize':'10'
        }
        res = Myrequest.get(self.url, header=headers,data=data)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_CourseList()
    c.test_courselist()
