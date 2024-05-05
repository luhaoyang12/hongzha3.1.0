# -*- coding:utf-8 -*-
from pynput.keyboard import Key, Controller

import os
import time
import dome1
import dome2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False
    #使用:https://blog.csdn.net/m0_37622530/article/details/81289520
def main():
    def sad():
        with open(os.path.join(os.getcwd(), 'a.txt\\activation.txt'), "r+", encoding='UTF-8')as f:
            if f.read() == '12344321':
                a = send_a.get()
                b = IntervalTime_a.get()
                if is_number(a)==False:
                    messagebox.showinfo('提示','发送次数为正整数')
                if is_number(b)==False:
                    messagebox.showinfo('提示', '发送次数为正数')
                else:
                    IntervalTime = float(b)
                    send = int(a)
                    text = text_a.get()
                    w.destroy()
                    keyboard = Controller()
                    if send==0:
                        dome1.dome0()
                        while True:
                            keyboard.type(text)
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                            time.sleep(IntervalTime)
                    else:
                        dome1.dome0()
                        for s in range(send):
                            keyboard.type(text)
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                            time.sleep(IntervalTime)
                        def a1():
                            e.destroy()
                            dome1.a()
                        e = tk.Tk()
                        e.geometry('200x100+700+400')
                        d = tk.Label(e, text='运行完成！', fg="black", font=('Times', 25))
                        d.pack()
                        p = ttk.Button(e, text='确定', command=e.destroy)
                        p.pack()
                        o = ttk.Button(e, text='返回', command=a1)
                        o.pack()
            else:
                messagebox.showinfo('提示', '     请先激活      ')
    w = tk.Tk()
    def dome0():
        w.destroy()
        dome2.sss()
    w.geometry('300x200+700+400')
    w.title("tk GUI")

    ttk.Label(w, text="发送次数:", font=('Times', 12)).place(x=10, y=30)
    send_a = ttk.Entry(w, width=20, )
    send_a.place(x=85, y=32)

    ttk.Label(w, text='内容:', font=('Times', 12)).place(x=10, y=60)
    text_a = ttk.Entry(w, width=20, )
    text_a.place(x=85, y=62)

    ttk.Label(w, text='间隔时长:', font=('Times', 12)).place(x=10, y=90)
    IntervalTime_a = ttk.Entry(w, width=20)
    IntervalTime_a.place(x=85, y=92)

    ttk.Button(w, text='发送', command=sad).place(x=115, y=130)
    tk.Button(w, text='更多', command=dome0).place(x=260, y=10)

    w.mainloop()

if __name__ == '__main__':
    main()