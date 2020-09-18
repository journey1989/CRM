from common.tool import testLogin
import unittest,json
from common.tool import Myrequest

class Crm_ReceiveLeads(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/leadsOperate/receiveLeads'

    def test_receiveleads(self):
        '''我的全部用户：领取客户'''

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://crm.putaoabc.com',
            'Referer': 'https://crm.putaoabc.com/my_user/all_user',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Cookie': 'uuid=5101923E-8415-9F5B-8049-72BB915EDE3E',
            'Authorization': self.token
        }

        data = {}

        res = Myrequest.post(self.url, header=headers, data=json.dumps(data))
        self.assertEqual(200, res.get('code'),msg=res.get('msg'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_ReceiveLeads()
    c.test_receiveleads()