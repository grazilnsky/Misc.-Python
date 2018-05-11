# -*- coding: utf-8 -*-

import tkinter as tk
import pandas as pd
import random
import os


data=pd.read_csv('memory_data.txt')  #read the file as a dataframe
words=data['a'].values.tolist()  #convert it from dataframe to list 
canvasWords=[]  #the set of words to be displayed on the canvas
errorMessages=[]
gameSet=[]    #the set of words in the game

def refreshCanvas(): #this function clears all words from the canvas
    if len(canvasWords)>0:
            for i in canvasWords:
                canvas1.delete(i)
    if len(errorMessages)>0:    #delete all previous error messages
            for i in errorMessages:
                canvas1.delete(i) 
    entry.delete(0, "end") #delete the text in the text box 
    entry.grid_forget() #hide the text box and confirm answer button
    answerButton.grid_forget()
    
def start():
    refreshCanvas()  #clear the canvas
    fillCanvas()     #fill it again
    root.after(var3.get()*1000,stop) #after a desired number of seconds, call the stop method
      
def stop():
    refreshCanvas()   #clear the canvas
    entry.grid(row=6, column=1,columnspan=2)     #make the answer text box and button visible
    answerButton.grid(row=7, column=1,columnspan=2)

def fillCanvas():
    if(var2.get()==1): #if the selection is a word
        
        r1.grid_forget() #hide the radio boxes
        r2.grid_forget() 
        
        pos=random.sample(range(1, 999), var4.get()) #generate a desired number of numbers between 1 and 999
        global gameSet
        fill=[] 
    
        for i in pos:
            fill.append(words[i])   #take the words with the positions generated on line 34
    
        gameSet=fill        #set the game set to the 5 random words
        for i in fill:    #display the words with a random position on the screen
            posX=random.randint(40, 760)  
            posY=random.randint(20, 480)
            canvasWords.append(canvas1.create_text(posX,posY, text=i))
     
    if(var2.get()==2):  #if the selection is a number
        
        r1.grid_forget() #hide the radio boxes
        r2.grid_forget()
        
        gameSet=[]
        pos=random.sample(range(1, 999), var4.get())#generate a desired number of numbers between 1 and 999
        for i in pos:
            gameSet.append(str(i))      #set the game set to the 5 random numbers
        
        for i in pos:    #display the numbers with a random position on the screen
            posX=random.randint(40, 760)  
            posY=random.randint(20, 480)
            canvasWords.append(canvas1.create_text(posX,posY, text=str(i)))
            
            
def compare():
      
    answer=(var1.get())      #retreive the answer set as a string and convert it into a set of strings
    answer=answer.split(' ')
    errors=0
    print(gameSet)
    print(answer)
    for i in range(0, len(gameSet)):
        found=False
        for j in range(0, len(answer)):
            if(gameSet[i]==answer[j]):
                found=True
        if(found==False):
            errors=errors+1
            
    r1.grid(row=1, column=1)  #show the radio boxes      
    r2.grid(row=1, column=2)
    
    errorMessage="The number of errors in your answer is: "+str(errors)
    errorMessages.append(canvas1.create_text(400,490, text=errorMessage))
    correct=len(gameSet)-errors
    errorMessage="The number of correct answers is: "+str(correct)
    errorMessages.append(canvas1.create_text(400,475, text=errorMessage))
    
def help():    
    os.system('start ' + 'MemoryTestHelp.html')
    
    
root=tk.Tk()
root.geometry('800x650') #create the window and set its size and title
root.title('Memory Test')

var1=tk.StringVar() #variable for the entry
var2=tk.IntVar()    #variable for the radiobuttons
var3=tk.IntVar()    #variable for time
var4=tk.IntVar()    #variable for number of objects

canvasFrame = tk.Frame(root)  #create the canvas
canvasFrame.grid(row=0, column=1, columnspan=2) 
canvas1 = tk.Canvas(canvasFrame, width=800, height=500, bg='white')
canvas1.create_text(400,20, text="Write your answer with an empty space between each word or number.")

#radio buttons for choosing between numbers and words

r1=tk.Radiobutton(canvasFrame, text="Words", variable=var2, value=1)
r1.grid(row=1, column=1)
r2=tk.Radiobutton(canvasFrame, text="Numbers", variable=var2, value=2)
r2.grid(row=1, column=2)

#duration on screen and number of objects entries
l1=tk.Label(canvasFrame, text="Duration")
l1.grid(row=2, column=1)
l2=tk.Label(canvasFrame, text="Number of objects")
l2.grid(row=2, column=2)
entryD=tk.Entry(canvasFrame,width=50, textvariable=var3)
entryD.grid(row=3, column=1)
entryN=tk.Entry(canvasFrame,width=50, textvariable=var4)
entryN.grid(row=3, column=2)
#create the start button
startButton = tk.Button(canvasFrame, text="Start", command=start, width=20, bg='blue', fg='white')
startButton.grid(row=4, column=1,columnspan=1) 

#help button
helpButton=tk.Button(canvasFrame, command=help, text="Help", bg='blue',fg='white', width=20)
helpButton.grid(row=4, column=2, columnspan=1)

canvas1.grid(row=5, column=1,columnspan=2) 

#entry and answer button without being put into the grid
entry=tk.Entry(canvasFrame,width=50, textvariable=var1)
answerButton = tk.Button(canvasFrame, text="Confirm Answer", command=compare)



root.mainloop()
