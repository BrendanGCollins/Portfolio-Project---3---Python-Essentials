![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Minesweeper Game

 Minesweeper Game is a classic puzzle game where your goal is to clear a grid of squares by clicking on safe squares and avoiding mines. This project uses the tkinter library for the graphical user interface.


## Features

### Existing Features

- __Navigation and Layout__

    - Top Frame: Contains the Start button to initiate the game.
    - Bottom Fame: Displays "Minesweeper" text.
    - Right Frame: Provides game instructions for the player.
    - Game Area: The main area where the game is displayed.

- __Game Functionality__
    - Start Button: Starts the game, places mines randomly and sets up the game board.
    - Game board cells: Each cell can be clicked to reveal if it has a mine or not. Left mouse button reveals the cell, right mouse button flags the cell as potentially containing a mine.
    - Winner notification: If all non-mine cells are revealed then a winning message is displayed.
    - Game over notification: If a mine is clicked the game will end and a "Game Over" message is displayed. 

- __Features left to Implement__
    - Difficulty levels: Add options for different mine counts and grid sizes.
    - Timer: Add a timer to track how quick you can beat the game.
    - Highscore table: A table showing high scores based on how quickly the game was completed.


## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
