board=[]

from tkinter import *
root = Tk()
root.title("Sudoku Solver")
root.geometry("324x550")


label = Label(root, text= "Fill in the numbers and click solve").grid(row=0, column=1, columnspan=10)

#Error label for displaying when solution does not exist
error_label=Label(root, text="No solution exists for the sudoku",fg="red")

#Solved label for displaying when sudoku is solved
solved_label=Label(root, text="Sudoku solved!",fg="green")

# Dictionary to store the Entry widgets representing the cells
cells={}

def ValidateNumber(num):
    out=(num.isdigit() or num== "") and len(num)<2
    return out

reg = root.register(ValidateNumber)

# Function to draw a 3x3 grid of boxes
def draw_grid(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e=Entry(root, width=5, bg=bgcolor, justify="center", validate="key",validatecommand=(reg, "%P"))
            e.grid(row=row+i+1, column=column+j+1, sticky="nsew",padx=1,pady=1,ipady=5)
            cells[(row+i+1,column+j+1)]=e

# Function to draw a 9x9 grid of cells
def draw9x9grid(): 
    color="lightblue"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw_grid(rowNo, colNo, color)
            if color== "lightblue":
                color="white"
            else:
                color = "lightblue"

def clearValues():
    for row in range(2,11):
        for col in range(1,10):
            cell= cells[(row,col)]
            cell.delete(0,"end")
    solved_label.grid_remove()
    error_label.grid_remove()

# Function to solve the Sudoku puzzle
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid_check(board, i,(row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0      
    return False

# Function to check if a number is valid in a given position
def valid_check(board, number, position):
    #Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1]!= i:
            return False
    #Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0]!= i:
            return False
    
    #Check box
    box_x = position[1]//3
    box_y = position[0]//3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3 , box_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True

def find_empty(board):    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)   # row, col
    return None 

# Function to retrieve values from the cells and solve the Sudoku
def getValues():
    for row in range(2,11):
        rows=[]
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val=="":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    solve(board)
    # Show appropriate label based on solution
    if solve(board):
        solved_label.grid(row=15, column=1, columnspan=10, pady=5)
        error_label.grid_remove()
    else:
        solved_label.grid_remove()
        error_label.grid(row=15, column=1, columnspan=10, pady=5)
    display_board(board)

# Function to print the board to the console (for debugging)
def print_board(board):
    for i in range(len(board)):
        if i% 3==0 and i != 0:
            print("--------------------------------")

        for j in range(len(board[0])):
            if j% 3==0 and j!= 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j] ," ", end="")

def display_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                cells[(row+2, col+1)].insert(0, str(board[row][col]))

# Using arrow keys for navigation
def move_focus(event):
    if event.keysym == 'Up':
        event.widget.tk_focusPrev().focus()
    elif event.keysym == 'Down':
        event.widget.tk_focusNext().focus()
    elif event.keysym == 'Left':
        event.widget.tk_focusPrev().focus()
    elif event.keysym == 'Right':
        event.widget.tk_focusNext().focus()

root.bind('<Up>', move_focus)
root.bind('<Down>', move_focus)
root.bind('<Left>', move_focus)
root.bind('<Right>',move_focus)


solve_button= Button(root, command=getValues, text="Solve",width=10)
solve_button.grid(row=20, column=1, columnspan= 5, pady=20)


clear_button= Button(root, command=clearValues, text="Clear",width=10)
clear_button.grid(row=20, column=5, columnspan= 5, pady=20)

draw9x9grid()
root.mainloop()