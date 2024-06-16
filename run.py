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


#Run the Game
root.mainloop()