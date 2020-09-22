import yagmail,time
from config.setting import *


def SendEmail():

    list = os.listdir(REPORT_PATH)
    list.sort(key=lambda fn:os.path.getctime(REPORT_PATH + '\\' + fn))
    file = os.path.join(REPORT_PATH, list[-1])
    print(file)



    try:

       yag = yagmail.SMTP(host='smtp.qq.com',user='825664936@qq.com',password='zmzjqgggkcsgbfdc')
       body = ['<h1>CRM接口自动化测试报告</h1>' ,yagmail.inline(os.path.join(REPORT_PATH, file))]
    except Exception as e:
       exec = {'error':str(e)}

    else:
        yag.send(to='lilei2@putao-inc.com',contents=body, subject='CRM接口自动化测试报告')
        print('邮件已发送')
        yagmail.SMTP.close(yag)

if __name__ == '__main__':
    SendEmail()

