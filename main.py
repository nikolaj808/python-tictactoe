from tkinter import *
from tkinter import messagebox
import random
import os
import sys

### FUNCTIONS ###

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

def retry():
	btnrow4 = Frame(root, bg="#000000")
	btnrow4.pack(expand=True, fill=BOTH)

	labelfinish = Label(btnrow4, text="Re?", font=("Elephant", 72), width=1, bg="#145249", fg="#38B11E", bd=0, relief="ridge", highlightthickness=0)
	labelfinish.pack(side=LEFT, expand=True, fill=BOTH)

	byes = Button(btnrow4, text="Yes", font=("Elephant", 72), width=1, bg="#145249", fg="#38B11E", bd=0, relief="ridge", highlightthickness=0, command= lambda: retryButton(1, btnrow4, labelfinish, byes, bno))
	byes.pack(side=LEFT, expand=True, fill=BOTH)
	bno = Button(btnrow4, text="No", font=("Elephant", 72), width=1, bg="#145249", fg="#38B11E", bd=0, relief="ridge", highlightthickness=0, command= lambda: retryButton(0, btnrow4, labelfinish, byes, bno))
	bno.pack(side=LEFT, expand=True, fill=BOTH)
	root.update()

def clearBoard(aboard):
	for i in range(0, 9):
		board[i] = "-"
	b1.config(text="")
	b2.config(text="")
	b3.config(text="")
	b4.config(text="")
	b5.config(text="")
	b6.config(text="")
	b7.config(text="")
	b8.config(text="")
	b9.config(text="")

def checkWin(aboard):
	if aboard[0] == "X" and aboard[1] == "X" and aboard[2] == "X":
		return True
	elif aboard[3] == "X" and aboard[4] == "X" and aboard[5] == "X":
		return True
	elif aboard[6] == "X" and aboard[7] == "X" and aboard[8] == "X":
		return True
	elif aboard[0] == "X" and aboard[3] == "X" and aboard[6] == "X":
		return True
	elif aboard[1] == "X" and aboard[4] == "X" and aboard[7] == "X":
		return True
	elif aboard[2] == "X" and aboard[5] == "X" and aboard[8] == "X":
		return True
	elif aboard[0] == "X" and aboard[4] == "X" and aboard[8] == "X":
		return True
	elif aboard[2] == "X" and aboard[4] == "X" and aboard[6] == "X":
		return True
	elif aboard[0] == "O" and aboard[1] == "O" and aboard[2] == "O":
		return True
	elif aboard[3] == "O" and aboard[4] == "O" and aboard[5] == "O":
		return True
	elif aboard[6] == "O" and aboard[7] == "O" and aboard[8] == "O":
		return True
	elif aboard[0] == "O" and aboard[3] == "O" and aboard[6] == "O":
		return True
	elif aboard[1] == "O" and aboard[4] == "O" and aboard[7] == "O":
		return True
	elif aboard[2] == "O" and aboard[5] == "O" and aboard[8] == "O":
		return True
	elif aboard[0] == "O" and aboard[4] == "O" and aboard[8] == "O":
		return True
	elif aboard[2] == "O" and aboard[4] == "O" and aboard[6] == "O":
		return True
	elif available(aboard) == 0:
		retry()
	return False

def retryButton(button, btnrow, label, byes, bno):
	if button == 1:
		label.pack_forget()
		byes.pack_forget()
		bno.pack_forget()
		btnrow.pack_forget()
		clearBoard(board)
		root.update()
	else:
		root.quit()


def buttonClicked(button):
	if board[button-1] == '-':
		board[button-1] = "X"

		if button == 1:
			b1.config(text="X")
		elif button == 2:
			b2.config(text="X")
		elif button == 3:
			b3.config(text="X")
		elif button == 4:
			b4.config(text="X")
		elif button == 5:
			b5.config(text="X")
		elif button == 6:
			b6.config(text="X")
		elif button == 7:
			b7.config(text="X")
		elif button == 8:
			b8.config(text="X")
		else:
			b9.config(text="X")

		if(checkWin(board)):
			root.update()
			retry()
		root.update()
		if available(board) > 0:
			aiPlayGame()


def findPlacement():
	temp = board

	for i in range(0, 9):
		if temp[i] == "-":
			temp[i] = "O"
			if checkWin(temp):
				temp[i] = "-"
				return i
			else:
				temp[i] = "-"

	for i in range(0, 9):
		if temp[i] == "-":
			temp[i] = "X"
			if checkWin(temp):
				temp[i] = "-"
				return i
			else:
				temp[i] = "-"

	return random.randint(0, 8)

def aiPlayGame():
	while True:
		placement = findPlacement()
		if board[placement] == "-":
			break

	board[placement] = "O"

	if placement + 1 == 1:
		b1.config(text="O")
	elif placement + 1 == 2:
		b2.config(text="O")
	elif placement + 1 == 3:
		b3.config(text="O")
	elif placement + 1 == 4:
		b4.config(text="O")
	elif placement + 1 == 5:
		b5.config(text="O")
	elif placement + 1 == 6:
		b6.config(text="O")
	elif placement + 1 == 7:
		b7.config(text="O")
	elif placement + 1 == 8:
		b8.config(text="O")
	else:
		b9.config(text="O")

	if(checkWin(board)):
		root.update()
		retry()
	root.update()


def available(origBoard):
	counter = 0
	for i in range(0, 9):
		if origBoard[i] == "-":
			counter = counter + 1
	return counter

### CREATING THE BOARD ###

root = Tk()

root.geometry("900x900")
root.title("Ultimate Tic Tac Toe")

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill=BOTH)

btnrow2 = Frame(root, bg="#000000")
btnrow2.pack(expand=True, fill=BOTH)

btnrow3 = Frame(root, bg="#000000")
btnrow3.pack(expand=True, fill=BOTH)

b1 = Button(btnrow1, font=("Elephant", 72), width=1, bg="#000000", fg="white", bd=0, command= lambda: buttonClicked(1))
b1.pack(side=LEFT, expand=True, fill=BOTH)

b2 = Button(btnrow1, font=("Elephant", 72), width=1, bg="#000000", fg="white", bd=0, command= lambda: buttonClicked(2))
b2.pack(side=LEFT, expand=True, fill=BOTH)

b3 = Button(btnrow1, font=("Elephant", 72), width=1, bg="#000000", fg="white", bd=0, command= lambda: buttonClicked(3))
b3.pack(side=LEFT, expand=True, fill=BOTH)

b4 = Button(btnrow2, font=("Elephant", 72), width=1, bg="#000000", fg="white", bd=0, command= lambda: buttonClicked(4))
b4.pack(side=LEFT, expand=True, fill=BOTH)

b5 = Button(btnrow2, font=("Elephant", 72), width=1, bg="#000000", fg="white", bd=0, command= lambda: buttonClicked(5))
b5.pack(side=LEFT, expand=True, fill=BOTH)

b6 = Button(btnrow2, font=("Elephant", 72), width=1, bg="#000000", fg="white", bd=0, command= lambda: buttonClicked(6))
b6.pack(side=LEFT, expand=True, fill=BOTH)

b7 = Button(btnrow3, font=("Elephant", 72), width=1, bg="#000000", fg="white", bd=0, command= lambda: buttonClicked(7))
b7.pack(side=LEFT, expand=True, fill=BOTH)

b8 = Button(btnrow3, font=("Elephant", 72), width=1, bg="#000000", fg="white", bd=0, command= lambda: buttonClicked(8))
b8.pack(side=LEFT, expand=True, fill=BOTH)

b9 = Button(btnrow3, font=("Elephant", 72), width=1, bg="#000000", fg="white", bd=0, command= lambda: buttonClicked(9))
b9.pack(side=LEFT, expand=True, fill=BOTH)

### THE ACTUAL GAME ###

root.mainloop()