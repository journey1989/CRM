from BeautifulReport import BeautifulReport


from config.setting import *
import unittest,time

def Run():

    reportname = 'CRM接口自动化测试报告'
    discover = unittest.defaultTestLoader.discover(TESTCASE_PATH, 'CRM*.py')
    now = time.strftime("%Y%m%d %H_%M_%S")

    report =  now + reportname + '.html'
    print(report)
    result = BeautifulReport(discover)
    result.report(filename=report, description='CRM接口自动化', log_path=REPORT_PATH)




if __name__ == '__main__':
    Run()


