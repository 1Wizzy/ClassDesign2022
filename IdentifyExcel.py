
# encoding:utf-8

import requests
import base64
import imghdr
from os import path
'''
Function:表格文字识别(异步接口)
Author:WizzyAng
Explanation:
'''
def Identify_Excel(access_token,params):
    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        res_dict=response.json()
    ExcelUrl = res_dict["result"]["result_data"]
    res = requests.get(ExcelUrl)
    with open("Result.xls",'wb') as f:
        f.write(res.content)
    print("The file is downloaded in the program root directory")
    
def process_file(file_name):
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
def MakeParams(FileName):
    Params = {"is_sync":"true","request_type":"excel"}
    Params.update(process_file(FileName))
    return Params

