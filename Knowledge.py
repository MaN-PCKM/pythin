from tkinter import *
from tkinter import ttk
from tkinter import messagebox

################csv#################
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) #datalist ['pen','pencil']


def readcsv():
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
################csv#################


GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('900x400')

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.pack()

######################
def Button2():
    text = 'เงินในบัญชีมี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    
FB1=Frame(GUI)#คล้ายกับกระดาน
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)

######################

######################
def Button2():
    text = 'เงินในบัญชีมี 30 บาท'
    messagebox.showinfo('เงินในบัญชีของลูกมี',text)
    
FB1=Frame(GUI)#คล้ายกับกระดาน
FB1.place(x=100,y=200)
B2 = ttk.Button(FB1,text='เงินในบัญชีของลูกมี',command=Button2)
B2.pack(ipadx=20,ipady=20)

######################

######################
def Button2():
    text = 'เงินในบัญชีมี 3,000 บาท'
    messagebox.showinfo('เงินในบัญชีของเมีย',text)
    
FB1=Frame(GUI)#คล้ายกับกระดาน
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินในบัญชีของเมีย',command=Button2)
B2.pack(ipadx=20,ipady=20)

##########Section Right#######

LF1 = ttk.LabelFrame(GUI,text='กรอกข้อมูลที่ต้องการเข้าไป')
LF1.place(x=400,y=50)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(padx=10,pady=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get()
    text = [t,data]
    writecsv(text)
    v_data.set('')

B3 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B3.pack(ipadx=20,ipady=20)




GUI.mainloop()
