import pygame
import colors
from draftSolver import SudokuSolver
from draftWindow import Window
from inputSudoku import getBoardFromFile

inputSudoku = getBoardFromFile("Board1.txt")

pygame.init()

window = Window()
window.init(startPosX=200, startPosY=100, width=50, height=50, border=5)
window.drawInit(inputSudoku)

finishedInput = False
while(not finishedInput):
    for event in pygame.event.get():

        window.draw()
        window.updateWindow()

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            window.checkClick(mousePos)
            window.resetActiveCells(mousePos)
            finishedInput = window.startButton.isHovered(mousePos) 
        
        if event.type == pygame.KEYDOWN:
            active_cell = window.getActiveCell()
            if active_cell is not None:
                active_cell.active = False       
                active_cell.update(chr(event.key), colors.beige)

solver = SudokuSolver(window.cells, window)
solver.run()
