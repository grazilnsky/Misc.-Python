import tkinter as tk
import numpy as np
import os

#initial parameters
ax = 450
ay = 50
_y = 0
dax = 0
day = 0
thicknessScale = 0

#this function thickens or thins the lines based on the values on the thickness slider
def thickness(x):
    canvas1.itemconfig(line1, width=+int(x))
    canvas1.itemconfig(line2, width=+int(x))

#this function moves lines closer or further away from eachother based on the value on the distance slider
def distance(y):
    global dax
    global _y
    _y = y
    pax = int(y) - dax
    dax = int(y)
    canvas1.move(line1, pax/2, 0)
    canvas1.move(line2, -(pax/2), 0)


#this function calculates the visual angle based on a specific formula and my screen resolution.
#the distance will not be calculated for different resolution than 1366x768 px.
def angle():

    global e
    global _y
    S = (int(_y)*2.5)/100
    ang = 2*np.arctan(int(e.get())/2*S)
    printv(ang)

#print the visual angle
def printv(visangval1):
    visangval.set("Your visual angle is: "+str(visangval1))
    
def help():    
    os.system('start ' + 'AngularResolutionHelp.html')
    
root = tk.Tk()  #defining the 'root' for this interface
root.geometry('1100x600')  #setting the initial size for window
root.title('Eyes resolution')  #setting the window title

visangval = tk.StringVar()  #defining the visual angle variable

canvasFrame = tk.Frame(root)  #create a frame in root
canvasFrame.pack()  

canvas1 = tk.Canvas(canvasFrame, width=1000, height=700)  #create the canvas



#distance slider
slider1 = tk.Scale(canvasFrame, from_=1, to=100, length=800, 
                   tickinterval=800, orient='horizontal', label="Distance", command=distance)
slider1.pack()

#thickness slider
slider2 = tk.Scale(canvasFrame, from_=1, to=100, length=800, 
                   tickinterval=800, orient='horizontal', label="Thickness",command=thickness)
slider2.pack()

#text box to input the distance from between the observer's eyes and the monitor
e = tk.Entry(canvasFrame)
e.pack()

label1 = tk.Label(canvasFrame, text="Eye - Monitor distance(cm)")
label1.pack()

#label to print visual angle value
label2 = tk.Label(canvasFrame,textvariable =visangval)
label2.pack()

#Calculate button
calculate = tk.Button(canvasFrame, text="Calculate Visual Angle", command=angle)
calculate.pack(pady=10)

#lines
line1 = canvas1.create_line(ax, ay, ax, 250)
line2 = canvas1.create_line(550, 50, 550, 250)

#help button
helpButton=tk.Button(canvasFrame, command=help, text="Help", bg='blue',fg='white', width=20)
helpButton.pack()

canvas1.pack()
root.mainloop()
