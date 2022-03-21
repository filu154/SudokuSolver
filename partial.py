import copy

class Partial:
    def __init__(self):
        self.values = [[0 for i in range(0, 9)] for j in range(0, 9)]
        self.possible = [[None for i in range(0, 9)] for j in range(0, 9)]
        self.changes = []

    # Create a list of Partials with the updated possible values
    def playMoves(self, i, j):
        partialsList = []
        for d in self.possible[i][j]:
            newPartial = Partial()
            for i1 in range(0, 9):
                for j1 in range(0, 9):
                    newPartial.values[i1][j1] = self.values[i1][j1]
                    newPartial.possible[i1][j1] = copy.deepcopy(self.possible[i1][j1])
            
            for change in self.changes:
                newPartial.changes.append(change)

            newPartial.makeMove(i, j, d)
            newPartial.updateChanges((i, j))
            partialsList.append(newPartial)
                
        return partialsList

    # Make move in the Partial
    def makeMove(self, i, j, d):
        self.values[i][j] = d
        self.possible[i][j] = []
        self.updatePartial(i, j, d)

    # Update the array of changes
    def updateChanges(self, coord):
        self.changes.append(coord)

    # Update the other cells so that the value d won't appear
    # in their possible values anymore
    def updatePartial(self, i, j, d):
        for i1 in range(0, 9):
            if d in self.possible[i1][j]:
                self.possible[i1][j].remove(d)
        for j1 in range(0, 9):
            if d in self.possible[i][j1]:
                self.possible[i][j1].remove(d)
        squareX = i // 3 * 3
        squareY = j // 3 * 3
        for i1 in range(squareX, squareX+3):
            for j1 in range(squareY, squareY+3):
                if d in self.possible[i1][j1]:
                    self.possible[i1][j1].remove(d) 
                    

    # Get the number of possible values for a cell
    def getScore(self, i, j):
        return len(self.possible[i][j])

    # Find the cell with the least number of possible values
    def findNextMove(self):
        minScore = 10
        nextMove = None
        for i in range(0, 9):
            for j in range(0, 9):
                if self.getScore(i, j) > 0 and self.getScore(i, j) < minScore:
                    minScore = self.getScore(i, j)
                    nextMove = (i, j)
                if self.getScore(i, j) == 0 and self.values[i][j] == 0:
                    nextMove = None
                    break
        return nextMove

    # Check if the solution is complete
    def isComplete(self):
        for row in self.values:
            for value in row:
                if value == 0:
                    return False
        return True