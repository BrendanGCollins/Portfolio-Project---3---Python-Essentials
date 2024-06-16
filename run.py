#Import tkinter library
from tkinter import *
import random

root = Tk()
#Background Color
root.configure(bg = "blue")
#Set game area size
root.geometry("600x600")
#Add game name
root.title("Minesweeper Game")
#Prevent game area changing outside given height x width
root.resizable(False, False)