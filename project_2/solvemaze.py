import sys
from maze import Maze

# The main routine.
def main():
  maze = buildMaze(sys.argv[1])
  print "=========================================="
  print "EMPTY MAZE: {}".format(sys.argv[1])
  print "Start: {}\nEnd: {}".format(
    (maze._startCell.row, maze._startCell.col), \
    (maze._exitCell.row, maze._exitCell.col))
  print
  maze.draw()
  print "=========================================="
  print "Attempting to solve maze..."
  print "=========================================="
  if maze.findPath():
    print("STATUS: path found!")
    print "COMPLETED MAZE: {}".format(sys.argv[1])
    print
    maze.draw()
  else :
    print("STATUS: path not found")
    print "There was not a path found from the starting position the the end position, or, the maze is invalid"

# Builds a maze based on a text format in the given file. 
def buildMaze(filename):
  infile = open(filename, "r")
  
  # Read the size of the maze.
  nrows, ncols = readValuePair(infile)
  maze = Maze(nrows, ncols)
  
  # Read the starting and exit positions.
  row, col = readValuePair(infile)
  maze.setStart(row, col)
  row, col = readValuePair(infile)
  maze.setExit(row, col)

  # Read the maze itself.
  for row in range(nrows):
    line = infile.readline()
    for col in range(len(line)):
      if line[col] == "*":
        maze.setWall(row, col)

   # Close the maze file and return the newly constructed maze.
  infile.close()
  return maze
  
# Extracts an integer value pair from the given input file. 
def readValuePair(infile):
  line = infile.readline() 
  valA, valB = line.split()
  return int(valA), int(valB)
  
# Call the main routine to execute the program.
main()
