#coding:utf-8

import urllib2,urllib
import ssl
import json


ssl._create_default_https_context = ssl._create_unverified_context  #关闭安全验证

def getList():
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2017-09-17&leftTicketDTO.from_station=TYV&leftTicketDTO.to_station=TJP&purpose_codes=ADULT')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    req.add_header('Referer','https://kyfw.12306.cn/otn/leftTicket/init')
    req.add_header('Cookie','JSESSIONID=BC1C0D8F10E31FD6684E1E000F10C901; _jc_save_detail=true; RAIL_OkLJUJ=FFAS0vNtsUwCQjBzmJ_wH1C3BitWZWnd; fp_ver=4.5.1; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=636486154.24610.0000; RAIL_EXPIRATION=1505595252819; RAIL_DEVICEID=ALIbFn5Xasf9BDWSu0hAZ4XCvp7el6sLXszcEWihVVZuJdtpg3f0gQCOoeVBS5NMuuPBfMWx3kdRVFWADhh76ts2aNjGIntLiq7INADSkvTIRQGjGRcb1SOwmyivuhJsZbq_-WQwQbkr7pmuEmasuy_TSMjHNfI2; _jc_save_fromStation=%u592A%u539F%2CTYV; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_fromDate=2017-09-17; _jc_save_toDate=2017-09-13; _jc_save_wfdc_flag=dc')
    html = urllib2.urlopen(req).read()  #urlopen(req,data)第二个参数为空时为get请求
    dict = json.loads(html)   #将json数据转换为dict
    return dict['data']['result']
for i in getList():
    tmp_list = i.split('|')
    if tmp_list[23] != u'无' or tmp_list[23] != '':
        print u'有票'
        print tmp_list[3]
        print tmp_list[8]
        print tmp_list[9]
        print tmp_list[23]
        break
    #for n in tmp_list:
    #    print n
    break
