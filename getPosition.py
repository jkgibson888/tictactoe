
from board import *
from player import *

class GetPosition():
    playedArray = None
    root = None
    def __init__(self, master):
        GetPosition.root = master
        playedArray = Frame(master)
        playedArray.pack()
    def getPosition(self, e):
        self.x = e.x
        self.y = e.y
        print("Pointer is currently at %d, %d" % (self.x, self.y))
        for index,i in enumerate(Player.playerArray):

            if i.isPlaying:
                GetPosition.setArray(e.x, e.y, Board.array, Player.playerArray[index])

    def placeTile(player, xpos, ypos):
        # add image to spot
        image = player.__getattribute__('image')
        print(GetPosition.root.winfo_children())
        label = Label(GetPosition.playedArray, image=image, borderwidth=0, highlightthickness=0)
        label.place(x=xpos, y=ypos)
        print(GetPosition.root.winfo_children())


        # swap players
        player.swapPlayers()

    def setArray( x, y, array, player):
        #set top left
        if x > 100 and x < 190 and y > 81 and y < 176 and array[0][0] != 'X' and array[0][0] != 'O':
            array[0][0] = player.player
            GetPosition.placeTile(player, 110, 100)

        # set top middle
        if x > 200 and x < 286 and y > 81 and y < 176 and array[0][1] != 'X' and array[0][1] != 'O':
            array[0][1] = player.player
            GetPosition.placeTile(player, 205, 100)

        # set top right
        if x > 296 and x < 386 and y > 81 and y < 176 and array[0][2] != 'X' and array[0][2] != 'O':
            array[0][2] = player.player
            GetPosition.placeTile(player, 305, 100)

        #set middle left
        if x > 100 and x < 190 and y > 181 and y < 276 and array[1][0] != 'X' and array[1][0] != 'O':
            array[1][0] = player.player
            GetPosition.placeTile(player, 110, 195)

        # set middle middle
        if x > 200 and x < 286 and y > 181 and y < 276 and array[1][1] != 'X' and array[1][1] != 'O':
            array[1][1] = player.player
            GetPosition.placeTile(player, 205, 195)

        # set middle right
        if x > 296 and x < 386 and y > 181 and y < 276 and array[1][2] != 'X' and array[1][2] != 'O':
            array[1][2] = player.player
            GetPosition.placeTile(player, 305, 195)

        #set bottom left
        if x > 100 and x < 190 and y > 281 and y < 376 and array[2][0] != 'X' and array[2][0] != 'O':
            array[2][0] = player.player
            GetPosition.placeTile(player, 110, 295)

        # set bottom middle
        if x > 200 and x < 286 and y > 281 and y < 376 and array[2][1] != 'X' and array[2][1] != 'O':
            array[2][1] = player.player
            GetPosition.placeTile(player, 205, 295)

        # set bottom right
        if x > 296 and x < 386 and y > 281 and y < 376 and array[2][2] != 'X' and array[2][2] != 'O':
            array[2][2] = player.player
            GetPosition.placeTile(player, 305, 295)



