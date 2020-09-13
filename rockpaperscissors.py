import random
from tkinter import *
import tkinter.messagebox

app = Tk()
# The title of the project
app.title("Rock Paper Scissors By infinity#1234")
# The size of the window
app.geometry("400x400")


def rock():
    n = random.randint(0, 18)
    if (n >= 13):
        cpuchoice = 'rock'
    elif (n >= 7 and n <= 12):
        cpuchoice = 'paper'
    else:
        cpuchoice = 'scissors'

    if (cpuchoice == 'rock'):
        winner = 'tie'
    elif (cpuchoice == 'scissors'):
        winner = 'You'
    elif (cpuchoice == 'paper'):
        winner = 'Computer'

    if (winner == 'You'):
        MsgBox = tkinter.messagebox.askquestion("Rock Paper Scissors", "The computer chose "+ cpuchoice + "\nYou Chose Rock\nYou win!\nDo you want to play again?")
        if MsgBox == 'no':
            app.destroy()
        else:
            return
    elif (winner == 'tie'):
        MsgBox = tkinter.messagebox.askquestion("Rock Paper Scissors", "The computer chose "+ cpuchoice + "\nYou Chose Rock\nYou Tied!\nDo you want to play again?")
        if MsgBox == 'no':
            app.destroy()
        else:
            return
    elif (winner == "Computer"):
        MsgBox = tkinter.messagebox.askquestion("Rock Paper Scissors", "The computer chose "+ cpuchoice + "\nYou Chose Rock\nYou lose!\nDo you want to play again?")
        if MsgBox == 'no':
            app.destroy()
        else:
            return

def paper():
    n = random.randint(0, 18)
    if (n >= 13):
        cpuchoice = 'rock'
    elif (n >= 7 and n <= 12):
        cpuchoice = 'paper'
    else:
        cpuchoice = 'scissors'
    if (cpuchoice == 'rock'):
        winner = 'You'
    elif (cpuchoice == 'scissors'):
        winner = 'Computer'
    elif (cpuchoice == 'paper'):
        winner = 'tie'

    if (winner == 'You'):
        MsgBox = tkinter.messagebox.askquestion("Rock Paper Scissors", "The computer chose "+ cpuchoice + "\nYou Chose Paper\nYou win!\nDo you want to play again?")
        if MsgBox == 'no':
            app.destroy()
        else:
            return
    elif (winner == 'tie'):
        MsgBox = tkinter.messagebox.askquestion("Rock Paper Scissors", "The computer chose "+ cpuchoice + "\nYou Chose Paper\nYou Tied!\nDo you want to play again?")
        if MsgBox == 'no':
            app.destroy()
        else:
            return
    elif (winner == "Computer"):
        MsgBox = tkinter.messagebox.askquestion("Rock Paper Scissors", "The computer chose "+ cpuchoice + "\nYou Chose Paper\nYou lose!\nDo you want to play again?")
        if MsgBox == 'no':
            app.destroy()
        else:
            return

def scissors():
    n = random.randint(0, 18)
    if (n >= 13):
        cpuchoice = 'rock'
    elif (n >= 7 and n <= 12):
        cpuchoice = 'paper'
    else:
        cpuchoice = 'scissors'

    if (cpuchoice == 'rock'):
        winner = 'Computer'
    elif (cpuchoice == 'scissors'):
        winner = 'tie'
    elif (cpuchoice == 'paper'):
        winner = 'You'

    if (winner == 'You'):
        MsgBox = tkinter.messagebox.askquestion("Rock Paper Scissors", "The computer chose "+ cpuchoice + "\nYou Chose Scissors\nYou Win!\nDo you want to play again?")
        if MsgBox == 'no':
            app.destroy()
        else:
            return
    elif (winner == 'tie'):
        MsgBox = tkinter.messagebox.askquestion("Rock Paper Scissors", "The computer chose "+ cpuchoice + "\nYou Chose Scissors\nYou Tied!\nDo you want to play again?")
        if MsgBox == 'no':
            app.destroy()
        else:
            return
    elif (winner == "Computer"):
        MsgBox = tkinter.messagebox.askquestion("Rock Paper Scissors", "The computer chose "+ cpuchoice + "\nYou Chose Scissors\nYou Lose!\nDo you want to play again?")
        if MsgBox == 'no':
            app.destroy()
        else:
            return

rock = Button(app, text="Rock", command=rock)
rock.pack()

paper = Button(app, text="Paper", command=paper)
paper.pack()

scissors = Button(app, text="Scissors", command=scissors)
scissors.pack()

app.mainloop()
