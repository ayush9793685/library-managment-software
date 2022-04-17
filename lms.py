from logging import root
import tkinter as tk
from tkinter.constants import RADIOBUTTON

frame = tk.Tk()
frame.title("LMS")
frame.geometry('1275x700')
bg = tk.PhotoImage(file = "Untitled.png")
label3 = tk.Label( frame, image = bg)
label3.place(x = 0, y = 0,relwidth=1,relheight=1)


import mysql.connector as sqlctr
import sys
from datetime import date, datetime
mycon = sqlctr.connect(user='Ayush', password='Ayush9793@',
                              host='127.0.0.1',
                               database='lib')


cursor = mycon.cursor()

def command(st):
    cursor.execute(st)


def fetch():
    data = cursor.fetchall()
    a=20
    for i in data:
        a=a+(len(i)*3)
        z=20+a
        for j in i:
            c=i.index(j)
            b=[0,40,110,225,335,495,580]
            c=b[c]
            l = tk.Label(text = j)
            l.config(font =("Courier", 10))
            l.pack()
            l.place(x=500+(c),y=z)
    

def fetch2():
    data = cursor.fetchall()
    a=20
    for i in data:
        a=a+(len(i)*3)
        z=20+a
        print(i)
        for j in i:
            c=i.index(j)
            b=[0,40,140,260,320,365,430]
            c=b[c]
            l = tk.Label(text = j)
            l.config(font =("Courier", 10))
            l.pack()
            l.place(x=500+(c),y=350+z)
        


def all_data(tname):
    li = []
    st = 'desc '+tname
    command(st)
    data = cursor.fetchall()
    for i in data:
        li.append(i[0])
    st = 'select * from '+tname
    command(st)
    if tname=='book':
        for j in li:
            a=li.index(j)
            b=[0,40,110,225,335,495,580]
            a=b[a]
            l1 = tk.Label(text = j)
            l1.config(font =("Courier", 10))
            l1.pack()
            l1.place(x=500+(a),y=20)   
    
        fetch()
    elif tname=='students':
        for j in li:
            a=li.index(j)
            b=[0,40,140,260,320,365,430]
            a=b[a]
            l1 = tk.Label(text = j)
            l1.config(font =("Courier", 10))
            l1.pack()
            l1.place(x=500+(a),y=350)    
        fetch2()


def show_book():
    all_data('book')
    

printButton = tk.Button(frame,bg=("mintcream"),text = "Show books data",command =show_book)
printButton.pack()
printButton.place(x=20,y=55)


def delete(tname):
    if tname=="book":
        l = tk.Label(frame,text = "delete through :-")
        l.config(font =("Courier", 14))
        l.pack()
        l.place(x=30,y=280)
        printButton4 = tk.Button(frame,text = "book id",command =bookid)
        printButton4.pack()
        printButton4.place(x=70,y=310)
        printButton5 = tk.Button(frame,text = "book name",command =bookname)
        printButton5.pack()
        printButton5.place(x=125,y=310)
        printButton6 = tk.Button(frame,text = "sno",command =sno)
        printButton6.pack()
        printButton6.place(x=200,y=310)
    elif tname=="students":
        l = tk.Label(frame,text = "delete through :-")
        l.config(font =("Courier", 14))
        l.pack()
        l.place(x=30,y=380)
        printButton4 = tk.Button(frame,text = "student id",command =studentid)
        printButton4.pack()
        printButton4.place(x=70,y=410)
        printButton5 = tk.Button(frame,text = "student name",command =studentname)
        printButton5.pack()
        printButton5.place(x=140,y=410)
        printButton6 = tk.Button(frame,text = "sno",command =srno)
        printButton6.pack()
        printButton6.place(x=230,y=410)


def bookid():
    l = tk.Label(frame,text = "enter id")
    l.config(font =("Courier", 13))
    l.pack()
    l.place(x=40,y=340)
    inputtxt3 = tk.Text(frame,height = 2,width = 20)
    inputtxt3.pack()
    inputtxt3.place(x=140,y=340)
    def printInput():
        inp2 = inputtxt3.get(1.0, "end-1c")
        st1="delete from book where book_id={}".format(inp2)
        command(st1)
        mycon.commit()

        l = tk.Label(frame,text = "data har been deleted ")
        l.config(font =("Courier", 14))
        l.pack()
        l.place(x=30,y=480)
        
        
    printButton7 = tk.Button(frame,bg=("mintcream"),text = "confirm",command =printInput)
    printButton7.pack()
    printButton7.place(x=305,y=340)
    
    
def bookname():
    l = tk.Label(frame,text = "enter name")
    l.config(font =("Courier", 13))
    l.pack()
    l.place(x=20,y=340)
    inputtxt3 = tk.Text(frame,height = 2,width = 20)
    inputtxt3.pack()
    inputtxt3.place(x=140,y=340)
    def printInput():
        inp2 = inputtxt3.get(1.0, "end-1c")
        st1="delete from book where book_name='{}'".format(inp2)
        command(st1)
        mycon.commit()
        
        l = tk.Label(frame,text = "data har been deleted ")
        l.config(font =("Courier", 14))
        l.pack()
        l.place(x=30,y=480)

    printButton7 = tk.Button(frame,text = "confirm",command =printInput)
    printButton7.pack()
    printButton7.place(x=305,y=340)

def sno():
    l = tk.Label(frame,text = "enter sno")
    l.config(font =("Courier", 13))
    l.pack()
    l.place(x=20,y=340)
    inputtxt3 = tk.Text(frame,height = 2,width = 20)
    inputtxt3.pack()
    inputtxt3.place(x=140,y=340)
    def printInput():
        inp2 = inputtxt3.get(1.0, "end-1c")
        st1="delete from book where sno='{}'".format(inp2)
        command(st1)
        mycon.commit()
        
        l = tk.Label(frame,text = "data har been deleted ")
        l.config(font =("Courier", 14))
        l.pack()
        l.place(x=30,y=480)

    printButton7 = tk.Button(frame,text = "confirm",command =printInput)
    printButton7.pack()
    printButton7.place(x=305,y=340)

def studentid():
    l = tk.Label(frame,text = "enter id")
    l.config(font =("Courier", 13))
    l.pack()
    l.place(x=40,y=440)
    inputtxt3 = tk.Text(frame,height = 2,width = 20)
    inputtxt3.pack()
    inputtxt3.place(x=140,y=440)
    def printInput():
        inp2 = inputtxt3.get(1.0, "end-1c")
        st1="delete from students where student_id={}".format(inp2)
        command(st1)
        mycon.commit()
        
        
        l = tk.Label(frame,text = "data har been deleted ")
        l.config(font =("Courier", 14))
        l.pack()
        l.place(x=30,y=480)

    printButton7 = tk.Button(frame,text = "confirm",command =printInput)
    printButton7.pack()
    printButton7.place(x=305,y=440)
    
    
def studentname():
    l = tk.Label(frame,text = "enter name")
    l.config(font =("Courier", 13))
    l.pack()
    l.place(x=20,y=440)
    inputtxt3 = tk.Text(frame,height = 2,width = 20)
    inputtxt3.pack()
    inputtxt3.place(x=140,y=440)
    def printInput():
        inp2 = inputtxt3.get(1.0, "end-1c")
        st1="delete from students where student_name='{}'".format(inp2)
        command(st1)
        mycon.commit()
        
        l = tk.Label(frame,text = "data har been deleted ")
        l.config(font =("Courier", 14))
        l.pack()
        l.place(x=30,y=480)
    printButton7 = tk.Button(frame,text = "confirm",command =printInput)
    printButton7.pack()
    printButton7.place(x=305,y=440)

def srno():
    l = tk.Label(frame,text = "enter sno")
    l.config(font =("Courier", 13))
    l.pack()
    l.place(x=20,y=440)
    inputtxt3 = tk.Text(frame,height = 2,width = 20)
    inputtxt3.pack()
    inputtxt3.place(x=140,y=440)
    def printInput():
        inp2 = inputtxt3.get(1.0, "end-1c")
        st1="delete from students where sno='{}'".format(inp2)
        command(st1)
        mycon.commit()
        
        l = tk.Label(frame,text = "data har been deleted ")
        l.config(font =("Courier", 14))
        l.pack()
        l.place(x=30,y=480)

    printButton7 = tk.Button(frame,text = "confirm",command =printInput)
    printButton7.pack()
    printButton7.place(x=305,y=440)


def delete_but():
    delete('book')           

#delete()
printButton3 = tk.Button(frame,bg=("mintcream"),width=13,text = "Delete book data ",command =delete_but)
printButton3.pack()
printButton3.place(x=20,y=170)

def deletebut2():
    delete('students')
stu_but3 = tk.Button(frame,bg=("mintcream"),width=14,text = "Delete student data ",command =deletebut2)
stu_but3.pack()
stu_but3.place(x=150,y=170)


def sampletry():
    sample('book')
    
printButton2 = tk.Button(frame,bg=("mintcream"),width=13,text = "Insert book data ",command =sampletry)
printButton2.pack()
printButton2.place(x=20,y=110)






def sample(tname):
    frame2= tk.Tk()
    frame2.title("insert")
    frame2.geometry('300x300')
    frame2.config(bg="light blue")
    licol=[]
    command('desc '+tname)
    data=cursor.fetchall()
    for i in data:
        licol.append(i[0])

    l = tk.Label(frame2,text = licol[1])
    l.config(font =("Courier", 10))
    l.pack()
    l.place(x=10,y=10)
    textbox1 = tk.Text(frame2,height = 1,width = 20)

    l = tk.Label(frame2,text = licol[2])
    l.config(font =("Courier", 10))
    l.pack()
    l.place(x=10,y=40)
    textbox2 = tk.Text(frame2,height = 1,width = 20)
        

    l = tk.Label(frame2,text = licol[3])
    l.config(font =("Courier", 10))
    l.pack()
    l.place(x=10,y=70)
    textbox3 = tk.Text(frame2,height = 1,width = 20)
        

    l = tk.Label(frame2,text = licol[4])
    l.config(font =("Courier", 10))
    l.pack()
    l.place(x=10,y=100)
    textbox4 = tk.Text(frame2,height = 1,width = 20)

        
    l = tk.Label(frame2,text = licol[5])
    l.config(font =("Courier", 10))
    l.pack()
    l.place(x=10,y=130)
    textbox5 = tk.Text(frame2,height = 1,width = 20)

        
    l = tk.Label(frame2,text = licol[6])
    l.config(font =("Courier", 10))
    l.pack()
    l.place(x=10,y=160)
    textbox6 = tk.Text(frame2,height = 1,width = 20)

    textbox1.pack()
    textbox1.place(x=120,y=10)

    textbox2.pack()
    textbox2.place(x=120,y=40)

    textbox3.pack()
    textbox3.place(x=120,y=70)

    textbox4.pack()
    textbox4.place(x=120,y=100)

    textbox5.pack()
    textbox5.place(x=120,y=130)

    textbox6.pack()
    textbox6.place(x=120,y=160)

    def adding():
        insert('book')
    
    def adding_st():
        insert('students')

    if tname=='book':
        addbutton=tk.Button(frame2,height=2,width=20,text = "Add data",command = adding)
        addbutton.pack()
        addbutton.place(x=70,y=200)
    elif tname== 'students':
        addbutton=tk.Button(frame2,height=2,width=20,text = "Add data",command = adding_st)
        addbutton.pack()
        addbutton.place(x=70,y=200)
        
    
    def insert(tname):
        print(tname)
        l1=[]
        licol=[]
        command('desc '+tname)
        data=cursor.fetchall()
        for i in data:
            licol.append(i[0])
        command('select max(sno) from '+tname)
        dta=cursor.fetchall()
        for j in dta:
            l1.append(j[0]+1)
        inp1=textbox1.get(1.0, "end-1c")
        l1.append(inp1)

        inp2=textbox2.get(1.0, "end-1c")
        l1.append(inp2)

        inp3=textbox3.get(1.0, "end-1c")
        l1.append(inp3)

        inp4=textbox4.get(1.0, "end-1c")
        l1.append(inp4)

        inp5=textbox5.get(1.0, "end-1c")
        l1.append(inp5)

        inp6=textbox6.get(1.0, "end-1c")
        l1.append(inp6)
        
        a=tuple(l1)
        print(a)
        if tname == "book":
            st1 = "INSERT INTO book VALUES {}".format(a)
            command(st1)
            mycon.commit()

        elif tname=='students':
            st1 = "INSERT INTO students VALUES {}".format(a)
            command(st1)
            mycon.commit()
                

#student data

    
def stu_data():
    all_data('students')

stbut1 = tk.Button(frame,bg=("mintcream"),text = "Show student data",command =stu_data)
stbut1.pack()
stbut1.place(x=150,y=55)

def ins_data():
    sample('students')

stbut2 = tk.Button(frame,bg=("mintcream"),text = "insert student data",command =ins_data)
stbut2.pack()
stbut2.place(x=150,y=110)

def issuecreate():
    frame2= tk.Tk()
    frame2.title("issue ")
    frame2.geometry('300x300')
    frame2.config(bg="light blue")
    l1 = tk.Label(frame2,height=2,width=13,text = "book id")
    l1.config(font =("Courier", 10))
    l1.pack()
    l1.place(x=10,y=10)
    textbox1 = tk.Text(frame2,height = 2,width = 17)
    l2 = tk.Label(frame2,height=2,width=13,text = "student id")
    l2.config(font =("Courier", 10))
    l2.pack()
    l2.place(x=10,y=70)
    textbox2 = tk.Text(frame2,height = 2,width = 17)
    l3 = tk.Label(frame2,text = "date_of_issue\nin (y-m-d)\nformat")
    l3.config(font =("Courier", 10))
    l3.pack()
    l3.place(x=10,y=130)
    textbox3 = tk.Text(frame2,height = 2,width = 17)
    

    textbox1.pack()
    textbox1.place(x=140,y=10)

    textbox2.pack()
    textbox2.place(x=140,y=70)

    textbox3.pack()
    textbox3.place(x=140,y=130)

    def adding():
        add_data()
    addbutton=tk.Button(frame2,height=2,width=20,text = "issue book",command = adding)
    addbutton.pack()
    addbutton.place(x=70,y=200)

    def add_data():
        l1=[]
        inp1=textbox1.get(1.0, "end-1c")
        l1.append(inp1)

        inp2=textbox2.get(1.0, "end-1c")
        l1.append(inp2)

        inp3=textbox3.get(1.0, "end-1c")
        l1.append(inp3)
        dt_ret=1111-1-1
        l1.append(dt_ret)
        l1=tuple(l1)
        st1='insert into issue values {}'.format(l1)
        command(st1)
        mycon.commit()


        





def issue_data():
    issuecreate()
issuebut = tk.Button(frame,bg=("mintcream"),width=13,text = "issue book",command =issue_data)
issuebut.pack()
issuebut.place(x=20,y=220)



def returndata():
    frame2= tk.Tk()
    frame2.title("return ")
    frame2.geometry('300x300')
    frame2.config(bg="light blue")

    l1 = tk.Label(frame2,height=2,width=13,text = "book id")
    l1.config(font =("Courier", 10))
    l1.pack()
    l1.place(x=10,y=10)
    textbox1 = tk.Text(frame2,height = 2,width = 17)
    l2 = tk.Label(frame2,height=2,width=13,text = "student id")
    l2.config(font =("Courier", 10))
    l2.pack()
    l2.place(x=10,y=70)
    textbox2 = tk.Text(frame2,height = 2,width = 17)

    textbox1.pack()
    textbox1.place(x=140,y=10)

    textbox2.pack()
    textbox2.place(x=140,y=70)

    def scanning():
        l1=[]
        inp1=textbox1.get(1.0, "end-1c")
        inp1=int(inp1)
        l1.append(inp1)

        inp2=textbox2.get(1.0, "end-1c")
        inp2=int(inp2)
        l1.append(inp2)

        A1=tuple(l1)

        st0 = 'select bookid,studentid  from issue' 
        command(st0)
        data=cursor.fetchall()
        
        l2=[]
        for i in data:
            l2.append(i)
        

        a=0
        for j in l2:
            if j==A1:
                a=a+1
                l3 = tk.Label(frame2,text = "date_of_return\nin (y-m-d)\nformat")
                l3.config(font =("Courier", 10))
                l3.pack()
                l3.place(x=10,y=170)
                textbox3 = tk.Text(frame2,height = 2,width = 17)
                textbox3.pack()
                textbox3.place(x=140,y=170)
                def ret_book():
                    from datetime import datetime
                    inp3=textbox3.get(1.0, "end-1c")
                    inp4="'{}'".format(inp3)
                    
                    st1='update issue set date_of_return={}'.format(inp4)+' where bookid={}'.format(inp1)
                    command(st1)
                    mycon.commit()
                
                    st2='select date_of_issue,date_of_return  from issue where bookid={}'.format(inp1)
                    date_format = "%Y-%m-%d"
                    command(st2)
                    data=cursor.fetchall()
                    a=data[0]
                    b=a[0]
                    b='{}'.format(b)
                    c=a[1]
                    c='{}'.format(c)
                    
                    
                    d1= datetime.strptime(b,date_format)
                    d2= datetime.strptime(c, date_format)
                    diff= d2-d1
                    difference=diff.days
                    if difference>=10:
                        fine=(difference-10)*2
                        st3='UPDATE students SET fine=+{}'.format(fine)+' WHERE studentid={}'.format(inp2)
                        command(st3)
                        mycon.commit()

                addbutton2=tk.Button(frame2,height=2,width=20,text = "return book",command = ret_book)
                addbutton2.pack()
                addbutton2.place(x=70,y=240)
            else:
                a=a+0
        if a==0:
            l1 = tk.Label(frame2,text = "provided input is wrong")
            l1.config(font =("Courier", 10))
            l1.pack()
            l1.place(x=50,y=200)
    addbutton=tk.Button(frame2,height=2,width=20,text = "check data",command = scanning)
    addbutton.pack()
    addbutton.place(x=70,y=120)

def return_data():
    returndata()

issuebut = tk.Button(frame,bg=("mintcream"),width=14,text = "return book",command =return_data)
issuebut.pack()
issuebut.place(x=150,y=220)






frame.mainloop()






