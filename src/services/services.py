from src import constants
from src.domain.board import Board
from src.domain.ship import Ship


class Services:
    def __init__(self):
        self.__userBoard = Board()
        self.__computerBoard = Board()

    def addShipToUserBoard(self, shipId, startingPosition: tuple, direction: int):
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
        areTilesEmpty = self.__userBoard.areTilesEmpty(startingPosition, endingPosition)
        if areTilesEmpty:
            shipToAdd = Ship(shipId)
            self.__userBoard.addShip(shipToAdd, startingPosition, endingPosition)
            return constants.THIS_SHIP_WAS_ADDED
        return None

    def checkIfTileIsOccupiedOnUserBoard(self, positionOfTile):
        return self.__userBoard.checkWhatTypeOfShipIsOnTheTile(positionOfTile)
