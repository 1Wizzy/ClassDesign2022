# encoding:utf-8

import requests
import base64
import validators
import imghdr
import sys
from os import path

'''
Function:通用文字识别
Author:WizzyAng
Explanation:This function will store the  return json named res_dict in local
'''


def Identify_Words(access_token, params):  # str,dict
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)  # 请求url     请求参数        请求头
    if response:
        res_dict = response.json()
    LanguageTypeNumber = ["English", "Japanese", "Korean", "Chinese"]
    print("We Find {} Words from your file".format(res_dict["words_result_num"]))
    print("This is the Plain Text result for easy copy")
    print("****************************************")
    for wd in res_dict["words_result"]:
        print(wd["words"])
    print("****************************************")
    if "language" in res_dict.keys() or "paragraph" in params.keys() or "probability" in params.keys():
        print("The Advanced Data: ")
        if "language" in res_dict.keys():  # Print The Language in the uploaded File
            print("The Language in the File you uploaded is {}".format(LanguageTypeNumber[res_dict["language"]]))
        if "paragraph" in params.keys():  # Print The Info About Paragraph
            print("The File you uploaded have {} paragraph(s)".format(res_dict["paragraphs_result_num"]))
            for ParagraphIdx in range(0, res_dict["paragraphs_result_num"]):
                print("Paragraph {}:".format(ParagraphIdx))
                for WordsInParagraph in res_dict["paragraphs_result"][ParagraphIdx][
                    "words_result_idx"]:  # WordsInParagraph:list
                    print("{}".format(res_dict["words_result"][WordsInParagraph]["words"]), end=' ')
                print("\n")
        if "probability" in params.keys():
            for Words_Result in res_dict["words_result"]:  # Wors_Result:list element
                print("The Info of Probability about {} is".format(Words_Result["words"]))
                print("\tThe Average Probability is {}".format(Words_Result["probability"]["average"]))
                print("\tThe Minimum Probability is {}".format(Words_Result["probability"]["min"]))
                print("\tThe Variance Probability is {}".format(Words_Result["probability"]["variance"]))


"""
Function: Auto Select File Format 
Author: WizzyAng
Incoming parameters: file name(str)
Return parameters: a pair key:value
"""


def auto_select_file(file_name):  #
    if validators.url(file_name):  # Check if is url
        return {"url": file_name}
    if not path.exists(file_name):
        print("The File Does NOT Exist!")
        return "Error"
    with open(file_name, 'rb') as f:
        temp = base64.b64encode(f.read())
    if file_name[-3:] == "pdf":
        return {"pdf_file": temp}
    elif imghdr.what(file_name) == "jpg" or "jpeg" or "png" or "bmp":
        return {"image": temp}
    else:
        print("Please Input The Correct Format File !")
        return "Error"


"""
FileName(str):本地文件或者url
LanguageType(str): CHN_ENG  ENG  JAP  KOR  FRE
                 SPA  POR  GER  ITA  RUS
其余均为Bool值
"""


def MakeParams(FileName, LanguageType="None", DetectLanguage=False, Paragraph=False, Probability=False):
    Parms = {}
    FileDictPair = auto_select_file(FileName)
    if FileDictPair == "Error":
        print("Is Wrong!")
        sys.exit(-1)
    Parms.update(FileDictPair)
    if LanguageType != "None":
        Parms.update({"language_type": LanguageType})
    if DetectLanguage:
        Parms.update({"detect_direction": "true"})
    if Paragraph:
        Parms.update({"paragraph": "true"})
    if Probability:
        Parms.update({"probability": "true"})
    return Parms


def Identify_Words_GUI(access_token, params):  # str,dict
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)  # 请求url     请求参数        请求头
    if response:
        res_dict = response.json()
    res = open("log", mode='a', encoding="utf-8")
    LanguageTypeNumber = ["English", "Japanese", "Korean", "Chinese"]
    print("We Find {} Words from your file".format(res_dict["words_result_num"]), file=res)
    print("This is the Plain Text result for easy copy", file=res)
    print("****************************************", file=res)
    for wd in res_dict["words_result"]:
        print(wd["words"], file=res)
    print("****************************************", file=res)
    if "language" in res_dict.keys() or "paragraph" in params.keys() or "probability" in params.keys():
        print("The Advanced Data: ", file=res)
        if "language" in res_dict.keys():  # Print The Language in the uploaded File
            print("The Language in the File you uploaded is {}".format(LanguageTypeNumber[res_dict["language"]]),
                  file=res)
        if "paragraph" in params.keys():  # Print The Info About Paragraph
            print("The File you uploaded have {} paragraph(s)".format(res_dict["paragraphs_result_num"]), file=res)
            for ParagraphIdx in range(0, res_dict["paragraphs_result_num"]):
                print("Paragraph {}:".format(ParagraphIdx), file=res)
                for WordsInParagraph in res_dict["paragraphs_result"][ParagraphIdx][
                    "words_result_idx"]:  # WordsInParagraph:list
                    print("{}".format(res_dict["words_result"][WordsInParagraph]["words"]), end=' ', file=res)
                print("\n", file=res)
        if "probability" in params.keys():
            for Words_Result in res_dict["words_result"]:  # Wors_Result:list element
                print("The Info of Probability about {} is".format(Words_Result["words"]), file=res)
                print("\tThe Average Probability is {}".format(Words_Result["probability"]["average"]), file=res)
                print("\tThe Minimum Probability is {}".format(Words_Result["probability"]["min"]), file=res)
                print("\tThe Variance Probability is {}".format(Words_Result["probability"]["variance"]), file=res)
        res.close()



