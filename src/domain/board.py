from src import constants


class Board:
    def __init__(self):
        self.__boardTiles = [[constants.EMPTY_TILE] * constants.DIMENSION_OF_BOARD for boardLine in range(
            constants.DIMENSION_OF_BOARD)]
        self.__shipOnBoard = [[constants.EMPTY_TILE] * constants.DIMENSION_OF_BOARD for boardLine in range(
            constants.DIMENSION_OF_BOARD)]
        self.__addedShips = {}

    def areTilesEmpty(self, tileToStartFrom: tuple, tileToEndTo: tuple) -> bool:
        lineOfStartingTile = tileToStartFrom[constants.INDEX_OF_LINE_COORDINATES]
        columnOfStartingTile = tileToStartFrom[constants.INDEX_OF_COLUMN_COORDINATES]
        lineOfEndingTile = tileToEndTo[constants.INDEX_OF_LINE_COORDINATES]
        columnOfEndingTile = tileToEndTo[constants.INDEX_OF_COLUMN_COORDINATES]
        if lineOfEndingTile != lineOfStartingTile and columnOfEndingTile != columnOfStartingTile:
            return False
        if lineOfEndingTile == lineOfStartingTile:
            if columnOfEndingTile >= constants.DIMENSION_OF_BOARD:
                return False
            for columnIndexOfTile in range(columnOfStartingTile, columnOfEndingTile + constants.VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED):
                if self.__shipOnBoard[lineOfEndingTile][columnIndexOfTile] != constants.EMPTY_TILE:
                    return False
        else:
            if lineOfEndingTile >= constants.DIMENSION_OF_BOARD:
                return False
            for lineIndexOfTile in range(lineOfStartingTile, lineOfEndingTile + constants.VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED):
                if self.__shipOnBoard[lineIndexOfTile][columnOfEndingTile] != constants.EMPTY_TILE:
                    return False
        return True


    def addShip(self, shipToAdd, tileToStartFrom: tuple, tileToEndTo: tuple):
        lineOfStartingTile = tileToStartFrom[constants.INDEX_OF_LINE_COORDINATES]
        columnOfStartingTile = tileToStartFrom[constants.INDEX_OF_COLUMN_COORDINATES]
        lineOfEndingTile = tileToEndTo[constants.INDEX_OF_LINE_COORDINATES]
        columnOfEndingTile = tileToEndTo[constants.INDEX_OF_COLUMN_COORDINATES]
        shipId = shipToAdd.getId()
        print(shipId)
        if lineOfEndingTile == lineOfStartingTile:
            for columnIndexOfTile in range(columnOfStartingTile, columnOfEndingTile + constants.VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED):
                self.__shipOnBoard[lineOfEndingTile][columnIndexOfTile] = shipId
        else:
            for lineIndexOfTile in range(lineOfStartingTile, lineOfEndingTile + constants.VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED):
                self.__shipOnBoard[lineIndexOfTile][columnOfEndingTile] = shipId
        print(self.__shipOnBoard)
        self.__addedShips[shipId] = shipToAdd

    def checkWhatTypeOfShipIsOnTheTile(self, positionOfTile: tuple) -> int:
        lineOfTile = positionOfTile[constants.INDEX_OF_LINE_COORDINATES]
        columnOfTile = positionOfTile[constants.INDEX_OF_COLUMN_COORDINATES]
        return self.__shipOnBoard[lineOfTile][columnOfTile]

    def isGameOver(self):
        for ship in self.__addedShips:
            if self.__addedShips[ship].getHits() != self.__addedShips[ship].getLength():
                return False
        return True
