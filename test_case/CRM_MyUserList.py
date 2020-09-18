from common.tool import *
import unittest
from config.setting import *

class Crm_MyUserList(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/myUser/myUserList'


    def test_myuserlist1(self):
        '''我的全部用户：全部'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://crm.putaoabc.com',
            'Referer': 'https://crm.putaoabc.com/my_user/all_user',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Cookie': 'uuid=5101923E-8415-9F5B-8049-72BB915EDE3E',
            'Authorization': self.token

        }

        # cookies = {
        #     'um_distinctid': '173b228a6242c3-0fec2eac7c0be3-5373e62-100200-173b228a62675'
        # }

        data = {
                "pageIndex": 1,
                "pageSize": 10,
                "sortType": "",
                "desc": "desc",
                "queryType": "all",
                "dataPerms": 4
            }

        res = Myrequest.post(self.url, header=headers, data=json.dumps(data))
        self.assertEqual(0, res.get('code'))


    def test_myuserlist2(self):
        '''我的全部用户：已成单'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://crm.putaoabc.com',
            'Referer': 'https://crm.putaoabc.com/my_user/all_user',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Cookie': 'uuid=5101923E-8415-9F5B-8049-72BB915EDE3E',
            'Authorization': self.token

        }

        # cookies = {
        #     'um_distinctid': '173b228a6242c3-0fec2eac7c0be3-5373e62-100200-173b228a62675'
        # }

        data = {
                "pageIndex": 1,
                "pageSize": 10,
                "sortType": "",
                "desc": "desc",
                "queryType": "alreadyPay",
                "dataPerms": 4
            }

        res = Myrequest.post(self.url, header=headers, data=json.dumps(data))
        self.assertEqual(0, res.get('code'))

    def test_myuserlist3(self):
        '''我的全部用户：未成单'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://crm.putaoabc.com',
            'Referer': 'https://crm.putaoabc.com/my_user/all_user',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Cookie': 'uuid=5101923E-8415-9F5B-8049-72BB915EDE3E',
            'Authorization': self.token

        }

        # cookies = {
        #     'um_distinctid': '173b228a6242c3-0fec2eac7c0be3-5373e62-100200-173b228a62675'
        # }

        data = {
            "pageIndex": 1,
            "pageSize": 10,
            "sortType": "",
            "desc": "desc",
            "queryType": "notPay",
            "dataPerms": 4
        }

        res = Myrequest.post(self.url, header=headers, data=json.dumps(data))
        self.assertEqual(0, res.get('code'))


    def test_myuserlist4(self):
        '''我的全部用户：我的锁定用户'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://crm.putaoabc.com',
            'Referer': 'https://crm.putaoabc.com/my_user/all_user',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Cookie': 'uuid=5101923E-8415-9F5B-8049-72BB915EDE3E',
            'Authorization': self.token

        }

        # cookies = {
        #     'um_distinctid': '173b228a6242c3-0fec2eac7c0be3-5373e62-100200-173b228a62675'
        # }

        data = {
            "pageIndex": 1,
            "pageSize": 10,
            "sortType": "",
            "desc": "desc",
            "queryType": "lockUsers",
            "dataPerms": 4
        }

        res = Myrequest.post(self.url, header=headers, data=json.dumps(data))
        self.assertEqual(0, res.get('code'))

    def test_myuserlist5(self):
        '''我的全部用户：公海'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://crm.putaoabc.com',
            'Referer': 'https://crm.putaoabc.com/my_user/all_user',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Cookie': 'uuid=5101923E-8415-9F5B-8049-72BB915EDE3E',
            'Authorization': self.token

        }

        # cookies = {
        #     'um_distinctid': '173b228a6242c3-0fec2eac7c0be3-5373e62-100200-173b228a62675'
        # }

        data = {
            "pageIndex": 1,
            "pageSize": 10,
            "sortType": "",
            "desc": "desc",
            "queryType": "publicSea",
            "dataPerms": 4
        }

        res = Myrequest.post(self.url, header=headers, data=json.dumps(data))
        self.assertEqual(0, res.get('code'))

    def test_myuserlist6(self):
        '''我的全部用户：勿扰库'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://crm.putaoabc.com',
            'Referer': 'https://crm.putaoabc.com/my_user/all_user',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Cookie': 'uuid=5101923E-8415-9F5B-8049-72BB915EDE3E',
            'Authorization': self.token

        }

        # cookies = {
        #     'um_distinctid': '173b228a6242c3-0fec2eac7c0be3-5373e62-100200-173b228a62675'
        # }

        data = {
            "pageIndex": 1,
            "pageSize": 10,
            "sortType": "",
            "desc": "desc",
            "queryType": "notDisturb",
            "dataPerms": 4
        }

        res = Myrequest.post(self.url, header=headers, data=json.dumps(data))
        self.assertEqual(0, res.get('code'))

    def test_myuserlist7(self):
        '''我的全部用户：学员列表'''
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://crm.putaoabc.com',
            'Referer': 'https://crm.putaoabc.com/my_user/all_user',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Cookie': 'uuid=5101923E-8415-9F5B-8049-72BB915EDE3E',
            'Authorization': self.token

        }

        # cookies = {
        #     'um_distinctid': '173b228a6242c3-0fec2eac7c0be3-5373e62-100200-173b228a62675'
        # }

        data = {
            "pageIndex": 1,
            "pageSize": 10,
            "sortType": "",
            "desc": "desc",
            "queryType": "longUsers",
            "dataPerms": 4
        }

        res = Myrequest.post(self.url, header=headers, data=json.dumps(data))
        self.assertEqual(0, res.get('code'))


    def tearDown(self):
        pass



if __name__ == '__main__':
     suite = unittest.TestSuite()
     test_cases = [Crm_MyUserList('test_myuserlist1'),Crm_MyUserList('test_myuserlist2'),Crm_MyUserList('test_myuserlist3'),Crm_MyUserList('test_myuserlist4'),Crm_MyUserList('test_myuserlist5'),Crm_MyUserList('test_myuserlist6'),Crm_MyUserList('test_myuserlist7')]
     suite.addTests(test_cases)
     runner = unittest.TextTestRunner()
     runner.run(suite)