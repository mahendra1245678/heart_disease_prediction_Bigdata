#### --------------------------------------- IMPORTING MODULES ---------------------------------------- ####
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import ctypes
import pandas as pd
import tkinter.messagebox as tkMessageBox
import numpy as np
import os,PIL
from tkinter import messagebox
import re,joblib
global window
from sklearn.model_selection import train_test_split



l1 = ['SEQN', 'Gender', 'Age', 'Annual-Family-Income', 'Ratio-Family-Income-Poverty', 'X60-sec-pulse', 'Systolic', 'Diastolic', 'Weight', 'Height', 'Body-Mass-Index', 'White-Blood-Cells', 'Lymphocyte', 'Monocyte', 'Eosinophils', 'Basophils', 'Red-Blood-Cells', 'Hemoglobin', 'Mean-Cell-Vol', 'Mean-Cell-Hgb-Conc.', 'Mean-cell-Hemoglobin', 'Platelet-count', 'Mean-Platelet-Vol', 'Segmented-Neutrophils', 'Hematocrit', 'Red-Cell-Distribution-Width', 'Albumin', 'ALP', 'AST', 'ALT', 'Cholesterol', 'Creatinine', 'Glucose', 'GGT', 'Iron', 'LDH', 'Phosphorus', 'Bilirubin', 'Protein', 'Uric.Acid', 'Triglycerides', 'Total-Cholesterol', 'HDL', 'Glycohemoglobin', 'Vigorous-work', 'Moderate-work', 'Health-Insurance', 'Diabetes', 'Blood-Rel-Diabetes', 'Blood-Rel-Stroke']
disease = ["no","yes"]
tr=pd.read_csv("./CardiacPrediction.csv")
X= tr[l1]
y = tr[["CoronaryHeartDisease"]]
X, X_test, y, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

clf3 = joblib.load("dtc.pkl")
clf4= joblib.load("rfc.pkl")
gnb = joblib.load("gnb.pkl")

from sklearn.metrics import accuracy_score
y_pred=clf3.predict(X_test)
score_dt=accuracy_score(y_test, y_pred)

from sklearn.metrics import accuracy_score
y_pred=clf4.predict(X_test)
score_rf=accuracy_score(y_test, y_pred)

from sklearn.metrics import accuracy_score
y_pred=gnb.predict(X_test)
score_nb=accuracy_score(y_test, y_pred)


def heart():
    global window
    def dt():
        l2=[]
        for x in range(0,len(l1)):
            l2.append(0)
        val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11=v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get(),v11.get()
        l2[2]=val1
        l2[5]=val2
        l2[10]=val3
        l2[11]=val4
        l2[16]=val5
        l2[17]=val6
        l2[43]=val7
        l2[6]=val8
        l2[7]=val9
        l2[49]=val10
        l2[47]=val11
        predict = clf3.predict([l2])
        out = disease[predict[0]]
        if out=="no":
            tkMessageBox.showinfo("Heart Disease Prediction","According to the prediction from decision tree algorith you don't have chances for heart disease. Accuracy = "+str(round(score_dt*100,2)))
        else:
            tkMessageBox.showinfo("Heart Disease Prediction","According to the prediction from decision tree algorith you have chances for heart disease. Accuracy = "+str(round(score_dt*100,2)))
   
    def res():
        v1.set(0);v2.set(0);v3.set(0);v4.set(0);v5.set(0);v6.set(0);v7.set(0);v8.set(0);v9.set(0);v10.set(0);v11.set(0)
  
    def rf():
        l2=[]
        for x in range(0,len(l1)):
            l2.append(0)
        val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11=v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get(),v11.get()
        l2[2]=val1
        l2[5]=val2
        l2[10]=val3
        l2[11]=val4
        l2[16]=val5
        l2[17]=val6
        l2[43]=val7
        l2[6]=val8
        l2[7]=val9
        l2[49]=val10
        l2[47]=val11
    
        predict = clf4.predict([l2])
        out = disease[predict[0]]
        if out=="no":
            tkMessageBox.showinfo("Heart Disease Prediction","According to the prediction from random forest algorith you don't have chances for heart disease. Accuracy = "+str(round(score_rf*100,2)))
        else:
            tkMessageBox.showinfo("Heart Disease Prediction","According to the prediction from random forest algorith you have chances for heart disease. Accuracy = "+str(round(score_rf*100,2)))
   
     
        
    def nb():
        l2=[]
        for x in range(0,len(l1)):
            l2.append(0)
        val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11=v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get(),v11.get()
        l2[2]=val1
        l2[5]=val2
        l2[10]=val3
        l2[11]=val4
        l2[16]=val5
        l2[17]=val6
        l2[43]=val7
        l2[6]=val8
        l2[7]=val9
        l2[49]=val10
        l2[47]=val11

        predict = gnb.predict([l2])
        out = disease[predict[0]]
        
        if out=="no":
            tkMessageBox.showinfo("Heart Disease Prediction","According to the prediction from Naive Bayes algorith you don't have chances for heart disease. Accuracy = "+str(round(score_nb*100,2)))
        else:
            tkMessageBox.showinfo("Heart Disease Prediction","According to the prediction from Naive Bayes algorith you have chances for heart disease. Accuracy = "+str(round(score_nb*100,2)))
   
        
        
    window = Tk()

    window.resizable(0,0)

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-446)
    b= str(lt[1]//2-383)

    window.geometry("892x710+"+a+"+"+b)
    window.title('HeartDiseasePrediction')

    img = Image.open(r"Images/bg.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.pack(side="top", fill="both", expand="yes")

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    v1 = IntVar()
    v2 = IntVar()
    v3 = DoubleVar()
    v4 = DoubleVar()
    v5 = DoubleVar()
    v6 = DoubleVar()
    v7 = DoubleVar()
    v8 = IntVar()
    v9 = IntVar()
    v10 = IntVar()
    v11 = IntVar()
    
    v1.set(0);v2.set(0);v3.set(0);v4.set(0);v5.set(0);v6.set(0);v7.set(0);v8.set(0);v9.set(0);v10.set(0);v11.set(0)
    canvas = Canvas(window, bg="firebrick3", height=457, width=888)
    canvas.place(x=0,y=249)

    agel = Label(canvas, text="Age :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    agel.place(x = 30,y = 2)

    agee = Entry(canvas, textvariable=v1, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    agee.place(x=465, y=11)

    genl = Label(canvas, text="X60-sec-pulse :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    genl.place(x = 30,y = 31)

    gene = Entry(canvas, textvariable=v2, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    gene.place(x=465, y=40)

    cpl = Label(canvas, text="Body-Mass-Index :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    cpl.place(x = 30,y = 60)

    cpe = Entry(canvas, textvariable=v3, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    cpe.place(x=465, y=69)

    rbpl = Label(canvas, text="White-Blood-Cells :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    rbpl.place(x = 30,y = 293)

    rbpe = Entry(canvas, textvariable=v4, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    rbpe.place(x=465, y=300)

    rbpl = Label(canvas, text="Red-Blood-Cells :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    rbpl.place(x = 30,y = 89)

    rbpe = Entry(canvas, textvariable=v5, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    rbpe.place(x=465, y=98)

    lchol = Label(canvas, text="Heamoglobin :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    lchol.place(x = 30,y = 118)

    echol = Entry(canvas, textvariable=v6, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    echol.place(x=465, y=127)

    lfbs = Label(canvas, text="Glycohemoglobin :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    lfbs.place(x = 30,y = 147)

    efbs = Entry(canvas, textvariable=v7, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    efbs.place(x=465, y=156)

    lres = Label(canvas, text="Systolic :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    lres.place(x = 30,y = 176)

    eres = Entry(canvas, textvariable=v8, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    eres.place(x=465, y=185)

    lmha = Label(canvas, text="Diastolic :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    lmha.place(x = 30,y = 205)

    emha = Entry(canvas, textvariable=v9, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    emha.place(x=465, y=214)

    leia = Label(canvas, text="Blood-rel-stroke :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    leia.place(x = 30,y = 234)

    leiae = Entry(canvas, textvariable=v10, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    leiae.place(x=465, y=243)

    stl = Label(canvas, text="Diabetes :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    stl.place(x = 30,y = 263)

    ste = Entry(canvas, textvariable=v11, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    ste.place(x=465, y=272)


    bh = Button(canvas, text="Decision Tree", fg="black", bg="#FFB6B6", width = 22,
                font=("Calibri", "16",'bold'),command=dt)
    bh.place(x=30, y=390)

    bh = Button(canvas, text="Random Forest", fg="black", bg="#FFB6B6", width = 22,
                font=("Calibri", "16",'bold'),command=rf)
    bh.place(x=325, y=390)

    bh = Button(canvas, text="Naive Bayes", fg="black", bg="#FFB6B6", width = 22,
                font=("Calibri", "16",'bold'),command=nb)
    bh.place(x=621, y=390)

    bh = Button(canvas, text="Reset", fg="black", bg="#FFB6B6", width = 22,
                font=("Calibri", "16",'bold'),command=res)
    bh.place(x=621, y=335)
    
    window.mainloop()
    
heart()




# sample
