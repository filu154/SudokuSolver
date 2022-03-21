import pygame
from time import sleep
from draftCell import Cell
from partial import Partial

# Color-scheme 1
beige = (253, 245, 223)
green_blue = (160, 174, 205)
better_red = (189, 30, 81)

class SudokuSolver():
    def __init__(self, cells_input, window):
        # add self.changes to Partial and whenever you pop one from the stack, compare the changes to the prev one and display with red the changes
        self.currPartial = None 
        self.window = window
        self.stackPartials = []
        self.cells_input = cells_input

    def run(self):
        completed = False
        self.currPartial = self.createPartialFromInput(self.cells_input)

        while(True):
            sleep(0.4)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if not completed:
                move = self.currPartial.findNextMove()
                if move is not None:
                    (i, j) = move
                    partialsList = self.currPartial.playMoves(i, j)
                    for partial in partialsList:
                        self.stackPartials.append(partial)
                    self.currPartial = self.stackPartials.pop()
                else:
                    self.displayWrongs() 

            completed = self.currPartial.isComplete()

            self.draw(completed)
            pygame.display.update()


    def createPartialFromInput(self, cells):
        inputPartial = Partial()

        inputPartial.possible = [[[i for i in range(1, 10)] for j in range(0, 9)] for k in range(0, 9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if not cells[i][j].content:
                    inputPartial.values[i][j] = 0
                else:
                    inputPartial.makeMove(i, j, int(self.cells_input[i][j].content))
        
        return inputPartial


    def displayWrongs(self):
        prev = self.currPartial
        curr = self.stackPartials.pop()

        while(len(prev.changes) != len(curr.changes)):
            (i, j) = prev.changes.pop()
            self.cells_input[i][j].update("", better_red)
            self.cells_input[i][j].draw(self.window)
            pygame.display.update()
            sleep(0.3)

        self.currPartial = curr


    def draw(self, completed):
        self.window.fill((0, 0, 0))

        for i in range(0, 9):
            for j in range(0, 9):
                color = green_blue if self.getValueAtPos(i, j) != "0" else beige
                self.cells_input[i][j].update(self.getValueAtPos(i, j), color)
                self.cells_input[i][j].draw(self.window)

    def getValueAtPos(self, i, j):
        return str(self.currPartial.values[i][j])
