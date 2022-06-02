# DotsAndBoxes
Dots And Boxes game for computers and humans to play:
Developed Dots and Boxes game in python that allows two or more players to connect dots and form a box.The grid size of the dots is flexible. Python’s Numpy 2D arrays are used to store horizontal and vertical lines drawn. Whenever a line is drawn from one point to another, the coordinates are captured and used to check if the lines drawn form a box. Backtracking and greedy approach is used for the computer to select its moves.


Generated an algorithm for the computer to select the next move using the concept of longest chains. The idea is that the computer first searches for a box, if not found it makes or extends chains in the game. When all the straight chains(horizontal and vertical) are made, it closes the smallest chain for the opponent, so at the end, the computer gets to close the chain and gain more boxes. The game is developed for humans vs humans, humans vs computer, computer vs computer.
Technologies used: Python and it’s packages such as Numpy
