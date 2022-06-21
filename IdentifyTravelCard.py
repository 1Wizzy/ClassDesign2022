# encoding:utf-8

import requests
import base64
import imghdr
from os import path

'''
Function: 通信行程卡识别
Author: WizzyAng
'''

def GetResDict(access_token,params):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/travel_card"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        res_dict = response.json()
    return res_dict
def ProcessData(res_dict):
    print("The Phone Number is {}".format(res_dict["result"]['手机号'][0]['word'][0]))
    for way in res_dict["result"]['途经地'][0]['word']:
        print("You Have Passed {}".format(way))
    if res_dict["result"]['风险性']:
        print("The city you pass through has a medium or high risk area")
    else:
        print("There are no medium or high risk areas in the city you pass through")
    t = res_dict["result"]['更新时间'][0]['word'][0]
    t = t.replace(' ','')
    t = t.replace('.','')
    t = t.replace(':','')
    print("The time of the TravelCard is {}.{}.{} {}:{}:{}".format(t[:4],t[4:6],t[6:8],t[8:10],t[10:12],t[12:14]))
def ProcessFile(file_name):#
    if not path.exists(file_name):
        print("The File Does NOT Exist!")
        return "Error"
    if imghdr.what(file_name) == "jpg" or "jpeg" or "png" or "bmp":
        with open(file_name,'rb') as f:
            temp = base64.b64encode(f.read())
        return {"image":temp}
    else:
        print("Please Input The Correct Format File !")
        return "Error"      
