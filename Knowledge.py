from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x500')

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

######################



GUI.mainloop()
