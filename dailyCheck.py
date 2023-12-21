#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:dailyCheck.py
# datetime:2022/4/30 13:47
# software: PyCharm
'''
this is function  description 
'''
# import module your need

import requests
import datetime

def dailyC():
    time = datetime.datetime.now()
    time1 = str(time).split(" ")[0]
    time2 = str(time).split(" ")[1].split('.')[0]
    print(time1)
    print(time2)

    url = "http://xgxt.ncepu.edu.cn/qfwyqfkxg/sys/lwNcepuDailyReport/mobile/dataReport/T_STU_DAILYREPORT_INFO_SAVE.do"

    cookies = {
        "SECKEY_ABVK": "",
        "BMAP_SECKEY": "",
        "EMAP_LANG": "zh",
        "_WEU": "",
        "JSESSIONID": ""
    }

    formData = {
    }

    formData.CREATED_AT = time1 + " " + time2
    formData.NEED_CHECKIN_DATE = time1
    formData.CZRQ = time1 + " " + time2
    formData.TEMPERATURE = "36.5"

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh-HK;q=0.9,zh;q=0.8",
        "Content-Length": "5000",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "xgxt.ncepu.edu.cn",
        "Origin": "http://xgxt.ncepu.edu.cn",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://xgxt.ncepu.edu.cn/qfwyqfkxg/sys/lwNcepuDailyReport/*default/index.do",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    response = requests.post(url=url, headers=headers, data=formData, cookies=cookies)

    print(response.text)

