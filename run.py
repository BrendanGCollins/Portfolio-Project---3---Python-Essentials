#Import tkinter library, random number generator and messagebox
from tkinter import *
import random
from tkinter import messagebox

#Create main window
root = Tk()
#Set background Color
root.configure(bg = "grey")
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

#Position frame at the top
top_frame.place(x=0, y=0)

#Add bottom frame
bottom_frame = Frame(
    root, bg = "grey",
    width = 600,
    height = 60,
)

#Add bottom frame position
bottom_frame.place(x=0, y=540)

#Add label for game text
bottom_label = Label(bottom_frame, text = "Minesweeper", bg = "grey", font =("Verdana", "20"))
bottom_label.pack(pady=10)

# Add right frame
right_frame = Frame(
    root, bg="grey"
)
right_frame.pack(fill=Y, side=RIGHT)

#Add game instructions to right frame
info_1 = Label(
    right_frame,
    text = "Clear a grid of squares by clicking on safe squares and avoiding mines.",
    bg="grey",
    wraplength=100, 
    justify=LEFT
)
info_1.pack(pady = 10, padx = 10)

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
        self.revealed_cells = 0

        #Add Start button
        self.start_button = Button(
            top_frame,
            text = "Start",
            command=self.start_game,
            width = 20,
            height = 2
        )
        #Center the start button in top frame
        self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        print("Start button added to top frame") #Debugging

        #Starts the game
        self.start_game()

    def start_game(self):
        print("Game started")  # Debugging
        #Clear game area of any existing widgets
        for widget in game_area.winfo_children():
            widget.destroy()
        
        #Reset count for revealed cells
        self.revealed_cells = 0

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

        for mine in self.mines_set:
            row, col = mine
            self.board[row][col] = "M"
        
        #Calculate mines around each cell
        self.calculate_mines_around()

        #Create buttons for each cell
        for row in range(self.rows):
            for col in range(self.cols):
                btn = Button(game_area, height = 5, width = 12)
                btn.grid(row = row, column = col)
                #Bind left mouse button to show cell. Tkinter callback used for button click
                btn.bind("<Button-1>", self.reveal_cell_callback(row, col))
                #Bind right mouse button to show cell. Tkinter callback used for button click
                btn.bind("<Button-3>", self.flag_cell_callback(row, col))
                self.buttons[row][col] = btn

    def calculate_mines_around(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != "M":
                    mines_count = 0
                    #Loop to check row mines. -1 and +2 prevent checking above and below board
                    for row_adjacent in range(max(0, row -1), min(self.rows, row +2)):
                        #Loop to check column mines within game board
                        for col_adjacent in range(max(0, col -1), min(self.cols, col +2)):
                            if self.board[row_adjacent][col_adjacent] == "M":
                                mines_count += 1
                    self.board[row][col] = mines_count

    #Define method to return callback function for revealing cell
    def reveal_cell_callback(self, row, col):
        #Callback function that will be called
        def callback(event):
            #Call reveal_cell with the row and column
            self.reveal_cell(row, col)
        return callback

    #Define method to return callback function for flagging cell
    def flag_cell_callback(self, row, col):
        #Callback function that will be called
        def callback(event):
            #Call flag_cell with the row and column
            self.flag_cell(row, col)
        return callback
    
    def reveal_cell(self, row, col):
        #Ignore if button is already revealed or flagged
        btn = self.buttons[row][col]
        if btn["state"] == DISABLED:
            return

        #If cell has mine shows it and ends game
        if self.board[row][col] == "M":
            self.buttons[row][col].config(text = "Mine", bg = "red")
            self.game_over()
        #update button text and color. Disable button and increment cell count
        else:
            self.buttons[row][col].config(text = str(self.board[row][col]), bg = "green")
            self.revealed_cells +=1
            #Check if player has won the game
            if self.revealed_cells == (self.rows * self.cols) - self.mines:
                self.win_game()

    #Function for flagging/unflagging cells
    def flag_cell(self, row, col):
        btn = self.buttons[row][col]
        #Check current text displayed. If text is empty string means currently unflagged
        if btn["text"] == "":
            # Changes btn to display 'F' and color to yellow
            btn.config(text="F", bg="yellow")
        # If already flagged, unflag
        elif btn["text"] == "F":
            btn.config(text="", bg="white")
    
    def win_game(self):
        messagebox.showinfo("Winner!", "You cleared all the mines")
    
    def game_over(self):
        messagebox.showinfo("Game Over", "You hit a mine")
        #Disable buttons
        for row in range(self.rows):
            for col in range(self.cols):
                self.buttons[row][col].config(state=DISABLED)

#Run the Game
game = Minesweeper(root)
root.mainloop()