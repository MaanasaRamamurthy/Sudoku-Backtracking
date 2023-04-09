# Sudoku Solver Using Backtracking Algorithm and Pygame

Steps:
1. Start by finding a empty cell in the grid.
2. Check which number from 1 to 9 is valid for the particular cell and update the cell accordingly.
3. If the cell is not empty, we move to next cell in the row until a empty cell is found and repeat steps 1 and 2.
4. If none of the numbers from 1 to 9 is valid for the current cell,
    we will go back to the last updated cell and try with another valid value (i.e. backtrack).
5. Repeat the above steps until all the cells in the grid are filled.

The GUI was created using Pygame. The previously filled numbers are shown in Red and the rest in Black!

(https://user-images.githubusercontent.com/92803996/230758786-b0561862-b8db-4a7e-96df-61e17af96d11.jpeg)
