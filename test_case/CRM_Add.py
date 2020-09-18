from common.tool import testLogin
import unittest,json
from common.tool import Myrequest

class Crm_add(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/client/add'

    def test_add(self):
        '''我的全部用户：新建客户'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://crm.putaoabc.com',
            'Referer': 'https://crm.putaoabc.com/my_user/all_user',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Cookie': 'uuid=5101923E-8415-9F5B-8049-72BB915EDE3E',
            'Authorization': self.token
        }

        data = {
                "parents": "hello",
                "phoneNum": "14500009661",
                "kidName": "14500009661",
                "grade": "14500009661",
                "birth": "2020-09-18",
                "kidLevel": 105,
                "saleOwnerId": 22
            }

        res = Myrequest.post(self.url, header=headers, data=json.dumps(data))
        self.assertFalse(res.get('success'))

    def tearDown(self):
         pass


if __name__ == '__main__':
    c = Crm_add()
    c.test_add()