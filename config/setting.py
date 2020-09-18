#!/usr/bin/env python
# -*- coding:utf-8 -*-
import nnlog
from urllib.parse import urljoin
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = 'https://crm.putaoabc.com'
TESTBASE_URL = 'https://ctest.putaoabc.net.cn'


REPORT_PATH = os.path.join(BASE_PATH, 'result')
TESTCASE_PATH = os.path.join(BASE_PATH, 'test_case')
print(REPORT_PATH, TESTCASE_PATH)



#体验营面板
BOARDTYPE1 = 3
#特训营面板
BOARDTYPE2 = 4
#TMK面板
BOARDTYPE3 = 1
LEVEL = 'debug'
LOG_PATH = os.path.join(BASE_PATH, 'log')
LOG_NAME = 'crm.log'
log = nnlog.Logger(os.path.join(LOG_PATH, LOG_NAME), 'debug')

