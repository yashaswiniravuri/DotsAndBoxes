# Dots And Boxes Game

Dots And Boxes is a simple game that allows two or more players to connect dots and form a box. The grid size of the dots is flexible. Horizontal and vertical lines drawn on the grid are stored using Python's Numpy 2D arrays. Whenever a line is drawn from one point to another, the coordinates are captured and used to check if the lines drawn form a box.

The game is developed for humans vs humans, humans vs computer, and computer vs computer. 

## Technologies Used

Python and its packages such as Numpy were used to develop this game.

## Rules

The game board is a grid of dots. Players take turns connecting two adjacent dots with a horizontal or vertical line. If a player completes a square by drawing the fourth side, they place their initial in the box and take another turn. The game ends when all possible squares are completed. The player with the most squares at the end of the game wins.

## Algorithm

An algorithm was generated for the computer to select the next move using the concept of longest chains. The idea is that the computer first searches for a box, if not found it makes or extends chains in the game. When all the straight chains (horizontal and vertical) are made, it closes the smallest chain for the opponent, so at the end, the computer gets to close the chain and gain more boxes.

## How to Play

### Installation

1. Clone the repository or download the source code.
2. Navigate to the directory containing the code.

### Running the Game
- To start the game, run 'python main.py'
- To play against another human player, press 1.
- To play against the computer, press 2.
- To watch the computer play against itself, press 3.

### Game Controls
- To draw a line between two points, enter the starting and ending point coordinates in the format x1,y1,x2,y2 and press Enter.

## References

The algorithm for the computer's moves was inspired by [wikipedia](https://en.wikipedia.org/wiki/Dots_and_boxes)

## Contributing

Feel free to submit pull requests or open issues for any bugs or feature requests.
