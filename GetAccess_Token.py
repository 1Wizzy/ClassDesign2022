# encoding:utf-8
# This File 
import requests 
# client_id 为官网获取的AK， client_secret 为官网获取的SK
'''
Function:Get AccessToken
Author:WizzyAng
'''
def GetAccessToken():
    cd=input("Please Input Your API Key: ")
    cs=input("Please Input Your Secret Key: ")
    host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="+ cd + "&client_secret=" + cs
    response = requests.get(host)
    if response:
        res=response.json()
    else:
        return "Error"
    return res["access_token"]
def Get_Access_Token(cd,cs):
    host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="+ cd + "&client_secret=" + cs
    response = requests.get(host)
    if response:
        res=response.json()
    else:
        return "Error"
    return res["access_token"]
