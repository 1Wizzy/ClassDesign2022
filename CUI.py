
# encoding: utf-8

import sys
from time import sleep
import IdentifyWords
import GetAccess_Token
import IdentifyExcel
import os
from ReadImageFromClipboard import ClipboardImageToBase64,CheckIfIsImage
import IdentifyTravelCard
"""
Function: CUI
Author: WizzyAng
"""

def ChooseMode():# 选择模式
    print("************************************")
    print("                                    ")
    print("     Welcome to the Software        ")
    print("                                    ")
    print("[1] Identify Words                  ")
    print("                                    ")
    print("[2] Identify Excel                  ")
    print("                                    ")
    print("[3] Identify TravelCard             ")
    print("                                    ")
    print("[0] Info                            ")
    print("                                    ")
    print("                                    ")
    print("Press q or Control + C to quit the Program!")
    print("                                    ")
    print("************************************")
    op = input()
    return op
def IdentifyWordsMode():# 选择文字识别上传文件模式
    print("************************************")
    print("                                    ")
    print("  Your choice is text recognition   ")
    print("                                    ")
    print("[1] Read the file from the local file or url  ")#后接快速识别，高级识别选项
    print("                                    ")
    print("[2] Read the file from your clipboard")#后接快速识别，高级识别选项
    print("                                    ")
    print("[3] Read the file from your clipboard continuously                                  ")#快速识别返回结果，持续调用readfromclipboard
    print("                                    ")
    print("                                    ")
    print("[0] Delete the API Token of this function")
    print("                                    ")
    print("                                    ")
    print("Press Ctrol + C to shutdown this program     ")
    print("                                    ")
    print("************************************")
    op = input()
    return op
def IdentifyExcelMode():# 选择表格识别上传文件模式
    print("************************************")
    print("                                    ")
    print("  Your choice is table recognition   ")
    print("                                    ")
    print("[1] Read the file from the local file")
    print("                                    ")
    print("[2] Read the file from your clipboard")
    print("                                    ")
    print("[0] Delete the API Token of this function")
    print("                                    ")
    print("                                    ")
    print("************************************")
    op = input()
    return op
def AdvancedParmsofIdentifyWords(FileDictPair):# 制作高级文字识别的参数
    Parms={}
    Parms.update(FileDictPair)
    while True:
        Language_Type_Option = input("Do you want to choose the type of recognition language?(y/n)\t")
        if Language_Type_Option == "y" or Language_Type_Option == "Y":
            Language_Type_List=["CHN_ENG","ENG","JAP","KOR","FRE","SPA","POR","GER","ITA","RUS"]
            while True:
                print("You Can Choose The Language Below:")
                print("[0] CHN_ENG\t[1] ENG\t[2] JAP\t[3] KOR\t[4] FRE")
                print("[5] SPA\t\t[6] POR\t[7] GER\t[8] ITA\t[9] RUS")
                Language_Type_Idx = int(input("Please Input The MarkNumber of the Language\t"))
                if Language_Type_Idx <= 9 and Language_Type_Idx >= 0:
                    Parms.update({"language":Language_Type_List[Language_Type_Idx]})
                    break
                else:
                    print("Please input the correct MarkNumber")
            break
        elif Language_Type_Option == "n" or Language_Type_Option == "N":
            break
        else:
            print("Please input the correct options")
    while True:
        Paragraph_Option = input("Do you want to output paragraph information?(y/n)\t")
        if Paragraph_Option == "y" or Paragraph_Option == "Y":
            Parms.update({"paragraph":"true"})
            break
        elif Paragraph_Option == "n" or Paragraph_Option == "N":
            break
        else:
            print("Please input the correct options")
    while True:
        Probability_Option = input("Do you want to output the confidence of each row in the recognition result?(y/n)\t")
        if Probability_Option == "y" or Probability_Option == "Y":
            Parms.update({"probability":"true"})        
            break
        elif Probability_Option == "n" or Probability_Option == "N":
            break
        else:
            print("Please input the correct options")
    while True:
        Detect_Language_Option = input("Do you want to detect language?(y/n)\t")
        if Detect_Language_Option == "y" or Detect_Language_Option == "Y":
            Parms.update({"detect_language":"true"})
            break
        elif Detect_Language_Option == "n" or Detect_Language_Option == "N":
            break
        else:
            print("Please input the correct options")
    while True:
        Detect_Direction_Option = input("Do you want to detect image orientation?(y/n)\t")
        if Detect_Direction_Option == "y" or Detect_Direction_Option == "Y":
            Parms.update({"detect_direction":"true"})
            break
        elif Detect_Direction_Option == "n" or Detect_Direction_Option == "N":
            break
        else:
            print("Please input the correct options")
    if "pdf_file" in Parms.keys():
        while True:
            Pdf_File_Num_Option = input("Do you want to set the corresponding page number of the PDF file that needs to be recognized?(y/n),if not the default is first page\t")
            if Pdf_File_Num_Option == "y" or Pdf_File_Num_Option == "Y":
                Pdf_File_Num = int(input("Please input the number of pdf file,PLEASE INPUT CORRECT PAGE!!!\t"))
                Parms.update({"pdf_file_num":Pdf_File_Num})
                break
            elif Pdf_File_Num_Option == "n" or Pdf_File_Num_Option == "N":
                break
            else:
                print("Please input the correct options")
    return Parms
def FirstRunThisMode(ModeName):# 第一次运行模式获取Token
    print("                                         ")
    print("                        This Program Based on Baidu AI Cloud                                        ")
    print("If you want to use the corresponding function,you need corresponding API key and API secret key first")
    print("Then you need input corresponding API key and API secret key")
    print("You can change it later")
    Token = GetAccess_Token.GetAccessToken()
    if(Token == "Error"):
        print("The Info you input is wrong,don't be a obtuse angle!")
        sleep(8)
        sys.exit(0)
    else:
        f = open(ModeName+"Token",'w')
        f.write(Token)
        f.close()
        print("The Token of {} has been saved in the file:{}".format(ModeName,ModeName+"Token"))
def IdentifyWordsModeZero():# 删除文字识别Token
    if(os.path.exists("IdentifyWordsToken")):
        os.remove(r"IdentifyWordsToken")
        print("Delete Success!")
    else:
        print("You Don't have the Token of Identify Words !")
        restart()
def IdentifyExeclModeZero():# 删除表格识别Token    
    if(os.path.exists("IdentifyExcelToken")):
        os.remove(r"IdentifyExcelToken")
        print("Delete Success!")
    else:
        print("You Don't have the Token of Identify Excel !")
        restart()
def IdentifyTravelCardModeZero():# 删除表格识别Token    
    if(os.path.exists("IdentifyTravelCard")):
        os.remove(r"IdentifyTravelCard")
        print("Delete Success!")
    else:
        print("You Don't have the Token of Travel Card !")
        restart()
def IdentifyWordsSetting():# 文字识别识别模式
    print("[1] Fast Identify")
    print("[2] Advanced Identify")
    op = input()
    return op
def restart():
    input("Please Press Enter to continue!")
# Driver Code
while True:
    while True:
        ModeOption = ChooseMode()
        if ModeOption == "1" or ModeOption == "2" or ModeOption == "3" or ModeOption == "0" or ModeOption == "q" :
            break
        else:
            print("Please Input The Correct Options")
    if ModeOption == "1":# Identify Words Mode
        #Check Token exist
        if os.path.exists("IdentifyWordsToken"):
            print(" The program checks you have historical Token of this mode,")
            print(" we will use your previous Token,")
            print(" please confirm that this Token is available,  ")
            print(" if you want to change,please return to the upper layer to clear the Token of this mode")
        else:
            FirstRunThisMode("IdentifyWords")
        with open("IdentifyWordsToken",'r') as tk:
            AccessToken = tk.read()
        while True:
            IdentifyWordsModeOption = IdentifyWordsMode()
            if IdentifyWordsModeOption == "1" or IdentifyWordsModeOption == "2" or IdentifyWordsModeOption == "0" or IdentifyWordsModeOption == "3":
                break
            else:
                print("Please Input The Correct Options")
        if IdentifyWordsModeOption == "1":#Advanced
            while True:
                print("Please enter a picture in the format of jpg,jpeg,png,bmp or a url")
                FileName = r""
                FileName = input("Please Input The FileName or Url\n")
                FileDictPair = IdentifyWords.auto_select_file(FileName)
                if FileDictPair == "Error":
                    print("Is Wrong!")
                else:
                    print("File is Processed")
                    break
            while True:
                IdentifyWordsSettingOption = IdentifyWordsSetting()
                if IdentifyWordsSettingOption == "1":
                    IdentifyWords.Identify_Words(AccessToken,FileDictPair)
                    break
                elif IdentifyWordsSettingOption == "2":
                    IdentifyWords.Identify_Words(AccessToken,AdvancedParmsofIdentifyWords(FileDictPair))
                    break
                else:
                    print("Please Input Correct Option")
            restart()
        elif IdentifyWordsModeOption == "2":#Advanced
            while not CheckIfIsImage():
                print("The Content of Your Clipboard is not a image")
                sleep(5)
            print("The Image from your Clipboard have been read !")
            FileDictPair = {"image":ClipboardImageToBase64()}      
            while True:
                IdentifyWordsSettingOption = IdentifyWordsSetting()
                if IdentifyWordsSettingOption == "1":
                    IdentifyWords.Identify_Words(AccessToken,FileDictPair)
                    break
                elif IdentifyWordsSettingOption == "2":
                    IdentifyWords.Identify_Words(AccessToken,AdvancedParmsofIdentifyWords(FileDictPair))
                    break
                else:
                    print("Please Input Correct Option")
            restart()
        elif IdentifyWordsModeOption == "3":#Just Fast Identify
            print("You Can Stop by Control-C")
            print("You Must Make Sure Your Clipboard Is Image")
            t = int(input("Please enter the time interval at which we detect your clipboard\t"))
            st = input("Please Press Any Key To Start")
            PastFileDictPair = {}
            while CheckIfIsImage():
                sleep(t)
                FileDictPair = {"image":ClipboardImageToBase64()}
                if FileDictPair != PastFileDictPair:
                    IdentifyWords.Identify_Words(AccessToken,FileDictPair)#IdentifyWordsToken
                    PastFileDictPair = FileDictPair
            print("Your Clipboard is not a image!")
            restart()
        elif IdentifyWordsModeOption == "0":
            IdentifyWordsModeZero()
            restart()
    elif ModeOption == "2":# Identify Excel Mode
        #Check Token exist
        if os.path.exists("IdentifyExcelToken"):
            print(" The program checks you have historical Token of this mode,")
            print(" we will use your previous Token,")
            print(" please confirm that this Token is available,  ")
            print(" if you want to change, please return to the upper layer to clear the Token of this mode")
        else:
            FirstRunThisMode("IdentifyExcel")
        with open("IdentifyExcelToken",'r') as tk:
            AccessToken = tk.read()
        while True:#
            IdentifyExcelModeOption = IdentifyExcelMode()
            if IdentifyExcelModeOption == "1" or IdentifyExcelModeOption == "2"  or IdentifyExcelModeOption == "0" :
                break
            else:
                print("Please Input The Correct Options")
        Params = {"is_sync":"true","request_type":"excel"}
        if IdentifyExcelModeOption == "1":
            while True:
                print("Please enter a picture in the format of jpg,jpeg,png,bmp or a url")
                FileName = r""
                FileName = input("Please Input The FileName or Url\n")
                FileDictPair = IdentifyExcel.process_file(FileName)
                if FileDictPair == "Error":
                    print("Is Wrong!")
                else:
                    print("File is Processed")
                    break
            Params.update(FileDictPair)
            IdentifyExcel.Identify_Excel(AccessToken,Params)
            restart()
        elif IdentifyExcelModeOption == "2":
            while not CheckIfIsImage():
                print("The Content of Your Clipboard is not a image")
                sleep(5)
            print("The Image from your Clipboard have been read !")
            FileDictPair = {"image":ClipboardImageToBase64()}     
            Params.update(FileDictPair)
            IdentifyExcel.Identify_Excel(AccessToken,Params)
            restart()
        elif IdentifyExcelModeOption == "0":
            IdentifyExeclModeZero()
            restart()
    elif ModeOption == '3':
        #Check Token exist
        if os.path.exists("IdentifyTravelCardToken"):
            print("The program checks you have historical Token of this mode,")
            print("We will use your previous Token,")
            print("Please confirm that this Token is available.")
        else:
            FirstRunThisMode("IdentifyTravelCard")
        op = input("Do You Want Remove Your Token Of IdentifyTravelCard?(y/n)\n")
        if op == 'y' or op == 'Y':
            if(os.path.exists("IdentifyTravelCardToken")):
                os.remove(r"IdentifyTravelCardToken")
                print("Delete Success!")
            else:
                print("You Don't have the Token of Identify Words !")
                restart()
        with open("IdentifyTravelCardToken",'r') as tk:
            AccessToken = tk.read()
        print("Please enter a picture in the format of jpg,jpeg,png,bmp")
        File_Path = r""
        File_Path = input("Please Input The File Path\n")
        IdentifyTravelCard.ProcessData(IdentifyTravelCard.GetResDict(AccessToken,IdentifyTravelCard.ProcessFile(File_Path)))
    elif ModeOption == "0":
        print("This Program Based On BaiDu AI Cloud")
        print("The url of official documentation : https://ai.baidu.com/ai-doc/OCR/")
        print("If You Want More Function, Please tell me in the Gitee or GitHub")
        restart()
    elif ModeOption == "q":
        sys.exit(0)

