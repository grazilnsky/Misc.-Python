# -*- coding: utf-8 -*-

import tkinter as tk
import os

# The following functions change the intensity of the colored blocks
# (from black at 0 to white at 255) 
# by taking shade of grey based on the position of the slider. 
# The value for the slider is from 0 to 255. The value is converted to hexadecimal to generate the colors.


def intensity1(y): #for the left block
    if int(y) < 16:
        color = '#' + (('0' + (str(hex(int(y)))[2:])) * 3)
        canvas1.itemconfig(block1, fill=color)
    else:
        color = '#' + (str(hex(int(y)))[2:] * 3)
        canvas1.itemconfig(block1, fill=color)

def intensity2(y): #for the center block
    if int(y) < 16:
        color = '#' + (('0' + (str(hex(int(y)))[2:])) * 3)
        canvas1.itemconfig(block2, fill=color)
    else:
        color = '#' + (str(hex(int(y)))[2:] * 3)
        canvas1.itemconfig(block2, fill=color)
        
def intensity3(y): #for the right block
    if int(y) < 16:
        color = '#' + (('0' + (str(hex(int(y)))[2:])) * 3)
        canvas1.itemconfig(block3, fill=color)
    else:
        color = '#' + (str(hex(int(y)))[2:] * 3)
        canvas1.itemconfig(block3, fill=color)


def help():    
    os.system('start ' + 'MachIllusionHelp.html')

root = tk.Tk()  #create the window and set its title and size
root.geometry('1100x600')  
root.title('Mach\'s Illusion')

canvasFrame = tk.Frame(root)  # creating a frame in root
canvasFrame.pack() 

canvas1 = tk.Canvas(canvasFrame, width=1000, height=700)  # create the canvas

# creating the slider for intensity of the black
slide1 = tk.Scale(canvasFrame, from_=0, to=255, length=800, 
                  tickinterval=800, orient='horizontal', label="Hue Left", command=intensity1)
slide1.pack()

slide2 = tk.Scale(canvasFrame, from_=0, to=255, length=800, 
                  tickinterval=800, orient='horizontal', label="Hue Center", command=intensity2)
slide2.pack()

slide3 = tk.Scale(canvasFrame, from_=0, to=255, length=800, 
                  tickinterval=800, orient='horizontal', label="Hue Right", command=intensity3)
slide3.pack()



# the 3 blocks
block1 = canvas1.create_line(300, 50, 300, 300)
canvas1.itemconfig(block1, width=200)
block2 = canvas1.create_line(500, 50, 500, 300)
canvas1.itemconfig(block2, width=200)
block3 = canvas1.create_line(700, 50, 700, 300)
canvas1.itemconfig(block3, width=200)

#help button
helpButton=tk.Button(canvasFrame, command=help, text="Help", bg='blue',fg='white', width=20)
helpButton.pack()

canvas1.pack()
root.mainloop()
