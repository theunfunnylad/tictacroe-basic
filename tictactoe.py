from tkinter import *
import tkinter.messagebox
tk=Tk()
tk.title("Tic Tac Toe")
tk.iconbitmap('logo.ico')
tk.resizable(width=False,height=False)
chance = 9
click = True
def x_or_0(buttons):
    global click
    global chance
    if buttons["text"] == " " and click == True:
        chance=chance-1
        buttons["text"] = "X"
        buttons.config(relief = SUNKEN,fg="MEDIUMVIOLETRED",bg="LIGHTCORAL")
        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or 
           button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
           button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
           button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
           button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
           button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
           button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
           button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
           tkinter.messagebox.showinfo("YOU WON","Player X win the game")
           tk.destroy()
        elif (chance==0):
            tkinter.messagebox.showinfo("Tie","The game is Tie")
            tk.destroy()
        click = False
        
    elif buttons["text"] == " " and click == False:
        chance=chance-1
        buttons["text"] = "0"
        buttons.config(fg="BLUE",bg="SALMON")
        if (button1["text"] == "0" and button2["text"] == "0" and button3["text"] == "0" or
            button4["text"] == "0" and button5["text"] == "0" and button6["text"] == "0" or
            button7["text"] == "0" and button8["text"] == "0" and button9["text"] == "0" or
            button1["text"] == "0" and button4["text"] == "0" and button7["text"] == "0" or
            button2["text"] == "0" and button5["text"] == "0" and button8["text"] == "0" or
            button3["text"] == "0" and button6["text"] == "0" and button9["text"] == "0" or
            button1["text"] == "0" and button5["text"] == "0" and button9["text"] == "0" or
            button3["text"] == "0" and button5["text"] == "0" and button7["text"] == "0"):
            tkinter.messagebox.showinfo("YOU WON","Player 0 win the game")
            tk.destroy()
        
        elif (chance==0):
            tkinter.messagebox.showinfo("Tie","The game is tie")
            tk.destroy()
        click = True
buttons=StringVar()
button1 =Button(tk,text=" ",font=("Cooper 26 bold"),height = 2,width = 4, command=lambda:x_or_0(button1))
button1.grid(row=1,column=0,sticky = S+N+E+W)
button2 =Button(tk,text=" ",font=("Cooper 26 bold"),height = 2,width = 4, command=lambda:x_or_0(button2))
button2.grid(row=1,column=1,sticky = S+N+E+W)
button3 =Button(tk,text=" ",font=("Cooper 26 bold"),height = 2,width = 4, command=lambda:x_or_0(button3))
button3.grid(row=1,column=2,sticky = S+N+E+W)
button4 =Button(tk,text=" ",font=("Cooper 26 bold"),height = 2,width = 4, command=lambda:x_or_0(button4))
button4.grid(row=2,column=0,sticky = S+N+E+W)
button5 =Button(tk,text=" ",font=("Cooper 26 bold"),height = 2,width = 4, command=lambda:x_or_0(button5))
button5.grid(row=2,column=1,sticky = S+N+E+W)
button6 =Button(tk,text=" ",font=("Cooper 26 bold"),height = 2,width = 4, command=lambda:x_or_0(button6))
button6.grid(row=2,column=2,sticky = S+N+E+W)
button7 =Button(tk,text=" ",font=("Cooper 26 bold"),height = 2,width = 4, command=lambda:x_or_0(button7))
button7.grid(row=3,column=0,sticky = S+N+E+W)
button8 =Button(tk,text=" ",font=("Cooper 26 bold"),height = 2,width = 4, command=lambda:x_or_0(button8))
button8.grid(row=3,column=1,sticky = S+N+E+W)
button9 =Button(tk,text=" ",font=("Cooper 26 bold"),height = 2,width = 4, command=lambda:x_or_0(button9))
button9.grid(row=3,column=2,sticky = S+N+E+W)

tk.mainloop()
#HP
#Debugged_by_VJ
