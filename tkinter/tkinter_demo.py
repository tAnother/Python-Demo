#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:54:23 2021

@author: hangjieji
"""

import tkinter as Tk # Tkinter for Python2

root = Tk.Tk()

w = Tk.Canvas(master=root,
              width = 400,
              height=600)
w.pack()

w.create_rectangle(100,200,300,500,
                   fill = 'blue')
w.create_oval(200,250,250,300,
                   fill = 'red')

def callback(event):
    print("clicked!")
    print(event.x, event.y)

#w.bind("<Button-1>", callback)
    
def callback2(event):
    print("clicked!")
    print(event.x, event.y)
    w.create_oval(event.x, event.y,
                  event.x + 20, event.y+20,
                   fill = 'red')

w.bind("<Button-1>", callback2) # mouse click

def callback3():
    print("hello, you've clicked the button.")
b = Tk.Button(master=root,text="Click me!",
              command=callback3)
b.pack()

root.mainloop()