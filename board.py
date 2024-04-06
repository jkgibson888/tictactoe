from tkinter import *
class Board():
    array = [[None] * 3 for i in range(3)]

    # add image file
    def __init__(self, master, pic):
        myFrame = Frame(master)
        myFrame.pack()

        bg = PhotoImage(file=pic)

        # show background image file
        self.label1 = Label(master, image=bg)
        self.label1.image = bg
        self.label1.place(x=0,y=0)

        self.button1 = Button(master, text="Start", bg="green")
        self.button1.place(x=600, y=100)

        self.button2 = Button(master, text="Restart", bg="blue")
        self.button2.place(x=600, y=250)

        self.button3 = Button(master, text="Exit", bg="red", command=master.destroy)
        self.button3.place(x=600, y=400)






