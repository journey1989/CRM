#!/usr/bin/env python
# -*- coding:utf-8 -*-
from config.setting import *
from urllib.parse import urljoin
from common.my_request import Myrequest
import requests,json
def login():

    url = 'self_api/auth/login'
    real_url = urljoin(BASE_URL, url)
    headers = {
        'Content-Type':'application/json; charset=UTF-8',
        'Origin':'https://crm.putaoabc.com',
        'Referer':'https://crm.putaoabc.com/login',
        'Accept':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Cookie':'uuid=D58656BD-8333-AC8A-7D54-BC5090F92D60'
    }
    # cookies = {
    #     #     "uuid":"D58656BD-8333-AC8A-7D54-BC5090F92D60"
    #     # }

    json_data = json.dumps({
	     "email": "lilei2@putao-inc.com",
	     "password": "18519109588Abc"
      })

    res = Myrequest.post(url=real_url, data=json_data, header=headers, is_json=False)
    #json.dumps()用于将字典形式的数据转化为字符串，json.loads()用于将字符串形式的数据转化为字典

    token = res['data']['token']

    username = res['data']['username']

    roleInfos = res['data']['roleInfos']


    return token, username, roleInfos




def testLogin():

    url = 'self_api/auth/login'
    real_url = urljoin(TESTBASE_URL, url)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'https://crm.putaoabc.com',
        'Referer': 'https://crm.putaoabc.com/login',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Cookie': 'uuid=D58656BD-8333-AC8A-7D54-BC5090F92D60'

    }
    data = {
	"email": "zhangjunfeng@putao-inc.com",
	"password": "123456"
}
    json_data = json.dumps(data)

    res = Myrequest.post(url=real_url,data=json_data, is_json=False, header=headers)

    token = res['data']['token']


    return token




if __name__ == '__main__':
    #login()
     testLogin()



