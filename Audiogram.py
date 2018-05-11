# -*- coding: utf-8 -*-

import numpy as np
import pyaudio as pa
import tkinter as tk
import matplotlib.pyplot as plt
import os

frequencies=[]
volumes=[]

  
def getSound():
    #get the selected values for frequency and volume
    selection = (int)(var.get())  
    selection2 = (int)(var1.get())
    PyAudio=pa.PyAudio
    
    
    freq=selection #hz
    fs=44100 #hz        
    volume=selection2/10
    length=2 #seconds of playtime

    samples = (np.sin(2*np.pi*np.arange(fs*length)*freq/fs)).astype(np.float32)   
    
    p=PyAudio()
    stream = p.open(format=pa.paFloat32, channels=1, rate=fs, output=True)
    
    stream.write(samples*volume)
    stream.stop_stream()
    stream.close()
    p.terminate
    
def plot():
    
    #first, sort frequencies and volumes in ascending order of frequency. 
    #I sorted them in parallel because the position fo the volume in the sorted array 
    #must be the same as the position of its corresponding frequency at the time of recording
    for i in range(0, len(frequencies)):   
        for j in range(i, len(frequencies)):
            if frequencies[i]>frequencies[j]:
                aux1=frequencies[i]
                aux2=volumes[i]
                frequencies[i]=frequencies[j]
                volumes[i]=volumes[j]
                frequencies[j]=aux1
                volumes[j]=aux2
                
    print(frequencies)
    print(volumes)
    plt.close("all") 
    freq=np.log(frequencies)
    vol=volumes
    plt.plot(freq, vol) #plot the volume as a function of ln(frequency)
    plt.show()
    
def record():
    selection = (int)(var.get())
    selection2 = (int)(var1.get())

    freq=selection #hz
    volume=selection2/10
    
    #if the selected frequency and volume are different from 0,
    #add their values to the corresponding array
    if freq!=0 and volume!=0.0:    
        frequencies.append(freq)
        volumes.append(volume)
        print("recorded", freq, " ", volume)
    
def help():    
    os.system('start ' + 'AudiogramHelp.html')

    
root = tk.Tk()          #create the window
root.title("Audiogram") #set its title

var = tk.DoubleVar()    #create the text boxes' variables
var1 = tk.DoubleVar()


#frequency text box
l1=tk.Label(root, text="Sound Frequency (20-20.000 Hz)",anchor="w") 
l1.grid(row=1, column=1)

entry=tk.Entry(root, textvariable=var)
entry.grid(row=1, column=2, padx=10, pady=10)

#volume text box
l2=tk.Label(root, text="Sound Intensity (0-20)",anchor="w")
l2.grid(row=2, column=1)

entry2=tk.Entry(root, textvariable=var1)
entry2.grid(row=2, column=2, padx=10, pady=10)

#Play Sound
button = tk.Button(root, text = "Generate Tone", command = getSound)
button.grid(row=3, column=1, padx=10, pady=10)

#Record frequency and volume
button2=tk.Button(root, text = "Record", command = record)
button2.grid(row=3, column=2, padx=10, pady=10)

#plot the data
button3=tk.Button(root, text="Plot", command = plot)
button3.grid(row=3, column=3, padx=10, pady=10)

#help button
helpButton=tk.Button(root, command=help, text="Help", bg='blue',fg='white', width=20)
helpButton.grid(row=4, column=1, padx=10, pady=10) 
   
root.mainloop()   