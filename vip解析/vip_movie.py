#!/usr/bin/python3
# coding:utf-8


import  requests
import re
import tkinter as tk
import webbrowser
url = "http://www.qmaile.com/"
responed = requests.get(url)
responed.encoding=responed.apparent_encoding
responeds = responed.text
# print(responeds)
reg=re.compile('<option value="(.*?)" selected="">')
res= re.findall(reg ,responeds)
print(res)
one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]
root = tk.Tk()
root.geometry("500x270")
root.title('vip电影')
l1 = tk.Label(root,text='播放接口：',font=12)
l1.grid()
#value的值传给variable
var = tk.StringVar()
r1=tk.Radiobutton(root,text="播放接口1",variable=var,value=one)
r1.grid(row=0,column=1)
r2=tk.Radiobutton(root,text="播放接口2",variable=var,value=two)
r2.grid(row=1,column=1)
r3=tk.Radiobutton(root,text="播放接口3",variable=var,value=three)
r3.grid(row=2,column=1)
r4=tk.Radiobutton(root,text="播放接口4",variable=var,value=four)
r4.grid(row=3,column=1)
r5=tk.Radiobutton(root,text="播放接口5",variable=var,value=five)
r5.grid(row=4,column=1)
l2 = tk.Label(root,text="播放地址:",font=12)
l2.grid(row=5,column=0)
e1 = tk.Entry(root,text="",width=50)
e1.grid(row=5,column=1)
def bf():
    webbrowser.open(var.get()+e1.get())
b1 = tk.Button(root,text="播放",font=5,width=5,command=bf)
b1.grid(row=6,column=1)
def qc():
    e1.delete(0,'end')
b2 = tk.Button(root,text="清除",font=5,width=5,command=qc)
b2.grid(row=7,column=1)
root.mainloop()