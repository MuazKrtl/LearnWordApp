import tkinter as tk
import random
from collections import defaultdict
from secrets import choice  
from time import time,sleep
from tkinter import Tk, Button, Frame, Entry, END,ttk,Text,Toplevel,Listbox,messagebox,Scrollbar,filedialog,Label,X,StringVar,Label,TOP,Tk,Label,Button,Entry,Text,X,TOP,Y,ANCHOR,CENTER,SW,NW,S,N,W,E,EW,StringVar
def engSekmeAc():
    window.destroy()
    engSekme = Tk()
    engSekme.title("Dictionary")
    engSekme.geometry("720x480")
    engSekme.configure(background="lightgreen")
    anlamlar1 = defaultdict(list)
    all_words_in_file1 = defaultdict(list)
    with open('anlamlisteng.txt', 'r') as f:
        anlamlar1 = [line.strip() for line in f]
    def rastdosya():
        rastdosya = "kelimelisteng.txt"
        return rastdosya
    def rastkel(file_name):
        global all_words_in_file1
        with open("kelimelisteng.txt", 'r') as f:
            all_words_in_file1 = [line.strip() for line in f]
        global i 
        i = random.randrange(len(all_words_in_file1))
        random_word = all_words_in_file1[i]
        return random_word
    def keldeis():
        lbl['text'] = rastkel(rastdosya()) 
    if __name__ == '__main__':
        lbl = tk.Label(engSekme,font=("TimesNewRoman",40))
        lbl.configure(background="lightgreen")
        btn = tk.Button(engSekme, text="Show Word!", command=keldeis,font=("TimesNewRoman",12),height=5)
        btn.pack(side="bottom",fill=X)
    def printtext():
        global cevap
        cevap = e.get()
        if cevap == anlamlar1[i] :
            e.delete(0,"end")
            str_var.set("Correct!")
        else:
            str_var.set(f"Mistake! Answer was {anlamlar1[i].upper()}")
            e.delete(0,"end")
    str_var = StringVar()
    str_label = Label(engSekme,textvariable=str_var,height=3,font=("TimesNewRoman",30),relief="flat",bg="lightgreen",fg="red")
    e = Entry(engSekme,font=("TimesNewRoman",40))
    e.pack(side="bottom")
    str_label.pack(side="bottom")
    e.focus_set()
    lbl.pack(side="bottom")
    b = Button(engSekme,text='Check It!',command=printtext,font=("TimesNewRoman",10),height=5)
    b.pack(side="top",fill=X)  
    engSekme.bind('<Return>', lambda event=None: b.invoke())
    engSekme.bind('<Shift_L>', lambda event=None: btn.invoke())
    engSekme.mainloop()
def spaSekmeAc():
    window.destroy()
    spaSekme = Tk()
    spaSekme.title("Diccionario")
    spaSekme.geometry("720x480")
    spaSekme.configure(background="lightgreen")
    with open('anlamlistspa.txt', 'r') as f:
        anlamlar = [line.strip() for line in f]
    def rastdosya():
        rastdosya = "kelimelistspa.txt"
        return rastdosya
    def rastkel(file_name):
        global all_words_in_file
        with open("kelimelistspa.txt", 'r') as f:
            all_words_in_file = [line.strip() for line in f]
        global i 
        i = random.randrange(len(all_words_in_file))
        random_word = all_words_in_file[i]
        return random_word
    def keldeis():
        lbl['text'] = rastkel(rastdosya()) 
    if __name__ == '__main__':
        lbl = tk.Label(spaSekme,font=("TimesNewRoman",40))
        lbl.configure(background="lightgreen")
        btn = tk.Button(spaSekme, text="Mostrar Palabra!", command=keldeis,font=("TimesNewRoman",12),height=5)
        btn.pack(side="bottom",fill=X)
    def printtext():
        global cevap
        cevap = e.get()
        if cevap == anlamlar[i] :
            e.delete(0,"end")
            str_var.set("Cierto!")
        else:
            str_var.set(f"Falso! La respuesta fue {anlamlar[i].upper()}")
            e.delete(0,"end")
    str_var = StringVar()
    str_label = Label(spaSekme,textvariable=str_var,height=3,font=("TimesNewRoman",30),relief="flat",bg="lightgreen",fg="red")
    e = Entry(spaSekme,font=("TimesNewRoman",40))
    e.pack(side="bottom")
    str_label.pack(side="bottom")
    e.focus_set()
    lbl.pack(side="bottom")
    b = Button(spaSekme,text='Revisalo!',command=printtext,font=("TimesNewRoman",10),height=5)
    b.pack(side="top",fill=X)  
    spaSekme.bind('<Return>', lambda event=None: b.invoke())
    spaSekme.bind('<Shift_L>', lambda event=None: btn.invoke())
    spaSekme.mainloop()
window = Tk()
window.title("AskYourself!-Pregúntese!")
window.geometry("720x480")
window.configure(background="lightgreen")
text = Text(window, width=18, height=1,font=("TimesNewRoman", 32),relief="flat")
text.configure(background="lightgreen",foreground="red")
text.insert('5.0', '  English or Spanish?')
text.pack(side="top")
buton1 = Button(window,text ="English",bd=3,command=engSekmeAc,width=50,height=20)
buton1.pack(side="right",fill='both', expand=True)
buton2 = Button(window,text ="Spanish",bd=3,command=spaSekmeAc,width=50,height=20)
buton2.pack(side="left",fill='both', expand=True)

window.mainloop()

