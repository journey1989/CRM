

from BSTestRunner import BSTestRunner
from config.setting import *
import unittest,time
from common.sendemail import *

def Run():

    reportname = 'CRM接口自动化测试报告'
    discover = unittest.defaultTestLoader.discover(TESTCASE_PATH, 'CRM*.py')
    now = time.strftime("%Y%m%d %H_%M_%S")

    report = REPORT_PATH +'\\'+ now + reportname + '.html'
    print(report)

    with open(report, 'wb') as f:
        runner = BSTestRunner(stream=f,title="CRM接口自动化",description='CRM接口自动化测试结果如下：')
        runner.run(discover)

    SendEmail()

if __name__ == '__main__':
    Run()


