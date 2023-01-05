from tkinter import *
from tkinter import messagebox
from tkinter import Button
import os
import sys
from turtle import left

win = Tk()
win.title('Tic-Tac-Toe')
win.geometry("600x300")
count = 0
clicked = True

def button_clicked(b):
    global count, clicked
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        print(b["text"])
        
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        
    else:
        messagebox.showerror("Invalid Move")
    print(count)

    if count != 9:

        if button1["text"]== "X" and button2["text"]== "X" and button3["text"]=="X":
            messagebox.showinfo("X Won!")
        elif button4["text"]== "X" and button5["text"] == "X" and button6["text"]=="X":
                messagebox.showinfo("X Won!")
        elif button7["text"]== "X" and button8["text"] == "X" and button9["text"]=="X":
                messagebox.showinfo("X Won!")
        elif button1["text"]== "X" and button4["text"] == "X" and button7["text"]=="X":
                messagebox.showinfo("X Won!")
        elif button2["text"]== "X" and button5["text"] == "X" and button8["text"]=="X":
                messagebox.showinfo("X Won!")
        elif button3["text"]== "X" and button6["text"] == "X" and button9["text"]=="X":
                messagebox.showinfo("X Won!")
        elif button1["text"]== "X" and button5["text"] == "X" and button9["text"]=="X":
                messagebox.showinfo("X Won!")
        elif button3["text"]== "X" and button5["text"] == "X" and button7["text"]=="X":
                messagebox.showinfo("X Won!")
        Button(win, text="Restart", command=restart_program).grid(row=4,column=2)
    
    
    else:
        if button1["text"]== "O" and button2["text"]== "O" and button3["text"]=="O":
            messagebox.showinfo("O Won!")
        elif button4["text"]== "O" and button5["text"] == "O" and button6["text"]=="O":
            messagebox.showinfo("O Won!")
        elif button7["text"]== "O" and button8["text"] == "O" and button9["text"]=="O":
            messagebox.showinfo("O Won!")
        elif button1["text"]== "O" and button4["text"] == "O" and button7["text"]=="O":
            messagebox.showinfo("O Won!")
        elif button2["text"]== "O" and button5["text"] == "O" and button8["text"]=="O":
            messagebox.showinfo("O Won!")
        elif button3["text"]== "O" and button6["text"] == "O" and button9["text"]=="O":
            messagebox.showinfo("O Won!")
        elif button1["text"]== "O" and button5["text"] == "O" and button9["text"]=="O":
            messagebox.showinfo("O Won!")
        elif button3["text"]== "O" and button5["text"] == "O" and button7["text"]=="O":
            messagebox.showinfo("O Won!")
        elif count == 9:
            messagebox.showerror("It's a Tie")
    Button(win, text="Restart", command=restart_program)
  
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

button1= Button(win, text=" ", height=3,width=6,bg="SystemButtonFace",command=lambda:button_clicked(button1))
button2= Button(win, text=" ", height=3,width=6,bg="SystemButtonFace",command=lambda:button_clicked(button2))
button3= Button(win, text=" ", height=3,width=6,bg="SystemButtonFace",command=lambda:button_clicked(button3))

button4= Button(win, text=" ", height=3,width=6,bg="SystemButtonFace",command=lambda:button_clicked(button4))
button5= Button(win, text=" ", height=3,width=6,bg="SystemButtonFace",command=lambda:button_clicked(button5))
button6= Button(win, text=" ", height=3,width=6,bg="SystemButtonFace",command=lambda:button_clicked(button6))

button7= Button(win, text=" ", height=3,width=6,bg="SystemButtonFace",command=lambda:button_clicked(button7))
button8= Button(win, text=" ", height=3,width=6,bg="SystemButtonFace",command=lambda:button_clicked(button8))
button9= Button(win, text=" ", height=3,width=6,bg="SystemButtonFace",command=lambda:button_clicked(button9))


button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

win.mainloop()