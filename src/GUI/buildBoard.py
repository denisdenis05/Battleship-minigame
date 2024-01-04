
import pygame
import sys
from src import constants
from src.services.services import Services


class BuildBoardMenu:
    def __init__(self):
        self.__services = Services()
        pygame.init()

        self.__checkmarkIcon = pygame.image.load(constants.LOCATION_OF_CHECKMARK_ICON)
        self.__pointerIcon = pygame.image.load(constants.LOCATION_OF_POINTER_ICON)

        screenInfo = pygame.display.Info()
        self.__screenWidth, self.__screenHeight = screenInfo.current_w, screenInfo.current_h
        self.__screenWindow = pygame.display.set_mode((self.__screenWidth, self.__screenHeight))

        self.__leftSectionOfScreen = pygame.Rect(0, 0, self.__screenWidth * 2 // 5, self.__screenHeight)
        self.__rightSectionOfScreen = pygame.Rect(self.__screenWidth * 2 // 5, 0, self.__screenWidth * 3 // 4, self.__screenHeight)

        self.__gridRectangles = self.createGrid()
        self.__buttons = self.createButtons()
        self.__counterIfShipWasAdded = [constants.THIS_SHIP_WAS_NOT_ADDED] * constants.NUMBER_OF_SHIPS

        self.__menuTitle = self.createMenuTitle()

        self.selectedShip = None
        self.selectedShipDirection = None
        self.selectedShipPosition = None


    # ---------------------------------------
    # VISUAL CREATORS DOWN HERE
    # ---------------------------------------


    @staticmethod
    def createMenuTitle():
        fontToUseInText = pygame.font.Font(None, constants.BOARD_BUILDER_TITLE_SIZE)
        text = fontToUseInText.render(constants.BUILD_BOARD_CHOOSE_SHIPS_TEXT, True, constants.COLOR_BLACK)
        return text

    def createGrid(self):
        tileSize = int(self.__rightSectionOfScreen.width * constants.TILE_DIMENSION_AS_PERCENTAGE_OF_SCREEN)
        spaceNeededForTile = tileSize + constants.SPACING_BETWEEN_TILES

        startPositionXAxis = self.__rightSectionOfScreen.centerx - (constants.GRID_OFFSET_X_AXIS * spaceNeededForTile) // constants.NUMBER_OF_SCREEN_SECTIONS
        startPositionYAxis = self.__rightSectionOfScreen.centery - (constants.GRID_OFFSET_Y_AXIS * spaceNeededForTile) // constants.NUMBER_OF_SCREEN_SECTIONS

        gridRectangles = [
            [pygame.Rect(startPositionXAxis + column * spaceNeededForTile, startPositionYAxis + row * spaceNeededForTile, tileSize, tileSize) for column in range(constants.DIMENSION_OF_BOARD)]
            for row in range(constants.DIMENSION_OF_BOARD)
        ]
        return gridRectangles

    @staticmethod
    def createButton(buttonText, topLeftCornerPosition):
        topCoordinates = topLeftCornerPosition[constants.INDEX_OF_X_AXIS_VALUE]
        leftCoordinates = topLeftCornerPosition[constants.INDEX_OF_Y_AXIS_VALUE]
        fontSize = 20
        fontToUseInText = pygame.font.Font(None, fontSize)
        buttonWidth, buttonHeight = constants.MEDIUM_BUTTON_DIMENSIONS

        buttonRectangle = pygame.Rect(leftCoordinates, topCoordinates, buttonWidth, buttonHeight)
        button_surface = pygame.Surface(buttonRectangle.size, pygame.SRCALPHA)

        text = fontToUseInText.render(buttonText, True, constants.COLOR_BLACK)
        return buttonRectangle, button_surface, text

    def createButtons(self):
        buttons = {
            "horizontalPatrolBoat": self.createButton("Horizontal Patrol Boat", constants.firstRowFirstButtonPosition),
            "verticalPatrolBoat": self.createButton("Vertical Patrol Boat", constants.firstRowSecondButtonPosition),
            "horizontalSubmarine": self.createButton("Horizontal Submarine", constants.secondRowFirstButtonPosition),
            "verticalSubmarine": self.createButton("Vertical Submarine", constants.secondRowSecondButtonPosition),
            "horizontalDestroyer": self.createButton("Horizontal Destroyer", constants.thirdRowFirstButtonPosition),
            "verticalDestroyer": self.createButton("Vertical Destroyer", constants.thirdRowSecondButtonPosition),
            "horizontalBattleship": self.createButton("Horizontal Battleship", constants.fourthRowFirstButtonPosition),
            "verticalBattleship": self.createButton("Vertical Battleship", constants.fourthRowSecondButtonPosition),
            "horizontalCarrier": self.createButton("Horizontal Carrier", constants.fifthRowFirstButtonPosition),
            "verticalCarrier": self.createButton("Vertical Carrier", constants.fifthRowSecondButtonPosition)}
        return buttons



    # ---------------------------------------
    # SCREEN DRAWERS DOWN HERE
    # ---------------------------------------


    def drawLeftAndRightSectionsOfScreen(self):
        pygame.draw.rect(self.__screenWindow, constants.COLOR_RED, self.__leftSectionOfScreen)
        pygame.draw.rect(self.__screenWindow, constants.COLOR_GREEN, self.__rightSectionOfScreen)


    def colorButtonBackground(self, leftSideSectionSurface, shipId, buttonToDraw, buttonNumberToDraw):
        buttonRectangle = self.__buttons[buttonToDraw][constants.INDEX_OF_BUTTON_RECTANGLE]
        if self.__counterIfShipWasAdded[shipId] == constants.THIS_SHIP_WAS_ADDED:
            pygame.draw.rect(leftSideSectionSurface, constants.COLOR_GREY, buttonRectangle)
        elif self.selectedShip == shipId and self.selectedShipDirection == buttonNumberToDraw % constants.NUMBER_OF_BUTTONS_PER_ROW:
            pygame.draw.rect(leftSideSectionSurface, constants.COLOR_GREEN, buttonRectangle)
        else:
            pygame.draw.rect(leftSideSectionSurface, constants.COLOR_WHITE, buttonRectangle)

    def drawButtons(self):
        leftSideSectionSurface = pygame.Surface(self.__leftSectionOfScreen.size, pygame.SRCALPHA)

        for buttonNumberToDraw in range(constants.NUMBER_OF_SHIPS * constants.NUMBER_OF_BUTTONS_PER_ROW):
            buttonToDraw = dict(enumerate(self.__buttons))[buttonNumberToDraw]
            buttonRectangle = self.__buttons[buttonToDraw][constants.INDEX_OF_BUTTON_RECTANGLE]
            buttonRectangleSurface = self.__buttons[buttonToDraw][constants.INDEX_OF_BUTTON_SURFACE]
            textSurface = self.__buttons[buttonToDraw][constants.INDEX_OF_TEXT_SURFACE]
            
            shipId = buttonNumberToDraw // constants.NUMBER_OF_BUTTONS_PER_ROW
            self.colorButtonBackground(leftSideSectionSurface, shipId, buttonToDraw, buttonNumberToDraw)

            leftSideSectionSurface.blit(buttonRectangleSurface, buttonRectangle.topleft)
            leftSideSectionSurface.blit(textSurface, textSurface.get_rect(center=buttonRectangle.center).topleft)
            
        for shipButtonRow in range(constants.NUMBER_OF_SHIPS):
            if self.__counterIfShipWasAdded[shipButtonRow] == constants.THIS_SHIP_WAS_ADDED:
                leftSideSectionSurface.blit(self.__checkmarkIcon, constants.buttonsIconPositions[shipButtonRow])
            else:
                leftSideSectionSurface.blit(self.__pointerIcon, constants.buttonsIconPositions[shipButtonRow])

        self.__screenWindow.blit(leftSideSectionSurface, self.__leftSectionOfScreen.topleft)

    def drawBoard(self):
        for lineNumber, boardGridRow in enumerate(self.__gridRectangles):
            for columnNumber, positionOfRectangleToDraw in enumerate(boardGridRow):
                positionOfTileOnGrid = (columnNumber, lineNumber)
                typeOfShipOnTheTile = self.__services.checkIfTileIsOccupiedOnUserBoard(positionOfTileOnGrid)
                if typeOfShipOnTheTile == constants.EMPTY_TILE:
                    pygame.draw.rect(self.__screenWindow, constants.COLOR_LIGHT_BLUE, positionOfRectangleToDraw)
                else:
                    pygame.draw.rect(self.__screenWindow, constants.COLOR_OF_TILES_FOR_SHIP[typeOfShipOnTheTile], positionOfRectangleToDraw)


    def drawMenuTitle(self):
        self.__screenWindow.blit(self.__menuTitle, self.__menuTitle.get_rect(center=(self.__leftSectionOfScreen.centerx, self.__leftSectionOfScreen.top + constants.BOARD_BUILDER_TITLE_OFFSET)))


    # ---------------------------------------
    # LOGIC DOWN HERE
    # ---------------------------------------



    def getShipIdFromButtonName(self, buttonName):
        for shipId, shipName in enumerate(self.__buttons):
            if buttonName == shipName:
                return shipId // constants.NUMBER_OF_BUTTONS_PER_ROW

    def getShipDirectionFromButtonName(self, buttonName):
        for shipId, shipName in enumerate(self.__buttons):
            if buttonName == shipName:
                return shipId % constants.NUMBER_OF_BUTTONS_PER_ROW

    def onButtonPress(self, buttonName):
        self.selectedShip = self.getShipIdFromButtonName(buttonName)
        if self.__counterIfShipWasAdded[self.selectedShip] == constants.THIS_SHIP_WAS_ADDED:
            return
        self.selectedShipDirection = self.getShipDirectionFromButtonName(buttonName)

    def wasEveryShipAddedToBoard(self):
        for ship in self.__counterIfShipWasAdded:
            if ship == constants.THIS_SHIP_WAS_NOT_ADDED:
                return False
        return True

    def onTilePress(self, tileCoordinates):
        if self.selectedShip is None or self.selectedShipDirection is None:
            return
        self.selectedShipPosition = tileCoordinates
        addedShipToBoard = self.__services.addShipToUserBoard(self.selectedShip, self.selectedShipPosition, self.selectedShipDirection)
        if addedShipToBoard:
            self.__counterIfShipWasAdded[self.selectedShip] = constants.THIS_SHIP_WAS_ADDED
            self.selectedShip = None
            self.selectedShipDirection = None
            self.selectedShipPosition = None
            if self.wasEveryShipAddedToBoard():
                shouldEnterGame = True
                return shouldEnterGame

    # ---------------------------------------
    # EVENT HANDLERS DOWN HERE
    # ---------------------------------------


    @staticmethod
    def quitGame():
        pygame.quit()
        sys.exit()


    def checkIfClickedOnButton(self, clickEvent):
        for buttonName, buttonData in self.__buttons.items():
            buttonRectangle, _, _ = buttonData
            if buttonRectangle.collidepoint(clickEvent.pos):
                return buttonName
        return

    def checkIfClickedOnGrid(self, clickEvent):
        for row, rowRectangles in enumerate(self.__gridRectangles):
            for column, gridRectangles in enumerate(rowRectangles):
                if gridRectangles.collidepoint(clickEvent.pos):
                    return column, row
        return

    def findWhatObjectWasClicked(self, clickEvent):
        clickedOnButton = self.checkIfClickedOnButton(clickEvent)
        if clickedOnButton:
            return clickedOnButton
        clickedOnGrid = self.checkIfClickedOnGrid(clickEvent)
        if clickedOnGrid:
            return clickedOnGrid
        return


    def handleMouseClick(self, eventToCheck):
        objectThatUserClickedOn = self.findWhatObjectWasClicked(eventToCheck)
        if objectThatUserClickedOn:
            if type(objectThatUserClickedOn) == str:
                buttonName = objectThatUserClickedOn
                self.onButtonPress(buttonName)
            elif type(objectThatUserClickedOn) == tuple:
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
            shouldEnterGame = self.eventLoop()
            if shouldEnterGame:
                return
            self.drawLeftAndRightSectionsOfScreen()
            self.drawBoard()
            self.drawButtons()
            self.drawMenuTitle()

            pygame.display.flip()
