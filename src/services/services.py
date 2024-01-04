from src import constants
from src.domain.board import Board
from src.domain.ship import Ship
from random import randint


class Services:
    def __init__(self):
        self.__userBoard = Board()
        self.__computerBoard = Board()

    def addShipToUserBoard(self, shipId, startingPosition: tuple, direction: int):
        return self.addShipToBoard(shipId, startingPosition, direction, self.__userBoard)

    def addShipToBoard(self, shipId, startingPosition: tuple, direction: int, board: Board):
        shipLength = constants.LENGTH_OF_SHIPS[shipId]
        startingPositionLine = startingPosition[constants.INDEX_OF_LINE_COORDINATES]
        startingPositionColumn = startingPosition[constants.INDEX_OF_COLUMN_COORDINATES]
        if direction == constants.SHIP_IS_HORIZONTAL:
            endingPositionLine = startingPositionLine
            endingPositionColumn = startingPositionColumn + shipLength - 1
        else:
            endingPositionLine = startingPositionLine + shipLength - 1
            endingPositionColumn = startingPositionColumn
        endingPosition = (endingPositionColumn, endingPositionLine)
        areTilesEmpty = board.areTilesEmpty(startingPosition, endingPosition)
        if areTilesEmpty:
            shipToAdd = Ship(shipId)
            board.addShip(shipToAdd, startingPosition, endingPosition)
            return constants.THIS_SHIP_WAS_ADDED
        return None

    def checkIfTileIsOccupiedOnUserBoard(self, positionOfTile):
        return self.__userBoard.checkWhatTypeOfShipIsOnTheTile(positionOfTile)

    def checkIfTileIsOccupiedOnComputerBoard(self, positionOfTile):
        return self.__computerBoard.checkWhatTypeOfShipIsOnTheTile(positionOfTile)

    def addShipToComputerBoard(self, shipId, startingPosition: tuple, direction: int):
        return self.addShipToBoard(shipId, startingPosition, direction, self.__computerBoard)

    def buildBoardForComputer(self):
        shipId = 0
        while shipId <= 4:
            line = randint(0, 9)
            column = randint(0, 9)
            direction = randint(0, 1)
            startingPosition = (line, column)
            addedToComputerBoard = self.addShipToComputerBoard(shipId, startingPosition, direction)
            if addedToComputerBoard:
                shipId = shipId + 1


    def handleHitOnUserBoard(self):
        hitTile = False
        while not hitTile:
            line = randint(0, 9)
            column = randint(0, 9)
            positionOfTile = (line, column)
            if self.__userBoard.checkIfTileWasHit(positionOfTile) == constants.EMPTY_TILE:
                self.__userBoard.hitTile(positionOfTile)
                hitTile = True
                return self.checkIfTileIsOccupiedOnUserBoard(positionOfTile)


    def checkIfTileIsHitOnComputerBoard(self, positionOfTile):
        return self.__computerBoard.checkIfTileWasHit(positionOfTile)

    def checkIfTileIsHitOnUserBoard(self, positionOfTile):
        return self.__userBoard.checkIfTileWasHit(positionOfTile)

    def handleHit(self, positionOfTile):
        if self.__computerBoard.checkIfTileWasHit(positionOfTile) == constants.HIT_TILE:
            return
        shipHitByUser = self.__computerBoard.hitTile(positionOfTile)
        shipHitByComputer = self.handleHitOnUserBoard()
        shipsHit = (shipHitByUser, shipHitByComputer)
        return shipsHit


    def checkIfGameEnded(self):
        if self.__userBoard.isGameOver():
            return constants.COMPUTER_WON
        elif self.__computerBoard.isGameOver():
            return constants.USER_WON
        return
