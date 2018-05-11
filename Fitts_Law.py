# -*- coding: utf-8 -*-

import tkinter as tk
import random
import numpy as np
import os

#initial parameters
ax = 375 #ax and ay are the coordinates of the upper left corner of the ellipse
ay = 225
bx = 425 #bx and by are the coordinates of the lower right corner of the ellipse
by = 275
distar = [] #array of distances
timear = []
ds = 0
count = 0

#this function modifies the size of the circle based on the thickness slider
def size(x):
    global ax
    global ay
    global bx
    global by
    canvas1.coords(circle, ax - (int(x) / 2), ay - int(x) / 2, bx + int(x) / 2, by + int(x) / 2)

#this function sets the size of the circle
def size2():
    global ax
    global ay
    global bx
    global by
    canvas1.coords(circle, ax, ay, bx, by)

#move on click
def mouse_click(event):
    global timear
    move()

#this function modifies the size and the position of the circle
def move():
    global count
    global distar
    global ax
    global ay
    global bx
    global by
    global ds

    newdist = random.randint(-200, 200)
    newsize = random.randint(-100, 10)
    
    canvas1.coords(circle, ax + newdist, ay + newdist, bx + newdist, by + newdist) #modify the coordinates of the circle depending on randC
    distar.append(abs(newdist))  #add the distance to the array
    print(distar)
    
    canvas1.tag_bind(circle, "<Button-1>", mouse_click)
     
    count += 1
    if (count == 5):
        #modify the size of the circle depending on randD
        ax = ax - newsize 
        ay = ay - newsize
        bx = bx + newsize
        by = by + newsize
        size2()
        count = 0

#function that calculate fitts law
def compute():
    global distar
    global ax
    global bx

    avgd = np.average(distar)   #average distance
    print(avgd)
    mt = np.log2((2 * avgd / (np.abs(ax - bx))))  #calculate fitts's parameter with the formula
    mtval.set("Fitts parameter(MT) = " + str(mt))  #set fitts's parameter to the new value such that it is displayed in the GUI

def help():    
    os.system('start ' + 'FittsLawHelp.html')
    
    
root = tk.Tk()
root.geometry('1100x720')  #create the window and set its title and size
root.title('Fitts\'s Law')

mtval = tk.StringVar() #variable for displaying fitts's parameter after computing

 #create the canvas and the frame
canvasFrame = tk.Frame(root)
canvasFrame.pack()
canvas1 = tk.Canvas(canvasFrame, width=800, height=500, bg='white')

# creating the slider for thickness
slider = tk.Scale(canvasFrame, from_=1, to=200, length=800, 
                  tickinterval=800, orient='horizontal', label="Thickness", command=size)
slider.pack()

#start button
startButton = tk.Button(canvasFrame, text="Start", command=move)
startButton.pack()

#compute button
computeButton = tk.Button(canvasFrame, text="Compute", command=compute)
computeButton.pack(pady=10)

#label for fitts's parameter
mtv = tk.Label(canvasFrame, textvariable=mtval)
mtv.pack()

#the circle
circle = canvas1.create_oval(ax, ay, bx, by, fill='red', outline='red')

#help button
helpButton=tk.Button(canvasFrame, command=help, text="Help", bg='blue',fg='white', width=20)
helpButton.pack()

canvas1.pack()
root.mainloop()
