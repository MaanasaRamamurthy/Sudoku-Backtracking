# Sudoku Solver Using Backtracking Algorithm and Pygame

Steps:
1. Start by finding a empty cell in the grid.
2. Check which number from 1 to 9 is valid for the particular cell and update the cell accordingly.
3. To check the validity, it should be made sure that the number is not present in
    i) same row
    ii) same column
    iii) 3x3 subgrid
4. If the cell is not empty, we move to next cell in the row until a empty cell is found and repeat steps 1 and 2.
5. If none of the numbers from 1 to 9 is valid for the current cell,
    we will go back to the last updated cell and try with another valid value (i.e. backtrack).
6. Repeat the above steps until all the cells in the grid are filled.

The GUI was created using Pygame. The previously filled numbers are shown in Red and the rest in Black!

![sudoku](https://user-images.githubusercontent.com/92803996/230758971-bc46c817-62b1-4d44-9a61-ee82c327e393.jpg)


