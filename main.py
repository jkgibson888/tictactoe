from tkinter import *

import game
from player import Player
from board import Board
from getPosition import *

root = Tk()
root.geometry("700x650")


#initialize board
board = Board(root, "tttbackground.png")

#initialize board for logic test
#initialize players
playerX = Player('X', "tttx.png", root)
playerO = Player('O', "ttto.png", root)
playerO.setPlayer()


position = GetPosition(root)
position = root.bind('<Button-1>', position.getPosition)




root.mainloop()














