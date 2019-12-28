import os
from tkinter import *
root = Tk()
root.geometry('500x150+400+100')
def runit():
    os.startfile('link.bat')
def downloadtv():
    with open('link.bat','w') as down_load:
        down_load.write(f'youtube-dl {link.get()}')
        down_load.close()
    runit()
f = Frame(root)
f.grid()
Label(f,text='###YouTube Video Downloader###',font=15,padx=6).pack()
Label(f,text='').pack()
f1 = Frame(root)
f1.grid()
Label(f1,text='  Enter the link here : ',font=5).grid(row=1)
link=StringVar()
Entry(f1,font=5,textvariable=link).grid(row=1,column=1,pady=5,padx=10)
Button(f1,text='Download',padx=50,relief=RAISED,font=10,borderwidth=5,command=downloadtv).grid(column=1,pady=5)
root.mainloop()

