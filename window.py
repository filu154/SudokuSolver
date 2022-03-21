import pygame
import colors
from cell import Cell

class Window:
    def __init__(self, bckg_clr=colors.black):
        self.window = pygame.display.set_mode((800,800))
        self.buttons = []
        self.bckg_clr = bckg_clr
        self.cells = []

    def init(self, startPosX, startPosY, width, height, border):
        self.createButtons()
        self.createSudokuCells(startPosX, startPosY, width, height, border)

    def draw(self):
        self.fill(self.bckg_clr)

        for button in self.buttons:
            button.draw(self.window)
        for row in self.cells:
            for cell in row:
                cell.draw(self.window)

    def drawInit(self, inputSudoku):
        self.fill(self.bckg_clr)

        for button in self.buttons:
            button.draw(self.window)

        for i in range(0, 9):
            for j in range(0, 9):
                color = colors.beige if inputSudoku[i][j] == "0" else colors.green_blue
                self.cells[i][j].update(inputSudoku[i][j], color)
                self.cells[i][j].draw(self.window)

        self.updateWindow()

    def updateWindow(self):
        pygame.display.update()

    def createSudokuCells(self, startPosX, startPosY, width, height, border):
        for i in range(0, 9):
            row = []
            for j in range(0, 9):
                row.append(Cell(startPosX + i*width, startPosY + j*height, width-border, height-border))
            self.cells.append(row)

    def createButtons(self):
        self.startButton = Cell(0, 0, 200, 100, "Start Solver", colors.better_red)
        self.buttons.append(self.startButton)

    def checkClick(self, mousePos):
        for row in self.cells:
            for cell in row:
                if cell.isHovered(mousePos):
                    cell.activate()
                    cell.update("", colors.grey)

    def getActiveCell(self):
        for row in self.cells:
            for cell in row:
                if cell.isActive():
                    print(cell.X, cell.Y)
                    return cell

    def resetActiveCells(self, mousePos):
        for row in self.cells:
            for cell in row:
                if (cell.isActive() and (not cell.isHovered(mousePos))):
                    cell.active = False
                    cell.update("")

    # functions that copy the behaviour of their implementations in pygame
    def blit(self, surface, coord):
        self.window.blit(surface, coord)

    def fill(self, color):
        self.window.fill(color)