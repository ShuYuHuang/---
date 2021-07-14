# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
import time
import tkinter.font as fnt
import numpy as np
import pandas as pd
import random
from PIL import ImageTk, Image
win = Tk()
win.geometry("1024x768")
win.resizable(width=True, height=True)
win.title("各國地理問答-重製版1.0")
myFont = fnt.Font(family='新細明體', size=20, weight='bold')
questions=pd.read_csv("questions.csv",encoding="ansi")
#造出隨機序列
qzQueue=list(range(len(questions)))
random.shuffle(qzQueue)
numInQue=0
#初始化總和計算
totalCount=len(questions)
correctCount=0

def Ans_1():
    global ans,numInQue,correctCount
    numInQue+=1
    if ans == 1:
        correctCount +=1
    game_main()
def Ans_2():
    global ans,numInQue,correctCount
    numInQue += 1
    if ans == 2:
        correctCount +=1
    game_main()
def Ans_3():
    global ans,numInQue,correctCount
    numInQue += 1
    if ans == 3:
        correctCount +=1
    game_main()
def Ans_4():
    global ans,numInQue,correctCount
    numInQue += 1
    if ans == 4:
        correctCount +=1
    game_main()

def game_main():
    global ans,qz_img,Lbl,panel,Btn_1,Btn_2,Btn_3,Btn_4,numInQue,totalCount
    #若題目還沒做完的情況
    if numInQue<totalCount:
        #亂數選取題目
        qz_number=qzQueue[numInQue]
        #題目答案
        ans = questions["correct"][qz_number]
        #題目圖片
        #qz_img = Image.open(questions["picture"][qz_number])
        #qz_img = qz_img.resize((50,50), Image.ANTIALIAS)
        qz_img = PhotoImage(file=questions["picture"][qz_number])
        WW,HH=qz_img.width(),qz_img.height()
        qz_img=qz_img.subsample(x=3, y=3)
        #print(qz_img.width())
        #print(qz_img.height())
        #抓取相關文字進按鈕
        Lbl = Label(win,text=questions["question"][qz_number], font=myFont, width=40, height=10)
        Lbl.grid(row=0, column=0, columnspan=10)
        panel = Label(win, image=qz_img,  width=200, height=300)
        panel.grid(row=1, column=0)
        Btn_1 = Button(win,text="1."+questions["answer1"][qz_number], font=myFont, width=52, height=2, fg="blue", command=lambda: Ans_1())
        Btn_1.grid(row=2, column=0)
        Btn_2 = Button(win,text="2."+questions["answer2"][qz_number], font=myFont, width=52, height=2, fg="blue", command=lambda: Ans_2())
        Btn_2.grid(row=2, column=2)
        Btn_3= Button(win,text="3."+questions["answer3"][qz_number], font=myFont, width=52, height=2, fg="blue", command=lambda: Ans_3())
        Btn_3.grid(row=3, column=0)
        Btn_4 = Button(win,text="4."+questions["answer4"][qz_number], font=myFont, width=52, height=2, fg="blue", command=lambda: Ans_4())
        Btn_4.grid(row=3, column=2)
        win.mainloop()
    else:
        # 若題目已經做完的情況
        Lbl_title=Label(text="各國地理問答",font=myFont,width=50, height=2)
        Lbl_title.grid(row=0, column=0, columnspan=4)
        qz_number=0
        Btn_startgame=Button(text="離開",font=myFont, width=5, height=2, fg="black", command=lambda: game_main())
        Btn_startgame.grid(row=4, column=0)
        Btn_quitgame=Button(text="回到開始畫面",font=myFont, width=5, height=2, fg="black", command=lambda: win.destroy())
        Btn_quitgame.grid(row=4, column=2)
        win.mainloop()
        
        Lbl_title.grid(row=0, column=0, columnspan=4)
        
        Btn_startgame = Button(text="進入", font=myFont, width=5, height=2, fg="black", command=lambda: game_main())
        Btn_startgame.grid(row=4, column=0)
        Btn_quitgame = Button(text="離開", font=myFont, width=5, height=2, fg="black", command=lambda: win.destroy())
        Btn_quitgame.grid(row=4, column=2)
        win.mainloop()

Lbl_title=Label(text="各國地理問答",font=myFont,width=50, height=2)

Lbl_title.grid(row=0, column=0, columnspan=4)
qz_number=0
Btn_startgame=Button(text="進入",font=myFont, width=5, height=2, fg="black", command=lambda: game_main())
Btn_startgame.grid(row=4, column=0)
Btn_quitgame=Button(text="離開",font=myFont, width=5, height=2, fg="black", command=lambda: win.destroy())
Btn_quitgame.grid(row=4, column=2)
win.mainloop()

win = Tk()
win.geometry("1024x768")
win.resizable(width=True, height=True)
win.title("各國地理問答-重製版1.0")
myFont = fnt.Font(family='新細明體', size=20, weight='black')
#造出隨機序列
qzQueue=list(range(len(questions)))
random.shuffle(qzQueue)
numInQue=0
#初始化總和計算
totalCount=len(questions)
correctCount=0
Lbl_title = Label(text="遊戲結束", font=myFont, width=50, height=2)
Lbl_title.grid(row=0, column=0, columnspan=4)
Btn_startgame = Button(text="回到開始畫面", font=myFont, width=12, height=2, fg="black")
Btn_startgame.grid(row=4, column=0)
Btn_quitgame = Button(text="離開", font=myFont, width=5, height=2, fg="black", command=lambda: win.destroy())
Btn_quitgame.grid(row=4, column=2)
win.mainloop()

Lbl_title.grid(row=0, column=0, columnspan=4)

Btn_startgame = Button(text="進入", font=myFont, width=5, height=2, fg="black")
Btn_startgame.grid(row=4, column=0)
Btn_quitgame = Button(text="離開", font=myFont, width=5, height=2, fg="black", command=lambda: win.destroy())
Btn_quitgame.grid(row=4, column=2)
win.mainloop()
