
# Sudoku Solver

Welcome! This is my first coding based project where I have created a sudoku solver in python using the tkinter library. 




## Installation

1.Clone the repository to your local machine:

```bash
git clone https://github.com/vinup-ram1308/sudoku-solver
```

2.Navigate to the project directory

```bash
cd sudoku-solver
``` 

3.Run the game:

```bash
python Sudoku_GUI.py
```

## Features

- Allows users to input an incomplete Sudoku puzzle.
- Solves the puzzle using a backtracking algorithm.
- Provides a graphical user interface for input and display.
- Displays a "Sudoku solved!" message upon successful completion.
- Handles keyboard navigation for ease of use.
## How it works

The solver uses a backtracking algorithm to recursively fill in numbers on the Sudoku grid, ensuring that each number is valid according to Sudoku rules. If a conflict arises during the filling process, the algorithm backtracks and tries a different number. This process continues until a solution is found or deemed impossible.
## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Usage

1. Fill in the numbers of the Sudoku puzzle into the grid provided.
2. Click the "Solve" button to solve the puzzle.
3. If there are errors in the input, they will be highlighted.
4. If the puzzle is solvable, the solved puzzle will be displayed.
5. Click the "Clear" button to clear the grid and start afresh.
## Sample game

An empty sudoku grid when you run the code

![Empty_grid](https://github.com/vinup-ram1308/sudoku-solver/assets/157267994/fc1cf7c5-1afc-43af-a854-259c0386f2f4)


Enter valid numbers to solve sudoku

![Unsolved_grid](https://github.com/vinup-ram1308/sudoku-solver/assets/157267994/c6d31783-3f27-4529-a564-4a0ff1437fd7)


Solved sudoku after pressing the Solve button along with a message

![Solved_grid](https://github.com/vinup-ram1308/sudoku-solver/assets/157267994/5f095f8c-69f6-42a0-94cf-a9ba9ae39a4b)


## Contributing

Contributions are always welcome!

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.


