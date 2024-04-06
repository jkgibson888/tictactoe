from tkinter import *

class Player():
    playerArray = []

    def returnPlayer(self, i):
        return Player.playerArray[i]

    def __init__(self, player, image, root):
        self.root = root
        self.player = player
        self.image = PhotoImage(file=image)
        self.isPlaying = False
        Player.playerArray.append(self)

    def getPlayer(player):
        if player.isPlaying == True:
            return player

    def setPlayer(player):
        player.isPlaying = True

    def notPlaying(player):
        player.isPlaying = False

    def swapPlayers(self):
        for index,i in enumerate(Player.playerArray):
           # print(Player.playerArray[index].__getattribute__('isPlaying'))
            if Player.playerArray[index].__getattribute__('isPlaying'):
                Player.notPlaying(Player.playerArray[index])

            else:
                Player.setPlayer(Player.playerArray[index])



