from tkinter import*
def sum(event):
    a=int(ent.get())
    b=int(ent1.get())
    c=a+b
    lab1['text']=str(c)
def minus(event):
    a=int(ent.get())
    b=int(ent1.get())
    c=a-b
    lab1['text']=str(c)
def umn(event):
    a=int(ent.get())
    b=int(ent1.get())
    c=a*b
    lab1['text']=str(c)
def Del(event):
    a=int(ent.get())
    b=int(ent1.get())
    if(b==0):
        lab1['text']='ошибка'
    else:
        c=a/b
        lab1['text']=str(c)
root=Tk()
ent=Entry(width=15,fg="black",bg="#EE82EE")
ent1=Entry(width=15,fg="black",bg="#EE82EE")
lab1=Label(width=20,fg="black",bg="#EE82EE", text="")
but=Button(width=20,text="-")
but1=Button(width=20,text="+")
but2=Button(width=20,text="*")
but3=Button(width=20,text="/")
but1.bind('<Button-1>', sum)
but.bind('<Button-1>', minus)
but2.bind('<Button-1>', umn)
but3.bind('<Button-1>', Del)
ent.pack()
ent1.pack()
but.pack()
but1.pack()
but2.pack()
but3.pack()
lab1.pack()
root.mainloop()

