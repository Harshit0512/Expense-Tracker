#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook

import sqlite3
mydb=sqlite3.connect('expense.db')
cursor=mydb.cursor()
cursor.execute('create table if not exists expense (date_ timestamp  not null , title varchar(255) , price float(10) )')
def Addexpense():
    global adddate
    a=adddate.get()
    b=Title1.get()
    c=Expense.get()
    cursor.execute(f'insert into expense values("{a}","{b}",{c})')
    mydb.commit()
    data=[a,b,c]
    print(data)
    TVExpense.insert('','end',values=data)
    
    
def View1expense():
    global Title2
    a=adddate2.get()
    print(a)
    b=Title2.get()
    print(b)
    if b.lower()=='all':
        cursor.execute(f"select * from expense where date_='{a}'")
        f=cursor.fetchall()
        
        
    else :
        cursor.execute(f'select * from expense where date_="{a}" and title="{b}"')
        f=cursor.fetchall()
    for i in f:
            print(i)
            RVExpense.insert('','end',values=list(i))
def View2expense():
    global Title
    a=adddate3.get()
    c=adddate4.get()
    b=Title.get()
    print(b)
    if b.lower()=='all':
        cursor.execute(f"select * from expense where date_ between '{a}' and '{c}' ")
        f=cursor.fetchall()
        #print(type(f))
        
    else :
        cursor.execute(f'select * from expense where date_ between "{a}" and "{c}" and title ="{b}"')
        f=cursor.fetchall()
    for i in f:
            print(i)
            PVExpense.insert('','end',values=list(i))
def clear():
    PVExpense.delete(*PVExpense.get_children())
def clear2():
    RVExpense.delete(*RVExpense.get_children())

GUI=Tk()
GUI.title('EXPENSE TRACKER')
GUI.geometry('618x500')
#Maximize window

#GUI.state('zoomed')

Tab=Notebook(GUI)

F1=Frame(Tab, width=500, height=500)
F2=Frame(Tab, width=500, height=500)

Tab.add(F1, text='Expense')
Tab.add(F2, text='Date Wise View')

Tab.pack(fill=BOTH, expand=1)

F3=Frame(Tab, width=500, height=500)
Tab.add(F3, text='Date Range Wise View')
Tab.pack(fill=BOTH, expand=1)
#Tab 1 (Expense)

#............Row 0.....................
LDate=ttk.Label(F1, text='DATE:-', font=(None,17,"bold underline"))
LDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')

#use data picker
#pip install tkcalendar
adddate=StringVar()
EDate=Entry(F1, width=18, bg='white', fg='black',textvariable=adddate, font=(None, 14))
EDate.grid(row=0, column=1, padx=5, pady=5, sticky='w')
#............Row 1.....................

LDate=ttk.Label(F1, text='TITLE:-', font=(None,17,"bold underline"))
LDate.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Title1=StringVar()

ETitle=ttk.Entry(F1, textvariable=Title1, font=(None,15))
ETitle.grid(row=1, column=1, padx=5, pady=5, sticky='w')
#............Row 2.....................

LExpense=ttk.Label(F1, text='EXPENSES:-', font=(None,17,"bold underline"))
LExpense.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Expense=StringVar()

EExpense=ttk.Entry(F1, textvariable=Expense,font=(None,15))
EExpense.grid(row=2, column=1, padx=5, pady=2, sticky='w')
#............Row 3.....................

BF1Add=ttk.Button(F1, text='Add',command=Addexpense)
BF1Add.grid(row=3, column=1, padx=5, pady=5, sticky='w',ipadx=10,ipady=8)
clearbt=ttk.Button(F3,text='Clear',command=clear)
clearbt.grid(row=3, column=2, padx=5, pady=5, sticky='w',ipadx=10,ipady=8)
#............Tree View...................

TVList=['Date', 'Title', 'Expense']
TVExpense=ttk.Treeview(F1, column=TVList, show='headings', height=9)
for i in TVList:
    TVExpense.heading(i,text=i.title())
TVExpense.grid(row=4, column=0, padx=5, pady=5, sticky='w',columnspan=3)


#.............Tab 1 (End).....................



#.................................xxxxxxxxxxxxx..................................


Tab.pack(fill=BOTH, expand=2)
#Tab 2 (Date wise view)
#............Row 0.....................
LDate=ttk.Label(F2, text='DATE:-', font=(None,17,"bold underline"))
LDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')

#use data picker
#pip install tkcalendar
adddate2=StringVar()
EDate=Entry(F2, width=18, bg='white', fg='black',textvariable=adddate2, font=(None, 14))
EDate.grid(row=0, column=1, padx=5, pady=5, sticky='w')
#............Row 1.....................

LDate=ttk.Label(F2, text='TITLE:-', font=(None,17,"bold underline"))
LDate.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Title2=StringVar()

ETitle=ttk.Entry(F2, textvariable=Title2, font=(None,14))
ETitle.grid(row=1, column=1, padx=5, pady=5, sticky='w')
#............Row 2....................

F2VIEW=ttk.Button(F2, text='VIEW',command=View1expense)
F2VIEW.grid(row=3, column=1, padx=5, pady=5, sticky='w',ipadx=10,ipady=8)
ETitle.bind("<Return>",lambda x : View1expense())

clearbt=ttk.Button(F2,text='Clear',command=clear2)
clearbt.grid(row=3, column=2, padx=5, pady=5, sticky='w',ipadx=10,ipady=8)

btn=Button(GUI, text='EXIT', bd='5', command=GUI.destroy)
btn.pack(padx=5, pady=5,ipadx=10,ipady=8)

RVList=['DATE', 'TITLE', 'EXPENSE']
RVExpense=ttk.Treeview(F2, column=RVList, show='headings', height=9)
for i in RVList:
    RVExpense.heading(i,text=i.title())
RVExpense.grid(row=4, column=0, padx=5, pady=5, sticky='w',columnspan=3)



#.............Tab 2 (End).....................



#.............................xxxxxxxxxxxxx..................................



Tab.pack(fill=BOTH, expand=3)
#Tab 2 (Date range wise view)
#............Row 0.....................
LDate=ttk.Label(F3, text='FROM DATE:-', font=(None,17,"bold underline"))
LDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')

#use data picker
#pip install tkcalendar
adddate3=StringVar()
EDate=Entry(F3, width=18, bg='white', fg='black',textvariable=adddate3, font=(None, 14))
EDate.grid(row=0, column=1, padx=5, pady=5, sticky='w')

#............Row 1.....................
LDate=ttk.Label(F3, text='TO DATE:-', font=(None,17,"bold underline"))
LDate.grid(row=1, column=0, padx=5, pady=5, sticky='w')

#use data picker
#pip install tkcalendar
adddate4=StringVar()
EDate=Entry(F3, width=18, bg='white', fg='black',textvariable=adddate4, font=(None, 14))
EDate.grid(row=1, column=1, padx=5, pady=5, sticky='w')

#............Row 2.....................

LDate=ttk.Label(F3, text='TITLE:-', font=(None,17,"bold underline"))
LDate.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Title=StringVar()

ETitle=ttk.Entry(F3, textvariable=Title, font=(None,15))
ETitle.grid(row=2, column=1, padx=5, pady=5, sticky='w')
#............Row 3....................

F3VIEW=ttk.Button(F3, text='VIEW',command=View2expense)

F3VIEW.grid(row=3, column=1, padx=5, pady=5, sticky='w',ipadx=10,ipady=8)

clearbt=ttk.Button(F3,text='Clear',command=clear)
clearbt.grid(row=3, column=2, padx=5, pady=5, sticky='w',ipadx=10,ipady=8)

PVList=['DATE', 'TITLE', 'EXPENSE']
PVExpense=ttk.Treeview(F3, column=PVList, show='headings', height=9)
for i in PVList:
    PVExpense.heading(i,text=i.title())
PVExpense.grid(row=4, column=0, padx=5, pady=5, sticky='w',columnspan=3)

#...............................END...................................
GUI.mainloop()


# In[ ]:




