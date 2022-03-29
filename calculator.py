
from tkinter import *
import tkinter.messagebox as tmsg
def click(event):
    text=event.widget.cget('text')
    if text=='=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(scvalue.get())
        scvalue.set(value)
        entry.update()
    elif text=='C':
        scvalue.set('')
        entry.update()
    else:
        scvalue.set(scvalue.get()+ text)
        entry.update()
def about():
    msg=tmsg.showinfo('About','Made With Smart Work using Python Tkinter Library')

root=Tk()
root.title('Avira Calculator')
root.geometry('644x900')
myMenu=Menu(root)
myMenu.add_command(label='About',command=about)
root.config(menu=myMenu)
scvalue=StringVar()
scvalue.set('')
entry=Entry(textvariable=scvalue,font='lucida 40 bold')
entry.pack(fill=X)


f1=Frame(root,bg='grey')
f1.pack()
# 987 num button
for i in range(9,6,-1):
    b=Button(f1,text=f'{i}',font='lucida 20 bold',padx=28,pady=22)
    b.bind('<Button-1>',click)
    b.pack(side=LEFT,padx=10,pady=10)
b=Button(f1,text='+',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=12,pady=12)


f2=Frame(root,bg='grey')
f2.pack()
# 654 num button
for i in range(6,3,-1):
    b=Button(f2,text=f'{i}',font='lucida 20 bold',padx=28,pady=22)
    b.bind('<Button-1>',click)
    b.pack(side=LEFT,padx=12,pady=12)
b=Button(f2,text='-',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=9,pady=5)


f3=Frame(root,bg='grey')
f3.pack()
# 321 num button
for i in range(3,0,-1):
    b=Button(f3,text=f'{i}',font='lucida 20 bold',padx=28,pady=22)
    b.bind('<Button-1>',click)
    b.pack(side=LEFT,padx=12,pady=12)

b=Button(f3,text='*',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=9,pady=5)

f4=Frame(root,bg='grey')
f4.pack()
b=Button(f4,text='/',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f4,text='0',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f4,text='%',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f4,text='C',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=10,pady=10)

f5=Frame(root,bg='grey')
f5.pack()
b=Button(f5,text='=',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f5,text='.',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f5,text='00',font='lucida 20 bold',padx=28,pady=22)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=10,pady=10)



root.mainloop()