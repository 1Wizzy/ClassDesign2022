# encoding: utf-8

# 注意！！！请在代码中输入您的百度AI文字识别API的Token！
# Attention！！！Please enter your Baidu AI text recognition API Token in the code！

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

import IdentifyWords

"""
Function: GUI of IdentifyWords
Author: Long Marui WizzyAng
"""
language_type = "None"  # 识别语言类型
detect_language = False  # 检测语言
Paragraph = False  # 输出段落信息
probability = False  # 返回置信度
File__name = ''  # 文件地址

window = tk.Tk()
window.title('Identify Word')  # 窗口名字
window.geometry("1900x950")  # 宽**高

# 图片
canvas = tk.Canvas(window, bg="white", height=8000, width=6000)

image_file_01 = tk.PhotoImage(file="013.png")
image_01 = canvas.create_image(0, 0, anchor='nw', image=image_file_01)

image_file_02 = tk.PhotoImage(file="011.png")  # 威尔史密斯
image_02 = canvas.create_image(650, 400, anchor='nw', image=image_file_02)

image_file_03 = tk.PhotoImage(file="012.png")  # 识别结果
image_03 = canvas.create_image(650, 350, anchor='nw', image=image_file_03)

canvas.place(x=0, y=0)


# 上方按钮
#  下拉框

def choose(event):
    global language_type
    language_type = value.get()



l = tk.Label(window, text="识别语言类型",  # 字符串变量
             font=("Arial", 12),  # label:标签
             width=15, height=2)  # bg:背景颜色  font:字体 text：文本
l.place(x=350, y=0)  # 安置：相对的上下左右
value = StringVar()
value.set('CHN_ENG')  # 默认选中CCC==combobox.current(2)
values = ['CHN_ENG', 'CHN', 'ENG', 'JAP', 'KOR', 'FRE', 'SPA', 'POR', 'GER', 'ITA', 'RUS']

combobox = ttk.Combobox(
    master=window,  # 父容器
    height=20,  # 高度,下拉显示的条目数量
    width=20,  # 宽度
    state='normal',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
    cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
    font=('', 20),  # 字体
    textvariable=value,  # 通过StringVar设置可改变的值
    values=values,  # 设置下拉框的选项
)
combobox.place(x=500, y=0)
combobox.bind('<<ComboboxSelected>>', choose)


# button 3  About
def b3_command():
    tk.messagebox.showinfo(title="Hi", message="此程序基于百度AI开发平台")


b3_About = tk.Button(window, text="关于", width=15, height=2, command=b3_command,
                     bg="white")
b3_About.place(x=1000, y=0)

# 下方选项

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()


def c1_Paragraph():
    global Paragraph
    if var1.get() == 1:
        Paragraph = True
    elif var1.get() == 0:
        Paragraph = False


c1 = tk.Checkbutton(window, text="输出段落信息", variable=var1, onvalue=1, offvalue=0,
                    width=15, height=2, command=c1_Paragraph,
                    bg="white")
c1.place(x=0, y=200)


def c2_probability():
    global probability
    if var2.get() == 1:
        probability = True
        print(probability)
    elif var2.get() == 0:
        probability = False
        print(probability)


c2 = tk.Checkbutton(window, text="返回置信度", variable=var2, onvalue=1, offvalue=0,
                    width=15, height=2, command=c2_probability,
                    bg="white")
c2.place(x=0, y=300)


def c3_language():
    global detect_language
    if var3.get() == 1:
        detect_language = True
    elif var3.get() == 0:
        detect_language = False


c3 = tk.Checkbutton(window, text="检测语言", variable=var3, onvalue=1, offvalue=0,
                    width=15, height=2, command=c3_language,
                    bg="white")
c3.place(x=0, y=400)


# 开始识别

def Identify_Words():  # 开始识别
    global File__name
    File__name = File__name__e.get()  # 获取地址
    IdentifyWords.Identify_Words_GUI("【TOKEN HERE】",
                                     IdentifyWords.MakeParams(File__name, language_type, detect_language,
                                                              Paragraph, probability))
    with open("log", mode='rb') as val:
        ans = val.read()
    os.remove(r"log")
    res =  ans.decode()
    t.insert("insert",res)


File__name__b = tk.Button(window, text='开始识别', width=15, height=2, command=Identify_Words,
                          bg="white")
File__name__b.place(x=0, y=0)

# 输入地址
l1 = tk.Label(window, text="文件路径或网络地址",  # 字符串变量
              bg="grey", font=("Arial", 12),  # label:标签
              width=15, height=2)  # bg:背景颜色  font:字体 text：文本
l1.place(x=0, y=100)  # 安置：相对的上下左右
File__name__e = tk.Entry(window, show=None)  # 输入框
File__name__e.place(x=142, y=110)
# 注释
l2 = tk.Label(window, text="(格式仅限jpg jpeg png bmp)",  # 字符串变量
              bg="white", font=("Arial", 12),  # label:标签
              width=25, height=2)  # bg:背景颜色  font:字体 text：文本
l2.place(x=280, y=100)
# 输出文本框
t = tk.Text(window, height=33, width=100)
t.place(x=900, y=350)

window.mainloop()  # 不断地循环：点击后有反应
