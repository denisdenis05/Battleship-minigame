import texttable

from src import constants


class Board:
    def __init__(self):
        self.__boardTiles = [[constants.EMPTY_TILE] * constants.DIMENSION_OF_BOARD for boardLine in range(
            constants.DIMENSION_OF_BOARD)]
        self.__shipsOnBoard = [[constants.EMPTY_TILE] * constants.DIMENSION_OF_BOARD for boardLine in range(
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
                if self.__shipsOnBoard[lineOfEndingTile][columnIndexOfTile] != constants.EMPTY_TILE:
                    return False
        else:
            if lineOfEndingTile >= constants.DIMENSION_OF_BOARD:
                return False
            for lineIndexOfTile in range(lineOfStartingTile, lineOfEndingTile + constants.VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED):
                if self.__shipsOnBoard[lineIndexOfTile][columnOfEndingTile] != constants.EMPTY_TILE:
                    return False
        return True


    def addShip(self, shipToAdd, tileToStartFrom: tuple, tileToEndTo: tuple):
        lineOfStartingTile = tileToStartFrom[constants.INDEX_OF_LINE_COORDINATES]
        columnOfStartingTile = tileToStartFrom[constants.INDEX_OF_COLUMN_COORDINATES]
        lineOfEndingTile = tileToEndTo[constants.INDEX_OF_LINE_COORDINATES]
        columnOfEndingTile = tileToEndTo[constants.INDEX_OF_COLUMN_COORDINATES]
        shipId = shipToAdd.getId()
        if lineOfEndingTile == lineOfStartingTile:
            for columnIndexOfTile in range(columnOfStartingTile, columnOfEndingTile + constants.VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED):
                self.__shipsOnBoard[lineOfEndingTile][columnIndexOfTile] = shipId
        else:
            for lineIndexOfTile in range(lineOfStartingTile, lineOfEndingTile + constants.VALUE_TO_ADD_SO_LAST_ELEMENT_IS_CONSIDERED):
                self.__shipsOnBoard[lineIndexOfTile][columnOfEndingTile] = shipId
        self.__addedShips[shipId] = shipToAdd

    def checkWhatTypeOfShipIsOnTheTile(self, positionOfTile: tuple) -> int:
        lineOfTile = positionOfTile[constants.INDEX_OF_LINE_COORDINATES]
        columnOfTile = positionOfTile[constants.INDEX_OF_COLUMN_COORDINATES]
        return self.__shipsOnBoard[lineOfTile][columnOfTile]


    def checkIfTileWasHit(self, positionOfTile: tuple) -> int:
        lineOfTile = positionOfTile[constants.INDEX_OF_LINE_COORDINATES]
        columnOfTile = positionOfTile[constants.INDEX_OF_COLUMN_COORDINATES]
        return self.__boardTiles[lineOfTile][columnOfTile]

    def hitTile(self, positionOfTile):
        lineOfTile = positionOfTile[constants.INDEX_OF_LINE_COORDINATES]
        columnOfTile = positionOfTile[constants.INDEX_OF_COLUMN_COORDINATES]
        self.__boardTiles[lineOfTile][columnOfTile] = constants.HIT_TILE
        idOfShipThatWasHit = self.__shipsOnBoard[lineOfTile][columnOfTile]
        if idOfShipThatWasHit != constants.EMPTY_TILE:
            self.__addedShips[idOfShipThatWasHit].addHit()
            return idOfShipThatWasHit
        else:
            return constants.EMPTY_TILE

    def isGameOver(self):
        for ship in self.__addedShips:
            if self.__addedShips[ship].getHits() != self.__addedShips[ship].getLength():
                return False
        return True

    def __str__(self):
        displayBoard = texttable.Texttable()
        first_row = [' ']
        for column in range(constants.DIMENSION_OF_BOARD):
            first_row.append(chr(ord('A') + column))
        displayBoard.add_row(first_row)

        for index in range(constants.DIMENSION_OF_BOARD):
            row = [str(index + 1)]
            rowContent = []
            for indexOfColumn in range(constants.DIMENSION_OF_BOARD):
                if self.__boardTiles[index][indexOfColumn] != constants.EMPTY_TILE:
                    rowContent.append("*")
                elif self.__shipsOnBoard[index][indexOfColumn] == constants.EMPTY_TILE:
                    rowContent.append(" ")
                else:
                    rowContent.append(self.__shipsOnBoard[index][indexOfColumn])
            row.extend(rowContent)
            displayBoard.add_row(row)

        return displayBoard.draw()

