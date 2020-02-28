# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:48:18 2020

@author: Muhammad Fakhar
"""

from tkinter import messagebox
from pyzbar.pyzbar import decode
import tkinter as tk
from PIL import Image
from tkinter import filedialog

def onclick():
    r.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
    return r.filename


r = tk.Tk();

r.title('demo Code')
btn1 = tk.Button(r,text='use me',command=onclick)
btn1.pack()
r.mainloop()



d = decode(Image.open(r.filename));
messagebox.showinfo('result',d[0].data.decode('ascii'))


