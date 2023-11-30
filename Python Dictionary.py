import tkinter
from tkinter import *
from tkinter import messagebox
from PyDictionary import PyDictionary

window = Tk()
window.geometry("1000x400")
window.title("Dictionary")
window.resizable(False,False)

dictionary = PyDictionary()
a = StringVar()

def dict():
    print("dict")
    Label3.config(text = dictionary.meaning(Ent.get()))
    Label4.config(text = dictionary.synonym(Ent.get()))
    Label5.config(text = dictionary.antonym(Ent.get()))

def Type_Word(event):
    ab = a.get()
    if ab =="":
        messagebox.showerror("Error", "One of the input feild(s) are empty.")
    else:
        dict()

window.bind('<Return>',Type_Word)

Label1 = Label(window,text = "Dictionary", font = ("Arial",26), relief = "solid", width = 10)
Label1.place(x = 100, y = 20)

a = StringVar()
Label2 = Label(window, text = "Type Word :  ", font = ("Arial",15))
Label2.place(x = 50, y = 100)
Ent = Entry(window,width = 18,font = (15),textvariable=a)
Ent.place(x = 170, y = 102)

Label3 = Label(window, text = "",font = (12) )
Label32 = Label(window, text = "Meaning : ",font = (12) )
Label3.place(x = 160, y = 150)
Label32.place(x = 80, y = 150)

Label4 = Label(window, text = "",font = (12) )
Label42 = Label(window, text = " Synonym : ",font = (12) )
Label4.place(x = 160, y = 200)
Label42.place(x = 70, y = 200)

Label5a = Label(window, text = "Antonym :",font = (12) )
Label5 = Label(window, text = "",font = (12) )
Label5.place(x = 160, y = 250)
Label5a.place(x = 80, y = 250)


window.mainloop()
