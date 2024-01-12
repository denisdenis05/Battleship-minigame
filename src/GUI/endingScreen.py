import pygame
import sys
from src import constants

class EndingMenu:
    def __init__(self, winner):
        pygame.init()
        screenInformation = pygame.display.Info()
        self.__winner = winner
        self.__screenWidth, self.__screenHeight = screenInformation.current_w, screenInformation.current_h
        self.__screenWindow = self.createDisplay()
        self.__backgroundImage = self.createBackgroundImage()


    # ---------------------------------------
    # VISUAL CREATORS DOWN HERE
    # ---------------------------------------


    def createDisplay(self):
        pygame.display.set_caption("Ending Menu")
        return pygame.display.set_mode((self.__screenWidth, self.__screenHeight))


    def createBackgroundImage(self):
        try:
            if self.__winner == constants.USER_WON:
                originalImage = pygame.image.load(constants.LOCATION_OF_WON_IMAGE)
            else:
                originalImage = pygame.image.load(constants.LOCATION_OF_LOST_IMAGE)
        except pygame.error:
            sys.exit()
        originalImageWidth, originalImageHeight = originalImage.get_size()
        imageAspectRatio = originalImageWidth / originalImageHeight
        newImageWidth = self.__screenWidth
        newImageHeight = int(newImageWidth / imageAspectRatio)
        return pygame.transform.scale(originalImage, (newImageWidth, newImageHeight))


    # ---------------------------------------
    # SCREEN DRAWERS DOWN HERE
    # ---------------------------------------


    def drawBackgroundImage(self):
        self.__screenWindow.blit(self.__backgroundImage, constants.COORDINATES_OF_STARTING_SCREEN)


    # ---------------------------------------
    # EVENT HANDLERS DOWN HERE
    # ---------------------------------------


    @staticmethod
    def quitGame():
        pygame.quit()
        sys.exit()

    def checkEvent(self, eventToCheck):
        if eventToCheck.type == pygame.QUIT:
            self.quitGame()

    def eventLoop(self):
        for event in pygame.event.get():
            return self.checkEvent(event)

    def gameLoop(self):
        while True:
            self.drawBackgroundImage()
            pygame.display.flip()
            self.eventLoop()
