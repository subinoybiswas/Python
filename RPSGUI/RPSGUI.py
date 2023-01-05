from ast import Delete, Global
from imaplib import Commands
from msilib import sequence
from optparse import Values
import re
from tkinter import *
import random
from tkinter import ttk
import os
import sys

win=Tk()
win.title('RPS GUI')
win.geometry("300x400")
win.config(bg="white")
win.resizable(False,False)
paper = PhotoImage(file= 'C:/Users/SUBINOY/Documents/projects/RPSGUI/Pic/paper.png')
rock = PhotoImage(file= 'C:/Users/SUBINOY/Documents/projects/RPSGUI/Pic/rock.png')
scissors = PhotoImage(file= 'C:/Users/SUBINOY/Documents/projects/RPSGUI/Pic/scissors.png')
computer_input = random.choice(['r', 'p', 's'])

user = ttk.Combobox(win,values=("Rock","Paper","Scissors"))
user.pack()
def result():
    global user_input
    if user.get()== "Rock":
         user_input = 'r'
    elif user.get()== "Paper":
        user_input = 'p'
    elif user.get()== "Scissors":
        user_input ='s'
    
    
    
    if(computer_input == 'r' and user_input =='p') or (computer_input == 'p' and user_input == 's') or (computer_input =='s' and user_input == 'r'):
        Label(win, text="You Win!").pack()
  
    else:
        if(computer_input == user_input):
            Label(win,text="It's a Tie").pack()
        else:
            Label(win, text="You Lose!").pack()
    print(user_input)
    print(computer_input)
    Button(win, text="Restart", command=restart_program).pack(pady=20)
    result_button.destroy()
    user.destroy()
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
    
def rndomcom():
    Label(win,text="We chose: ").pack()
    if computer_input == 'r':
        Label(win, image= rock).pack()
    elif computer_input == 'p':
        Label(win, image= paper).pack()
    elif computer_input == 's':
        Label(win, image= scissors).pack()

   
    

#To call several functions with one button
def multifunction(*args):
    for function in args:
        function()

cb = lambda: multifunction(rndomcom, result,)
button = Button(win, text='Press', command=cb)
result_button= ttk.Button(win, text="Result",command= cb)
result_button.pack()
win.mainloop()
