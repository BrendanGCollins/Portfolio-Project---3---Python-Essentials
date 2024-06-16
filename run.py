#Import tkinter library/random number generator and messagebox
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
#Background Color
root.configure(bg = "blue")
#Set game area size
root.geometry("600x600")
#Add game name
root.title("Minesweeper Game")
#Prevent game area changing outside given height x width
root.resizable(False, False)

#Add top frame dimensions and color
top_frame = Frame(
    root, bg = "grey",
    width = 600,
    height = 120,
)

#Add top frame position
top_frame.place(x=0, y=0)

#Add right frame dimensions and color
right_frame = Frame(
    root, bg = "grey",
    width = 120,
    height = 480,
)

#Add right frame position
right_frame.place(x=480, y=120)

#Add game area frame
game_area = Frame(
    root, bg = "white",
    width = 480,
    height = 480,
)

#Add game frame position
game_area.place(x=0, y=120)

class Minesweeper:
    def __init__(self, root, rows=5, cols=5, mines=5):
        #initialize the main variables
        self.root = root
        self.rows = rows
        self.cols = cols
        self.mines = mines

        #Add Start button
        self.start_button = Button(
            top_frame,
            text = "Start",
            command=self.start_game
        )
        #Add stat button with padding
        self.start_button.pack(pady=10)

        #Starts the game
        self.start_game()

    def start_game(self):
        #Clear game area of any existing widgets
        for widget in game_area.winfo_children():
            widget.destroy()

        #Start game board with zeros
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        #start button array for button widgets
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        #Set to hold mine locations
        self.mines_set = set()

#Run the Game
root.mainloop()