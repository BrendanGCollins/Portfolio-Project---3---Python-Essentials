#Import tkinter library, random number generator and messagebox
from tkinter import *
import random
from tkinter import messagebox

#Create main window
root = Tk()
#Set background Color
root.configure(bg = "blue")
#Set size of main window
root.geometry("600x600")
#Add game name
root.title("Minesweeper Game")
#Prevent game area changing outside given height x width
root.resizable(False, False)

#Add top frame for start button
top_frame = Frame(
    root, bg = "grey",
    width = 600,
    height = 120,
)

#Position frome at the top
top_frame.place(x=0, y=0)

#Add right frame for remaining mines
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

#Position the game area frame below the top frame and to the left of the right frame
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

        print("Start button added to top frame") #Debugging

        #Starts the game
        self.start_game()

    def start_game(self):
        print("Game started")  # Debugging
        #Clear game area of any existing widgets
        for widget in game_area.winfo_children():
            widget.destroy()

        #Start game board with zeros
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        #start button array for button widgets
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        #Set to hold mine locations
        self.mines_set = set()

        #Place mines on board
        while len(self.mines_set) < self.mines:
            row = random.randint(0, self.rows -1)
            col = random.randint(0, self.cols -1)
            self.mines_set.add((row, col))

        #Create buttons for each cell
        for row in range(self.rows):
            for col in range(self.cols):
                btn = Button(game_area, height = 6, width = 10)
                btn.grid(row = row, column = col)
                #Bind left mouse button to show cell. Tkinter callback used for button click
                btn.bind("<Button-1>", self.reveal_cell_callback(row, col))
                #Bind right mouse button to show cell. Tkinter callback used for button click
                btn.bind("<Button-3>", self.flag_cell_callback(row, col))
                self.buttons[row][col] = btn

    #Define method to retun callback function for revealing cell
    def reveal_cell_callback(self, row, col):
        #Callback function that will be called
        def callback(event):
            #Call reveal_cell with the row and column
            self.reveal_cell(row, col)
        return callback

    #Define method to return callback function for flaggin cell
    def flag_cell_callback(self, row, col):
        #Callback function that will be called
        def callback(event):
            #Call flag_cell with the row and column
            self.flag_cell(row, col)
        return callback

#Run the Game
game = Minesweeper(root)
root.mainloop()