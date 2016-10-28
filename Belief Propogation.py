#Author: Thomas Braun
#This program uses the belief propogation algorithm to solve a sudoku board
#This can't solve for every board input as the constraints send either a 1 or a 0 to the cells depending on the boardstate
#

class cell():
    """
    Cell Class represents a cell on the sudokuboard to be effected by the constraints
    """    
        def __init__(self, row, col, value):
                self.row = row 
                self.col = col 
                self.value = value
        
def iscomplete(boardstate):
        """
Determines whether a given boardstate is complete
        """
        for i in list(range(9)):
                for j in list(range(9)):
                        if boardstate[i][j] == 0:
                                return False
        return True

def sudokuboardsolve(boardstate):
        """
        Main function that's used to solve the sudoku
        Runs off of a while loop that doesn't terminate until the board is filled
        """
        cellboardstate = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]];

        
        for i in list(range(9)):
                for j in list(range(9)):
                        cellboardstate[i][j] = cell(i + 1, j + 1, boardstate[i][j])

        while (not (iscomplete(boardstate))):
                for i in list(range(9)):
                        for j in list(range(9)):
                                if cellboardstate[i][j].value == 0:
                                        vertconstraint = getvertconstraint(boardstate, cellboardstate[i][j])
                                        horconstraint = gethorconstraint(boardstate, cellboardstate[i][j])
                                        squarearray = getsquarearray(boardstate, cellboardstate[i][j])
                                        if (getvalue(vertconstraint, horconstraint, squarearray) != False):
                                                value = getvalue(vertconstraint, horconstraint, squarearray)
                                                cellboardstate[i][j].value = value[0]
                                                boardstate[i][j] = value[0]
        for i in list(range(9)):
                for j in list(range(9)):
                        cellboardstate[i][j] = cellboardstate[i][j].value
        printsudoku(cellboardstate)


def getvalue(vertconstraint, horconstraint, squarearray):
        """
        Takes in constraints and analyzes whether a value can be assigned, if not, returns False
        """
        Cannotbe = []
        Canbe = []
        for i in list(range(9)):
                if vertconstraint[i] != 0:
                        Cannotbe.append(vertconstraint[i])
        for j in list(range(9)):
                if horconstraint[j] != 0:
                        Cannotbe.append(horconstraint[j])

        for k in list(range(3)):
                for kk in list(range(3)):
                        if squarearray[k][kk] != 0:
                                Cannotbe.append(squarearray[k][kk])

        for i in list(range(1, 10)):
                if i not in Cannotbe:
                        Canbe.append(i)

        if len(Canbe) == 1:
                return Canbe
        else:
                return False
def getvertconstraint(boardstate, cell):
        """
        Gets the vertical constraint for a cell
        """
        vertconstraint = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in list(range(9)):
                if boardstate[i][cell.col - 1] != 0:
                        vertconstraint[i] = boardstate[i][cell.col - 1]
        return vertconstraint

def gethorconstraint(boardstate, cell):
        """
        Gets the horizantal constraint for a cell
        """
        horconstraint = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in list(range(9)):
                if boardstate[cell.row - 1][j] != 0:
                        horconstraint[j] = boardstate[cell.row - 1][j]
        return horconstraint

def getsquarearray(boardstate, cell):
        """
        Returns the square constraint for a cell
        """
        squarearray = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if cell.row <= 3:
                if cell.col <= 3:
                        for k in list(range(3)):
                                for kk in list(range(3)):
                                        if boardstate[k][kk] != 0:
                                                squarearray[k][kk] = boardstate[k][kk]
                if (cell.col > 3) and (cell.col <= 6):
                        for k in list(range(3)):
                                for kk in list(range(3, 6)):
                                        if boardstate[k][kk] != 0:
                                               squarearray[k][kk - 3] = boardstate[k][kk]                                              
                if (cell.col > 6) and (cell.col <= 9):
                        for k in list(range(3)):
                                for kk in list(range(6, 9)):
                                        if boardstate[k][kk] != 0:
                                               squarearray[k][kk - 6] = boardstate[k][kk]                                                                     
        if (cell.row > 3) and (cell.row <= 6):
                if cell.col <= 3:
                        for k in list(range(3, 6)):
                                for kk in list(range(3)):
                                        if boardstate[k][kk] != 0:
                                               squarearray[k - 3][kk] = boardstate[k][kk]
                if (cell.col >3) and (cell.col <= 6):
                        for k in list(range(3, 6)):
                                for kk in list(range(3, 6)):
                                        if boardstate[k][kk] != 0:
                                                squarearray[k - 3][kk - 3] = boardstate[k][kk]
                if (cell.col > 6) and (cell.col <= 9):
                        for k in list(range(3, 6)):
                                for kk in list(range(6, 9)):
                                        if boardstate[k][kk] != 0:
                                               squarearray[k - 3][kk - 6] = boardstate[k][kk]
        if (cell.row > 6) and (cell.row <= 9):
                if cell.col <= 3:
                        for k in list(range(6, 9)):
                                for kk in list(range(3)):
                                         if boardstate[k][kk] != 0:
                                               squarearray[k - 6][kk] = boardstate[k][kk]
                if (cell.col > 3) and (cell.col <= 6):
                        for k in list(range(6, 9)):
                                for kk in list(range(3, 6)):
                                        if boardstate[k][kk] != 0:
                                               squarearray[k - 6][kk - 3] = boardstate[k][kk]                                              
                if (cell.col > 6) and (cell.col <= 9):
                        for k in list(range(6, 9)):
                                for kk in list(range(6, 9)):
                                        if boardstate[k][kk] != 0:
                                               squarearray[k - 6][kk - 6] = boardstate[k][kk]
        return squarearray

def printsudoku(sudokuboard):
        """
        Prints a sudokuboard
        """
        for i in list(range(len(sudokuboard))):
                print(sudokuboard[i])
        return

def main():
        sudokuboard = [[0, 0, 3, 0, 2, 0, 6, 0, 0], [9, 0, 0, 3, 0, 5, 0, 0, 1], [0, 0, 1, 8, 0, 6, 4, 0, 0], [0, 0, 8, 1, 0, 2, 9, 0, 0], 
[7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 6, 7, 0, 8, 2, 0, 0], [0, 0, 2, 6, 0, 9, 5, 0, 0], [8, 0, 0, 2, 0, 3, 0, 0, 9], [0, 0, 5, 0, 1, 0, 3, 0, 0]];
        print("Solved sudoku, image 2, excersize 2: ")
        sudokuboardsolve(sudokuboard)
        return 1


if __name__ == "__main__": main()

