import pygame
import sys
from src import constants


class GameWindow:
    def __init__(self, services):
        self.__services = services
        pygame.init()

        self.__hitIcon = pygame.image.load(constants.LOCATION_OF_HIT_ICON)
        self.__almostHitIcon = pygame.image.load(constants.LOCATION_OF_ALMOST_HIT_ICON)

        screenInfo = pygame.display.Info()
        self.__screenWidth, self.__screenHeight = screenInfo.current_w, screenInfo.current_h
        self.__screenWindow = pygame.display.set_mode((self.__screenWidth, self.__screenHeight))

        self.__leftSectionOfScreen = pygame.Rect(0, 0, self.__screenWidth // 2, self.__screenHeight)
        self.__rightSectionOfScreen = pygame.Rect(self.__screenWidth // 2, 0, self.__screenWidth // 2,
                                                  self.__screenHeight)

        self.__userGridRectangles = self.createGrid(self.__rightSectionOfScreen)
        self.__computerGridRectangles = self.createGrid(self.__leftSectionOfScreen)
        self.__counterIfShipWasAdded = [constants.THIS_SHIP_WAS_NOT_ADDED] * constants.NUMBER_OF_SHIPS

        self.__menuTitle = self.createMenuTitle()

        self.__shipHitByComputer = None
        self.__shipHitByUser = None

    # ---------------------------------------
    # VISUAL CREATORS DOWN HERE
    # ---------------------------------------

    @staticmethod
    def createMenuTitle():
        fontToUseInText = pygame.font.Font(None, constants.BOARD_BUILDER_TITLE_SIZE)
        text = fontToUseInText.render(constants.ATTACK_COMPUTERS_SHIP_TEXT, True, constants.COLOR_BLACK)
        return text

    def createGrid(self, screenSection):
        tileSize = int(self.__rightSectionOfScreen.width * constants.TILE_DIMENSION_AS_PERCENTAGE_OF_SCREEN)
        spaceNeededForTile = tileSize + constants.SPACING_BETWEEN_TILES

        startPositionXAxis = screenSection.centerx - (constants.GRID_OFFSET_X_AXIS * spaceNeededForTile) // constants.NUMBER_OF_SCREEN_SECTIONS
        startPositionYAxis = screenSection.centery - (constants.GRID_OFFSET_Y_AXIS * spaceNeededForTile) // constants.NUMBER_OF_SCREEN_SECTIONS

        gridRectangles = [
            [pygame.Rect(startPositionXAxis + column * spaceNeededForTile,
                         startPositionYAxis + row * spaceNeededForTile, tileSize, tileSize) for column in
             range(constants.DIMENSION_OF_BOARD)]
            for row in range(constants.DIMENSION_OF_BOARD)
        ]
        return gridRectangles

    def createGameUpdateText(self, shipId, entityWhoHit):
        fontToUseInText = pygame.font.Font(None, constants.BOARD_BUILDER_TITLE_SIZE)
        textToUse = entityWhoHit + constants.SHIP_HIT_UPDATE_TEXT + constants.NAME_OF_SHIPS[shipId]
        textToDraw = fontToUseInText.render(textToUse, True, constants.COLOR_BLACK)
        return textToDraw

    # ---------------------------------------
    # SCREEN DRAWERS DOWN HERE
    # ---------------------------------------

    def drawLeftAndRightSectionsOfScreen(self):
        pygame.draw.rect(self.__screenWindow, constants.COLOR_RED, self.__leftSectionOfScreen)
        pygame.draw.rect(self.__screenWindow, constants.COLOR_GREEN, self.__rightSectionOfScreen)


    def drawUserBoard(self):
        for lineNumber, boardGridRow in enumerate(self.__userGridRectangles):
            for columnNumber, positionOfRectangleToDraw in enumerate(boardGridRow):
                positionOfTileOnGrid = (columnNumber, lineNumber)
                typeOfShipOnTheTile = self.__services.checkIfTileIsOccupiedOnUserBoard(positionOfTileOnGrid)
                if typeOfShipOnTheTile == constants.EMPTY_TILE:
                    pygame.draw.rect(self.__screenWindow, constants.COLOR_LIGHT_BLUE, positionOfRectangleToDraw)
                    if self.__services.checkIfTileIsHitOnUserBoard(positionOfTileOnGrid) != constants.EMPTY_TILE:
                        self.__screenWindow.blit(self.__almostHitIcon, positionOfRectangleToDraw)
                else:
                    pygame.draw.rect(self.__screenWindow, constants.COLOR_OF_TILES_FOR_SHIP[typeOfShipOnTheTile],
                                     positionOfRectangleToDraw)
                    if self.__services.checkIfTileIsHitOnUserBoard(positionOfTileOnGrid) != constants.EMPTY_TILE:
                        self.__screenWindow.blit(self.__hitIcon, positionOfRectangleToDraw)



    # Uncomment this to not see the computer board
    def drawComputerBoard_STANDARD(self):
        for lineNumber, boardGridRow in enumerate(self.__computerGridRectangles):
            for columnNumber, positionOfRectangleToDraw in enumerate(boardGridRow):
                pygame.draw.rect(self.__screenWindow, constants.COLOR_LIGHT_BLUE, positionOfRectangleToDraw)
                positionOfTileOnGrid = (columnNumber, lineNumber)
                typeOfShipOnTheTile = self.__services.checkIfTileIsOccupiedOnComputerBoard(positionOfTileOnGrid)
                if typeOfShipOnTheTile == constants.EMPTY_TILE:
                    if self.__services.checkIfTileIsHitOnComputerBoard(positionOfTileOnGrid) != constants.EMPTY_TILE:
                        self.__screenWindow.blit(self.__almostHitIcon, positionOfRectangleToDraw)
                else:
                    if self.__services.checkIfTileIsHitOnComputerBoard(positionOfTileOnGrid) != constants.EMPTY_TILE:
                        self.__screenWindow.blit(self.__hitIcon, positionOfRectangleToDraw)

    def drawComputerBoard_DEBUG_MODE(self):
        for lineNumber, boardGridRow in enumerate(self.__computerGridRectangles):
            for columnNumber, positionOfRectangleToDraw in enumerate(boardGridRow):
                positionOfTileOnGrid = (columnNumber, lineNumber)

                typeOfShipOnTheTile = self.__services.checkIfTileIsOccupiedOnComputerBoard(positionOfTileOnGrid)
                if typeOfShipOnTheTile == constants.EMPTY_TILE:
                    pygame.draw.rect(self.__screenWindow, constants.COLOR_LIGHT_BLUE, positionOfRectangleToDraw)
                    if self.__services.checkIfTileIsHitOnComputerBoard(positionOfTileOnGrid) != constants.EMPTY_TILE:
                        self.__screenWindow.blit(self.__almostHitIcon, positionOfRectangleToDraw)
                else:
                    pygame.draw.rect(self.__screenWindow, constants.COLOR_OF_TILES_FOR_SHIP[typeOfShipOnTheTile],
                                     positionOfRectangleToDraw)
                    if self.__services.checkIfTileIsHitOnComputerBoard(positionOfTileOnGrid) != constants.EMPTY_TILE:
                        self.__screenWindow.blit(self.__hitIcon, positionOfRectangleToDraw)

    def drawComputerBoard(self):
        if constants.DEBUG_MODE is True:
            self.drawComputerBoard_DEBUG_MODE()
        else:
            self.drawComputerBoard_STANDARD()



    def drawBoard(self):
        self.drawUserBoard()
        self.drawComputerBoard()



    def drawMenuTitle(self):
        self.__screenWindow.blit(self.__menuTitle, self.__menuTitle.get_rect(center=(
            self.__leftSectionOfScreen.centerx, self.__leftSectionOfScreen.top + constants.BOARD_BUILDER_TITLE_OFFSET)))


    def drawGameUpdateTextsIfNeeded(self):
        if self.__shipHitByUser is not None and self.__shipHitByUser != constants.EMPTY_TILE:
            entityWhoHit = "You"
            textToDraw = self.createGameUpdateText(self.__shipHitByUser, entityWhoHit)
            self.__screenWindow.blit(textToDraw, textToDraw.get_rect(center=(
                self.__leftSectionOfScreen.centerx,
                self.__leftSectionOfScreen.bottom + constants.GAME_UPDATES_TEXT_OFFSET)))
        if self.__shipHitByComputer is not None and self.__shipHitByComputer != constants.EMPTY_TILE:
            entityWhoHit = "Computer"
            textToDraw = self.createGameUpdateText(self.__shipHitByComputer, entityWhoHit)
            self.__screenWindow.blit(textToDraw, textToDraw.get_rect(center=(
                self.__rightSectionOfScreen.centerx,
                self.__rightSectionOfScreen.bottom + constants.GAME_UPDATES_TEXT_OFFSET)))


    # ---------------------------------------
    # LOGIC DOWN HERE
    # ---------------------------------------


    def onTilePress(self, tileCoordinates):
        successfullyHitTile = self.__services.handleHit(tileCoordinates)
        if successfullyHitTile:
            self.__shipHitByUser = successfullyHitTile[constants.INDEX_OF_SHIP_HIT_BY_USER]
            self.__shipHitByComputer = successfullyHitTile[constants.INDEX_OF_SHIP_HIT_BY_COMPUTER]
            gameEndedResult = self.__services.checkIfGameEnded()
            if gameEndedResult:
                return gameEndedResult


    # ---------------------------------------
    # EVENT HANDLERS DOWN HERE
    # ---------------------------------------


    @staticmethod
    def quitGame():
        pygame.quit()
        sys.exit()

    def checkIfClickedOnGrid(self, clickEvent):
        for row, rowRectangles in enumerate(self.__computerGridRectangles):
            for column, gridRectangles in enumerate(rowRectangles):
                if gridRectangles.collidepoint(clickEvent.pos):
                    return column, row
        return

    def findWhatObjectWasClicked(self, clickEvent):
        clickedOnGrid = self.checkIfClickedOnGrid(clickEvent)
        if clickedOnGrid:
            return clickedOnGrid
        return

    def handleMouseClick(self, eventToCheck):
        objectThatUserClickedOn = self.findWhatObjectWasClicked(eventToCheck)
        if objectThatUserClickedOn:
            coordinatesOfTile = objectThatUserClickedOn
            return self.onTilePress(coordinatesOfTile)

    def checkEvent(self, eventToCheck):
        if eventToCheck.type == pygame.QUIT:
            self.quitGame()
        if eventToCheck.type == pygame.MOUSEBUTTONDOWN:
            return self.handleMouseClick(eventToCheck)

    def eventLoop(self):
        for eventToCheck in pygame.event.get():
            return self.checkEvent(eventToCheck)

    def gameLoop(self):
        while True:
            shouldSwitchToEndScreen = self.eventLoop()
            if shouldSwitchToEndScreen:
                return shouldSwitchToEndScreen
            self.drawLeftAndRightSectionsOfScreen()
            self.drawBoard()
            self.drawMenuTitle()
            self.drawGameUpdateTextsIfNeeded()
            pygame.display.flip()
