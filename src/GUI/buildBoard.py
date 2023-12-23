
import pygame
import sys
from src import constants


class BuildBoardMenu:
    def __init__(self):
        pygame.init()
        screen_info = pygame.display.Info()
        self.__screenWidth, self.__screenHeight = screen_info.current_w, screen_info.current_h
        self.__screenWindow = self.createDisplay()
        self.__selector, self.__selectorRect = self.createSelector()
        self.__tiles = self.createTiles()

    def createDisplay(self):
        pygame.display.set_caption("Game Menu")
        return pygame.display.set_mode((self.__screenWidth, self.__screenHeight))

    def createSelector(self):
        selectorWidth, selectorHeight = 50, 200  # Replace with your specific values
        selectorRect = pygame.Rect(0, 0, selectorWidth, selectorHeight)
        selectorRect.midleft = (0.2 * self.__screenWidth, 0.5 * self.__screenHeight)
        selectorSurface = pygame.Surface(selectorRect.size, pygame.SRCALPHA)
        slightlyTransparentRed = (255, 0, 0, 128)  # Adjust color as needed
        pygame.draw.rect(selectorSurface, slightlyTransparentRed, selectorSurface.get_rect())
        return selectorSurface, selectorRect

    def createTiles(self):
        tile_size = 50  # Replace with your specific value
        tiles = [[pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size) for j in range(10)] for i in
                 range(10)]
        return tiles

    def drawSelector(self):
        self.__screenWindow.blit(self.__selector, self.__selectorRect.topleft)

    def drawTiles(self):
        tile_color = (0, 128, 255)  # Adjust color as needed
        for row in self.__tiles:
            for tile in row:
                pygame.draw.rect(self.__screenWindow, tile_color, tile)

    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__screenWindow.fill((255, 255, 255))  # Fill the background with white
            self.drawSelector()
            self.drawTiles()

            pygame.display.flip()

