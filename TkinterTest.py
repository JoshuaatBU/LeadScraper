# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:16:49 2020

@author: josh
"""

import tkinter as tk
import tkinter.ttk as ttk
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

class Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))
        
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.window.title('Lead Scraper')
        
        #Create the checkmarker
        chk_state = tk.IntVar(value=-1)
        chk_state.set(True)
        chk = ttk.Checkbutton(self.window, text='Choose', var=chk_state, command=self.check_test)
        chk.grid(column=0, row=0)
        
        lbl=Label(self.window, text='Welcome to Lead Scraper. Hit the check mark', fg='black', font=("Helvetica", 16))
        lbl.place(x=60, y=50)
        
        #Run the window
        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
    def check_test(self):
        print("state: {}".format(chk_state.get()))

#window = tk.Tk()
#window.attributes('-fullscreen',True)
#window.title('Lead Scraper')
##chk_state.set(True) #set check state
#lbl=Label(window, text='Welcome to Lead Scraper. Hit the check mark', fg='red', font=("Helvetica", 16))
#lbl.place(x=60, y=50)
#window.mainloop()
#im = response.json()[0]['Images'][0]['URL']

#chk_state = tk.IntVar(value=-1)
#chk = ttk.Checkbutton(window, text='Choose', var=chk_state, command=check_test)
#chk.grid(column=0, row=0)
