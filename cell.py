import pygame
import colors

class Cell:
    def __init__(self, X, Y, width, height, content="", color=colors.beige, text_size=32):
        self.content = content
        self.X = X
        self.Y = Y
        self.height = height
        self.width = width
        self.content = "" if content == "0" else content
        self.color = color
        self.active = False

        self.surface = pygame.Surface((width, height))
        self.text_size = text_size
        self.font = pygame.font.SysFont("Times New Roman", self.text_size)

    def update(self, content, color=colors.beige): 
        self.color = color
        self.content = "" if content == "0" else content

    def draw(self, window):
        self.surface.fill(self.color)
        text = self.font.render(self.content, False, colors.black)
        self.surface.blit(text, (0, 0))

        window.blit(self.surface, (self.X, self.Y))

    def isActive(self):
        return self.active

    def activate(self):
        if not self.active:
            self.active = True

    def isHovered(self, mousePos):
        (x, y) = mousePos
        if(x > self.X and x < self.X + self.width):
            if(y > self.Y and y < self.Y + self.height):
                return True
            else:
                return False
        else:
            return False
