import pygame
import sys
from src import constants

class StartMenu:
    def __init__(self):
        pygame.init()
        screen_info = pygame.display.Info()
        self.__screenWidth, self.__screenHeight = screen_info.current_w, screen_info.current_h
        self.__screenWindow = self.createDisplay()
        self.__backgroundImage = self.createBackgroundImage()
        self.__buttonObject, self.__buttonSurface, self.__buttonText = self.createPlayButton()


    def createDisplay(self):
        pygame.display.set_caption("Start Menu")
        return pygame.display.set_mode((self.__screenWidth, self.__screenHeight))


    def createBackgroundImage(self):
        try:
            originalImage = pygame.image.load(constants.LOCATION_OF_BACKGROUND_IMAGE_RELATIVE_TO_START)
        except pygame.error:
            print("Error loading image:")
            sys.exit()
        originalImageWidth, originalImageHeight = originalImage.get_size()
        imageAspectRatio = originalImageWidth / originalImageHeight
        newImageWidth = self.__screenWidth
        newImageHeight = int(newImageWidth / imageAspectRatio)
        return pygame.transform.scale(originalImage, (newImageWidth, newImageHeight))

    def createPlayButton(self):
        fontToUseInText = pygame.font.Font(None, 36)

        buttonWidth, buttonHeight = constants.MEDIUM_BUTTON_DIMENSIONS

        buttonRectangle = pygame.Rect((self.__screenWidth - buttonWidth) // 2, (self.__screenHeight - buttonHeight) // 2, buttonWidth, buttonHeight)
        button_surface = pygame.Surface(buttonRectangle.size, pygame.SRCALPHA)

        blackColor = (0, 0, 0)
        text = fontToUseInText.render("PLAY GAME", True, blackColor)
        return buttonRectangle, button_surface, text


    def drawBackgroundImage(self):
        self.__screenWindow.blit(self.__backgroundImage, constants.COORDINATES_OF_STARTING_SCREEN)

    def drawPlayButton(self):
        slightlyTransparentWhite = (255, 255, 255, 128)
        pygame.draw.rect(self.__buttonSurface, slightlyTransparentWhite, self.__buttonSurface.get_rect())
        self.__screenWindow.blit(self.__buttonSurface, self.__buttonObject.topleft)
        self.__screenWindow.blit(self.__buttonText, self.__buttonText.get_rect(center=self.__buttonObject.center))


    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__buttonObject.collidepoint(event.pos):
                        return

            self.drawBackgroundImage()
            self.drawPlayButton()

            pygame.display.flip()
