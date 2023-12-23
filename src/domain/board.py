from src import constants


class Board:
    def __init__(self):
        self.__boardTiles = [[constants.EMPTY_TILE] * constants.DIMENSION_OF_BOARD for boardLine in range(
            constants.DIMENSION_OF_BOARD)]
        self.__shipOnBoard = [[constants.EMPTY_TILE] * constants.DIMENSION_OF_BOARD for boardLine in range(
            constants.DIMENSION_OF_BOARD)]
        self.__addedShips = {}

    def areTilesEmpty(self, tileToStartFrom: tuple, tileToEndTo: tuple) -> bool:
        lineOfFirstTile = tileToStartFrom[constants.INDEX_OF_LINE_COORDINATES]
        columnOfFirstTile = tileToStartFrom[constants.INDEX_OF_COLUMN_COORDINATES]
        lineOfSecondTile = tileToEndTo[constants.INDEX_OF_LINE_COORDINATES]
        columnOfSecondTile = tileToEndTo[constants.INDEX_OF_COLUMN_COORDINATES]
        if lineOfSecondTile != lineOfFirstTile and columnOfSecondTile != columnOfFirstTile:
            return False
        if lineOfSecondTile == lineOfFirstTile:
            for columnIndexOfTile in range(columnOfFirstTile, columnOfSecondTile + constants.VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED):
                if self.__shipOnBoard[lineOfSecondTile][columnIndexOfTile] != constants.EMPTY_TILE:
                    return False
        else:
            for lineIndexOfTile in range(lineOfFirstTile, lineOfSecondTile + constants.VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED):
                if self.__shipOnBoard[lineIndexOfTile][columnOfSecondTile] != constants.EMPTY_TILE:
                    return False
        return True


    def addShip(self, shipToAdd, startingPosition: tuple, direction):
        pass

    def isGameOver(self):
        for ship in self.__addedShips:
            if self.__addedShips[ship].getHits() != self.__addedShips[ship].getLength():
                return False
        return True
