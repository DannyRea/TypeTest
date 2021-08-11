from os import close, error
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
from typing import Collection
from TestText import loadText
import WriteDatabase
import time
import math

sentence = ""
entered=""
correctCount = 0
incorrectCount = 0
mispelled = []   
t = 60
def setText():
    global sentence
    global errorBox
    if ((e1.get() == "" or e1.get().isspace()) or (e2.get() == "" or e2.get().isspace())):
        errorBox = Toplevel()
        errorBox.geometry("200x100")
        errorBox.title("Error")
        errorBox.resizable(False, False)
        error= Label(errorBox, text="Please enter both First and Last name.", font=("Times",14,"bold"), wraplength=200, justify=CENTER)
        error.grid(column=1, row= 1, sticky='NSEW')
        b1['state'] = DISABLED   
        errorBox.protocol('WM_DELETE_WINDOW', close)    
    else:
        sentence = loadText()
    
      
        print(sentence)

        # Delete is going to erase anything
        # in the range of 0 and end of file,
        # The respective range given here
        inputtxt.delete(1.0,END)
      
        # Insert method inserts the text at
        # specified position, Here it is the
        # begining
        inputtxt.insert(1.0, sentence)
    
        second.set(3)
        root.update()
        time.sleep(1)
        second.set(2)
        root.update()
        time.sleep(1)
        second.set(1)
        root.update()
        time.sleep(1)
        root.update()
        tick()
    

def scanText():
    global entered
    global correctCount
    global incorrectCount
    global misspelled
      
    input = inputtxt1.get("1.0", END)
    entered+=input
    for word in entered.split():
        if word in sentence.split():
            correctCount+=1
        else:
            print(word)
            mispelled.append(word)
            incorrectCount+=1
    wpm = math.ceil(correctCount/1.0)-incorrectCount
    print(correctCount)
    print(incorrectCount)
    showScore(correctCount, incorrectCount, mispelled, wpm)
    

def showScore(c, i, words,wpm):
    scoreWin = Toplevel()
    scoreWin.geometry("300x300")
    scoreWin.title("Results")
    scoreWin.resizable(False, False)
    testOver = Label(scoreWin, text="Test over!", font=("Arial",14,""), wraplength=200, justify=CENTER)
    testOver.grid(column=2, row= 1, sticky='NSEW')
    correctScore = Label(scoreWin, text="Correct: "+ str(c), font=("Arial",8,""), wraplength=200, justify=CENTER)
    correctScore.grid(column=2, row= 2, sticky='EW')
    incorrectScore = Label(scoreWin, text="Incorrect: "+ str(i), font=("Arial",8,""), wraplength=200, justify=CENTER)
    incorrectScore.grid(column=2, row= 3, sticky='EW')
    wordsWrong = Label(scoreWin, text="Words mispelled: "+ str(words), font=("Arial",8,""), wraplength=200, justify=CENTER)
    wordsWrong.grid(column=2, row= 4, sticky='EW')
    wpmLabel = Label(scoreWin, text="Words per minute (WPM): "+ str(wpm), font=("Arial",8,""), wraplength=200, justify=CENTER)
    wpmLabel.grid(column=2, row= 5, sticky='EW')
    BUpload = Button(scoreWin, text="Upload results to MongoDB", justify=CENTER, command=WriteDatabase.addStats(e1.get(), e2.get(), c, i, words, wpm))
    BUpload.grid(column=2, row=6,sticky='EW')
    scoreWin.grid_columnconfigure(2, weight=1)



def tick():
    global second
    global t
    second.set(t)
    t-=1
    print(t)
    second.set(t)
    if t == 0:
        
        scanText()
    else:
        secondEntry.after(1000, tick)


root = ThemedTk(theme="breeze")

root.geometry("800x600")
root.title("PyType Beta")

second = IntVar()
second.set(0)

fName = ttk.Label(root, text="FName", font=("Times",12,""))
fName.grid(column=1, row=0)
lName = ttk.Label(root, text="LName", font=("Times",12,""))
lName.grid(column=1, row=1)
Ltime= ttk.Label(root, text="Time", font=("Times",12,""))
Ltime.grid(column=1, row=2)
e1 = ttk.Entry(root)
e2 = ttk.Entry(root)
b1 = ttk.Button(root, text="Start", command=setText)

secondEntry= ttk.Entry(root, width=3, font=("Times",18,""), justify=CENTER, state='readonly',
                    textvariable=second)

def close():
     b1['state']=NORMAL
     errorBox.destroy()
     
                             
e1.grid(column = 2, row=0, sticky='EW')
e2.grid(column=2, row=1,sticky='EW')
secondEntry.grid(column=2,row=2, sticky='EW')
b1.grid(column=2,row=3,sticky='EW')


inputtxt =  Text(root, height = 25,
                width = 50,
                bg = "light yellow")

inputtxt1 = Text(root, height = 25,
                width = 50,
                bg = "light yellow")

                

inputtxt.grid(column=2,row=4,sticky='NSEW')
inputtxt1.grid(column=2,row=5,sticky='NSEW')

root.grid_columnconfigure(2, weight=1)






root.mainloop()