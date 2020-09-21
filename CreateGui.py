# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:21:55 2020
This file creates the GUI for the user to interact with lead related product recalls
@author: josh
"""
import json
from urllib.request import *
import tkinter as tk
from PIL import Image, ImageTk
import io
import base64

window = tk.Tk()
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50)
window.columnconfigure([0, 1, 2], minsize=50)
window.title("Lead Scraper v0.3")
image_byt = urlopen(im).read()
image_b64 = base64.encodebytes(image_byt)
photo = tk.PhotoImage(data=image_b64)

productName = tk.Label(wraplength=500, text=response.json()[0]['Products'][0]['Name'])
productName.grid(row = 1, column=1)
productDesc = tk.Label(wraplength=500, text=response.json()[0]['Description'])
productDesc.grid(row=3, column=1, sticky="s")
productHazard = tk.Label(wraplength=500, text=response.json()[0]['Hazards'][0]['Name'])
productHazard.grid(row=4, column=1, sticky="n")
# create a white canvas
cv = tk.Canvas(width=photo.width(), height=photo.height(), bg='white')
cv.grid(row=2,column=1)
cv.create_image(0, 0, image=photo, anchor='nw')
#Link everything together
productContact = tk.Label(wraplength=500, text=response.json()[0]['ConsumerContact'])
productContact.grid(row=4, column=1)
credit = tk.Label(text='Designed by Josh Taylor')
credit.grid(row=5, column=1,sticky="s")
searchBar = tk.Entry()
searchBar.grid(row=1, column=2)

nextButton = tk.Button(text = 'Next', width = 15, height = 15, bg = 'gray', fg = 'black')
nextButton.grid(row=3,column=2)
prevButton = tk.Button(text = 'Previous', width = 15, height = 15, bg = 'gray', fg = 'black')
prevButton.grid(row=4,column=2)