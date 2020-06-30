from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox 
from utils import *
from solution import *

def solve_sudoko():
    '''
    Handles the 'Solve' button
    '''

    # We'll read all the entry fields and store the input into the dictionary
    # format to be submitted to the search code. If a digit, store the digit for
    # that box, otherwise '123456789'
    values = {}
    for square in squares.keys():
        if squares[square].get() == '':
            values[square] = '123456789'
        else:
            values[square] = squares[square].get()

    # Submit the values to the search engine
    solution = search(values)

    # If return is boolean False (puzzle not solved) display error message,
    # otherwise update the UI with the solution by filling in the blanks
    if not solution:
        messagebox.showerror('Insoluable', 'Can\'t be solved')
    else:
        for item in solution.keys():
            if squares[item].get() == '':
                squares[item].insert(1, solution[item])

def clear():
    '''
    Handles the 'Clear' button. Clear all the entries.
    '''

    for square in squares.keys():
        squares[square].delete(0, END)


app = Tk() 
app.title('Soduko')

# Create entry fields in a 9 x 9 grid, all labeled as e.g. 'A3'
squares = {}
for i, row in enumerate(rows):
    for j, col in enumerate(cols):
        squares[row + col] = Entry(app, width = 2, justify=CENTER, font=('Arial', 24))
        squares[row+col].grid(row = i, column = j) 

# Add buttons
solve_btn = Button(app, text='Solve', command=solve_sudoko)
solve_btn.grid(row = 9, column=0, columnspan=7, padx=1)

clear_btn = Button(app, text='Clear', command=clear)
clear_btn.grid(row = 9,  column=2, columnspan=7, padx=1)

# Call Tkinter mainloop to run the UI
app.mainloop()