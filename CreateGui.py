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
import requests
from io import BytesIO
import pandas
def write():
    global response
    with open ('response.json','w') as outfile:
        json.dump(response.json(),outfile)
    pandas.read_json('response.json').to_excel('RecallReport.xlsx')
def search(event=None):
    print('happy')
def nextResponse():
    global response
    prod = window.prodNum.get()
    if (prod<len(response.json())):
        window.prodNum.set(prod+1)
    else:
        window.prodNum.set(len(response.json()))
    productName.configure(text=response.json()[window.prodNum.get()]['Products'][0]['Name']) 
    productDesc.configure(text=response.json()[window.prodNum.get()]['Description'])
    productHazard.configure(text=response.json()[window.prodNum.get()]['Hazards'][0]['Name'])
    productContact.configure(text=response.json()[window.prodNum.get()]['ConsumerContact'])
    im = response.json()[window.prodNum.get()]['Images'][0]['URL']
    im = im.replace(' ','%20')
    u = urlopen(im)
    raw_data = u.read()
    u.close()
    tempImage = Image.open(BytesIO(raw_data))
    tempImage = tempImage.resize((290, 330), Image.ANTIALIAS)
    window.photo = ImageTk.PhotoImage(tempImage)
    #cv.configure(width=window.photo.width(), height=window.photo.height(),bg='white',image=window.photo)
    cv.configure(width=window.photo.width(), height=window.photo.height(),bg='white',image=window.photo)
def prevResponse():
    global response
    prod = window.prodNum.get()
    if (prod>=1):
        window.prodNum.set(prod-1)
    else:
        window.prodNum.set(0)
    productName.configure(text=response.json()[window.prodNum.get()]['Products'][0]['Name']) 
    productDesc.configure(text=response.json()[window.prodNum.get()]['Description'])
    productHazard.configure(text=response.json()[window.prodNum.get()]['Hazards'][0]['Name'])
    productContact.configure(text=response.json()[window.prodNum.get()]['ConsumerContact'])
    im = response.json()[window.prodNum.get()]['Images'][0]['URL']
    im = im.replace(' ','%20')
    u = urlopen(im)
    raw_data = u.read()
    u.close()
    tempImage = Image.open(BytesIO(raw_data))
    tempImage = tempImage.resize((290, 330), Image.ANTIALIAS)
    window.photo = ImageTk.PhotoImage(tempImage)
    #cv.configure(width=window.photo.width(), height=window.photo.height(),bg='white',image=window.photo)
    cv.configure(width=window.photo.width(), height=window.photo.height(),bg='white',image=window.photo)


#Initialize the window parameters

response = requests.get("https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallTitle=Lead")
window = tk.Tk()
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50)
window.columnconfigure([0, 1, 2], minsize=50)
window.title("Lead Scraper v0.3")
window.prodNum = tk.IntVar()
window.prodNum.set(0)

#Grab the intitial stuff
im = response.json()[window.prodNum.get()]['Images'][0]['URL']
im = im.replace(' ','%20')
u = urlopen(im)
raw_data = u.read()
u.close()
tempImage = Image.open(BytesIO(raw_data))
tempImage = tempImage.resize((290, 330), Image.ANTIALIAS)
window.photo = ImageTk.PhotoImage(tempImage)

#image_byt = urlopen(im).read()
#image_b64 = base64.encodebytes(image_byt)
#window.photo = tk.PhotoImage(data=image_b64)

productName = tk.Label(wraplength=500, text=response.json()[window.prodNum.get()]['Products'][0]['Name'])
productName.grid(row = 1, column=1)
productDesc = tk.Label(wraplength=500, text=response.json()[window.prodNum.get()]['Description'])
productDesc.grid(row=3, column=1, sticky="s")
productHazard = tk.Label(wraplength=500, text=response.json()[window.prodNum.get()]['Hazards'][0]['Name'])
productHazard.grid(row=4, column=1, sticky="n")

# create a white canvas
cv = tk.Label(width=window.photo.width(), height=window.photo.height(),bg='white',image=window.photo)
cv.grid(row=2,column=1)
#Link everything together
productContact = tk.Label(wraplength=500, text=response.json()[window.prodNum.get()]['ConsumerContact'])
productContact.grid(row=4, column=1)
credit = tk.Label(text='Designed by Josh Taylor')
credit.grid(row=5, column=1,sticky="s")
searchBar = tk.Entry()
searchBar.bind('<Return>', search)
searchBar.grid(row=1, column=2)

writeButton = tk.Button(wraplength=200, text = 'Write Data to Spreadsheet', width=25, height=15, bg= 'gray', fg = 'black', command = write)
writeButton.grid(row=2,column=2)
nextButton = tk.Button(text = 'Next', width = 15, height = 15, bg = 'gray', fg = 'black', command=nextResponse)
nextButton.grid(row=3,column=2)
prevButton = tk.Button(text = 'Previous', width = 15, height = 15, bg = 'gray', fg = 'black', command=prevResponse)
prevButton.grid(row=4,column=2)
window.mainloop()