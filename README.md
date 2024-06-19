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






- Manual Testing
<table>
    <tr>
            <th>Action</th>
            <th>Expected Behavior</th>
            <th>Pass or Fail</th>
            <th>Notes<th>
    </tr>
        <tr>
            <th>Click Start button</th>
            <th>Initalise the game</th>
            <th>Pass</th>
            <th>Notes<th>
    </tr>
        <tr>
            <th>Left-click on a safe cell</th>
            <th>Reveals the cell content</th>
            <th>Pass</th>
            <th>Cell reveals and the number of mines surrounding the cell are shown<th>
    </tr>
        <tr>
            <th>Right-click on a cell</th>
            <th>Flags the cell as a potential mine</th>
            <th>Pass</th>
            <th>Cell shows an "F" and turns yellow<th>
    </tr>
        <tr>
            <th>Click a mine</th>
            <th>Ends the game and shows "Game Over" message</th>
            <th>Pass</th>
            <th>Ends the game and shows "Game Over" message<th>
    </tr>
        <tr>
            <th>Click Start button after game over</th>
            <th>Resets the game board</th>
            <th>Pass</th>
            <th>Board is cleared and a new game starts<th>
    </tr>
        <tr>
            <th>Left-click on a flagged cell</th>
            <th>No action</th>
            <th>Pass</th>
            <th>Notes<th>
    </tr>
        <tr>
            <th>Right-click on a revealed cell</th>
            <th>No action</th>
            <th>Pass</th>
            <th>Revealed cells should not change<th>
    </tr>
        <tr>
            <th>Attempt to flag all mines</th>
            <th>Flags all mines correctly without exceeding the mine count</th>
            <th>Pass</th>
            <th>Notes<th>
    </tr>
        <tr>
            <th>Reveal cells adjacent to multiple mines</th>
            <th>Correctly displays the number of adjacent mines</th>
            <th>Pass</th>
            <th>Numbers are correctly displayed based on adjacent mines<th>
    </tr>
</table>


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
