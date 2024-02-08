# Sudoku Solver with Python, Backtracking

## Overview
The goal of this project is to solve any 9x9 grid sudoku puzzle using the backtracking method. 

## Tools and Programming Language(s)
Python

## Rules of the game
Fill in all the empty cells with the numbers 1 to 9 but also ensuring there are no repetitions in any rows, columns and individual 3x3 grids

### Input
List of 9 lists 

[ [v00, v01, v02, ..., v08],
  [v10, v11, v12, ..., v18],
  ...
  [v80, v81, v82, ..., v88] ]

The 9x9 grid will be filled with numbers from 0 to 9. The empty cells are represented with the number zero -> 0. 

### Output
True and the completed solution, False otherwise
