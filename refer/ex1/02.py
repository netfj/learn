#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   02.py 
time:   2019/2/27.18:49
"""


import tkinter

import tkinter.messagebox



def showMsg(): #提示框
    tkinter.messagebox.showinfo('提示', '123')
    tkinter.messagebox.showwarning('警告', '234')
    tkinter.messagebox.showerror('错误', '345')

showMsg()