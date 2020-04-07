# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd

isBlocked=False #this variable dictates whether or not popup windows are allowed to appear

def combine_funcs(*funcs):  #this function is used for calling 2 functions with the same button on line 47
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def blockPopup(): #blocks popup windows from appearing
    global isBlocked
    isBlocked=True

def enablePopup(): #enables popup windows
    global isBlocked
    isBlocked=False
    
def popup(i): 
    if(isBlocked): #if the popup is blocked, send an error message to the console
        print("Can't open any more popup windows")
        exit
    else:
        popup = tk.Toplevel() #create the window, set its title and geometry
        popup.title(names[i])
        popup.geometry("%dx%d%+d%+d" % (550, 520, 550, 50)) 
#labels representing information about the selected county        
        label1 = tk.Label(popup, text="County: "+names[i])
        label1.pack()
        if capitals[i]!="H":
            label2 = tk.Label(popup, text="Capital: "+capitals[i])
            label2.pack()
        label3 = tk.Label(popup, text="Population: "+str(population[i]))
        label3.pack()
        label4 = tk.Label(popup, text="Surface Area: "+str(area[i]) + " km²")
        label4.pack()
#create the canvas and the image        
        canvas = tk.Canvas(popup,width=550, height=400)
        canvas.pack()
        canvas.create_image(280, 220, image=Images[i])
        canvas.update()
#create the close button        
        B1 = tk.Button(popup, text="Close", command=combine_funcs(popup.destroy, enablePopup))
        B1.pack()
        blockPopup()
        popup.protocol("WM_DELETE_WINDOW", combine_funcs(popup.destroy, enablePopup))
        popup.mainloop()

#create the main window, set its title and geometry    
root=tk.Tk() 
root.title('Interactive Map')
root.geometry("%dx%d%+d%+d" % (550, 450, 150, 50))

#read the data from the countries.data file
data = pd.read_csv('counties.data',header=None, delim_whitespace=True)
names=data[0]
capitals=data[1]
posX=data[2]
posY=data[3]
area=data[4]
population=data[5]

#create the main canvas
canvas1 = tk.Canvas(root,width=550, height=400)
canvas1.pack()
canvas1.create_text(200,20, text="Click the county names to reveal facts about each county!")

img = Image.open("romania.jpg")
ph=ImageTk.PhotoImage(img)

#iterate through the data and the images folder to create the data for popup windows
#also create a button for each county
Images=[]
Buttons=[]
for i in range(len(posX)):
    j=i
    button = tk.Button(canvas1, text = names[i], command=lambda x=i: popup(x))
    button_window = canvas1.create_window(posX[i],posY[i], window=button)
    Buttons.append(button)
    img = Image.open(str(i+1)+".jpg")
    Images.append(ImageTk.PhotoImage(img))

#create the image on the main canvas    
canvas1.create_image(280, 220, image=ph)
canvas1.update()

#create the close button 
closeButton = tk.Button(root, text="Close", command=root.destroy)
closeButton.pack()
        
root.mainloop()