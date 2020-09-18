#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  requests
from config.setting import log
from urllib3.exceptions import InsecureRequestWarning

from urllib3 import disable_warnings
from requests.adapters import HTTPAdapter

disable_warnings(InsecureRequestWarning)
req = requests.Session()
req.mount('http://', HTTPAdapter(max_retries=1))
req.mount('https://', HTTPAdapter(max_retries=1))
class Myrequest():
    @staticmethod
    def post(url, data=None, cookie=None, header=None, is_json=False, files=None, params=None):

        data = data if data else {}
        cookie = cookie if cookie else {}
        header = header if header else {"Connection": "close"}
        files = files if files else {}
        params = params if params else {}
        log.debug('【请求接口地址:%s】'%url)

        try:
            if is_json:
                res = req.post(url, json=data, cookies=cookie, headers=header, verify=False, files=files,
                               params=params, timeout=10).json()
            else:
                res = req.post(url, data=data, cookies=cookie, headers=header, verify=False, files=files,
                               params=params, timeout=10).json()

        except Exception as e:
            res = {'error': str(e)}  # 如果接口调用出错的话，那么就返回一个有错误信息的字典
            log.error('异常信息：接口调用失败！ url 【%s】 data 【%s】 实际结果是 【%s】' % (url, data, res))
        return res




    @staticmethod
    def get(url, data=None, header=None, cookie=None):

        data = data if data else {}

        cookie = cookie if cookie else {}
        header = header if header else {"Connection": "close"}
        log.debug('【请求接口地址：%s】' % url)

        try:

            res = req.get(url, params=data, cookies=cookie, headers=header, verify=False, timeout=20).json()



        except Exception as e:
            res = {'error': str(e)}  # 如果接口调用出错的话，那么就返回一个有错误信息的字典
            log.error('异常信息：接口调用失败！ url 【%s】 data 【%s】 实际结果是 【%s】' % (url, data, res))
            # log.error('耗时：%s' % get_time_used)
        return res
