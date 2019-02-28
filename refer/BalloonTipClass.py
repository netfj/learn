#coding:utf-8
"""
info:   气泡提示
        需要安装 pywin32 模块
        方法：pip install pywin32
author: NetFj@sina.com
file:   BalloonTipClass.py
time:   2019/2/27.20:16
"""

"""
info:   
author: NetFj@sina.com
file:   04.py 
time:   2019/2/27.19:03
"""
from win32api import *
from win32gui import *
import win32con
import sys, os
import time
import importlib
importlib.reload(sys)

class WindowsBalloonTip:
    def __init__(self, title, msg):
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(classAtom, "Taskbar", style, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join(sys.path[0], "balloontip.ico"))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
            hicon = LoadImage(hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, (self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20, hicon, "Balloon  tooltip", title, 200, msg))
        # self.show_balloon(title, msg)

        #下面两行可选，用于定时消除气泡
        # time.sleep(10)
        # DestroyWindow(self.hwnd)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)  # Terminate the app.

def balloon_tip(title, msg):
    w = WindowsBalloonTip(msg, title)

if __name__ == "__main__":
    balloon_tip('有新消息啦', '这是新消息')
