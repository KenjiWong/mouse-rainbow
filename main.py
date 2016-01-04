# encoding=utf-8

from pymouse import PyMouse
import pdb
import time
import random
import pyHook
from win32api import GetSystemMetrics
import pythoncom
import os

kk = ''
def onKeyboardEvent(event):
    global kk
    kk = kk + event.Key
    print kk
    if event.KeyID==13:
        if(kk != 'SHUADHReturn'):
            kk = ''
        else:
            os._exit(0)
    else:
        x = random.uniform(int(m.position()[0]-100), int(m.position()[0]+100))
        y = random.uniform(int(m.position()[1]-100), int(m.position()[1]+100))
        m.move(int(x), int(y))
        m.move(m.position()[0], m.position()[1])
    return True

hm = pyHook.HookManager()
hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()

start_time = time.time()
end_time = start_time + 30
m = PyMouse()
pythoncom.PumpMessages()
# while(time.time() < end_time):
