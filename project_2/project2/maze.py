# Implements the Maze ADT using a 2-D array. 
from my_array import Array2D
from lliststack import Stack

class Maze :
# Define constants to represent contents of the maze cells.
    MAZE_WALL = "%" #*
    PATH_TOKEN = "." #x
    TRIED_TOKEN = "-" #o

    # Creates a maze object with all cells marked as open.
    def __init__( self, numRows, numCols ):     
        self._mazeCells = Array2D(numRows, numCols)
        self._startCell = None
        self._exitCell = None
        self._path = Stack()
        self._path_found = False
    # Returns the number of rows in the maze.
    def numRows( self ):
        return self._mazeCells.numRows()

    # Returns the number of columns in the maze.
    def numCols( self ):
        return self._mazeCells.numCols()

    # Fills the indicated cell with a "wall" marker.
    def setWall( self, row, col ):             
        assert row >= 0 and row < self.numRows() and \
        col >= 0 and col < self.numCols(), "Cell index out of range."           
        self._mazeCells.__setitem__( (row, col), self.MAZE_WALL )

    # Sets the starting cell position.
    def setStart( self, row, col ):
        assert row >= 0 and row < self.numRows() and \
        col >= 0 and col < self.numCols(), "Cell index out of range."           
        self._startCell = _CellPosition( row, col )

    # Sets the exit cell position.
    def setExit( self, row, col ):
        assert row >= 0 and row < self.numRows() and \
        col >= 0 and col < self.numCols(), \
        "Cell index out of range."           
        self._exitCell = _CellPosition( row, col )  

    # Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def findPath(self):
        start = (self._startCell.row, self._startCell.col)
        end = (self._exitCell.row, self._exitCell.col)
        # If start is the same as end, then there's an error
        if start == end:
            return False
        self._path.push(start)
        self.make_a_move()
        return self._path_found


    def make_a_move(self):
        # Keep recursion going until stack is empty from not
        # finding a path
        if self._path._size > 0:
            cur_row, cur_col = self._path.peek()
            # If the current cell is also the exit cell
            # Break out of the recursion and return True!
            if self._exitFound(cur_row, cur_col):
                self._markPath(cur_row, cur_col)
                self._path_found = True
                return
            # Checks to see if any of the surrounding cells are
            # valid to move into- up, right, bottom, left
            # If there are valid moves available, move into one
            if (self._validMove(cur_row - 1, cur_col) or \
                self._validMove(cur_row, cur_col + 1) or \
                self._validMove(cur_row + 1, cur_col) or \
                self._validMove(cur_row, cur_col - 1)):
                # Mark the current cell we're on as 'tried'
                self._markPath(cur_row, cur_col)
                # We will now go for one of the next cells
                if self._validMove(cur_row - 1, cur_col):
                    self._path.push((cur_row - 1, cur_col))
                    self.make_a_move()
                elif self._validMove(cur_row, cur_col + 1):
                    self._path.push((cur_row, cur_col + 1))
                    self.make_a_move()
                elif self._validMove(cur_row + 1, cur_col):
                    self._path.push((cur_row + 1, cur_col))
                    self.make_a_move()
                elif self._validMove(cur_row, cur_col - 1):
                    self._path.push((cur_row, cur_col - 1))
                    self.make_a_move()
            # Otherwise, we are at a dead end and must backtrace
            else:
                self._markTried(self._path.peek()[0], self._path.peek()[1])
                self._path.pop()
                self.make_a_move()


    # Resets the maze by removing all "path" and "tried" tokens.
    #def reset( self ):
    #......

    # Prints a text-based representation of the maze.
    def draw( self ):
        # For each row
        for row, row_ndx in enumerate(range(self.numRows())):
            row_display = ''
            # Iterate through the number of columns there are
            # And then print the (row) value
            for col, col_ndx in enumerate(range(self.numCols())):
                if self._mazeCells.__getitem__((row_ndx, col_ndx)) == None:
                    row_display += ' '
                else:
                    row_display += str(self._mazeCells.__getitem__((row_ndx, col_ndx)))
            print row_display


    # Returns True if the given cell position is a valid move.
    def _validMove( self, row, col ):
        return row >= 0 and row < self.numRows() \
        and col >= 0 and col < self.numCols() \
        and self._mazeCells[row, col] is None 

    # Helper method to determine if the exit was found.
    def _exitFound( self, row, col ):
        return row == self._exitCell.row and \
        col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried( self, row, col ):
        self._mazeCells.__setitem__( (row, col), self.TRIED_TOKEN )

    # Drops a "path" token at the given cell.
    def _markPath( self, row, col ):
        self._mazeCells.__setitem__( (row, col), self.PATH_TOKEN ) 


# Private storage class for holding a cell position.
class _CellPosition( object ):
    def __init__( self, row, col ):
        self.row = row
        self.col = col
