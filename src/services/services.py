from src import constants
from src.domain.board import Board
from src.domain.ship import Ship
from random import randint


class Services:
    def __init__(self):
        self.__userBoard = Board()
        self.__computerBoard = Board()
        self.__computerHitsAI = []

    def addShipToUserBoard(self, shipId, startingPosition: tuple, direction: int):
        return self.addShipToBoard(shipId, startingPosition, direction, self.__userBoard)

    @staticmethod
    def addShipToBoard(shipId, startingPosition: tuple, direction: int, board: Board):
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

    @staticmethod
    def addTwoTuples(firstTupleToAdd, secondTupleToAdd):
        resultTuple = tuple(elementToAddFromFirstTuple + elementToAddFromSecondTuple
                            for elementToAddFromFirstTuple, elementToAddFromSecondTuple in zip(firstTupleToAdd, secondTupleToAdd))
        return resultTuple

    @staticmethod
    def notOutsideBoard(neighboringTile):
        column = neighboringTile[constants.INDEX_OF_COLUMN_COORDINATES]
        line = neighboringTile[constants.INDEX_OF_LINE_COORDINATES]
        return constants.DIMENSION_OF_BOARD > column >= constants.MINIMUM_POSITION_ON_BOARD and constants.DIMENSION_OF_BOARD > line >= constants.MINIMUM_POSITION_ON_BOARD

    def handleHitStackAI(self, positionThatWasHit):
        if self.checkIfTileIsOccupiedOnUserBoard(positionThatWasHit) != constants.EMPTY_TILE:
            neighboringTiles = [self.addTwoTuples(positionThatWasHit, constants.COORDINATES_OF_NORTH_TILE),
                                self.addTwoTuples(positionThatWasHit, constants.COORDINATES_OF_SOUTH_TILE),
                                self.addTwoTuples(positionThatWasHit, constants.COORDINATES_OF_EAST_TILE),
                                self.addTwoTuples(positionThatWasHit, constants.COORDINATES_OF_WEST_TILE)]
            for neighboringTile in neighboringTiles:
                if self.notOutsideBoard(neighboringTile) and self.__userBoard.checkIfTileWasHit(neighboringTile) == constants.EMPTY_TILE:
                    self.__computerHitsAI.append(neighboringTile)


    def hitRandomTileAI(self):
        hitTile = False
        while not hitTile:
            line = randint(0, 9)
            column = randint(0, 9)
            tileCoordinatesToHit = (line, column)
            if self.__userBoard.checkIfTileWasHit(tileCoordinatesToHit) == constants.EMPTY_TILE:
                self.__userBoard.hitTile(tileCoordinatesToHit)
                self.handleHitStackAI(tileCoordinatesToHit)
                return self.checkIfTileIsOccupiedOnUserBoard(tileCoordinatesToHit)

    def hitTileNearOtherSuccessfullyHitTiles(self):
        tileCoordinatesToHit = self.__computerHitsAI[constants.INDEX_OF_FIRST_TILE_THAT_SHOULD_BE_HIT_BY_AI]
        if self.__userBoard.checkIfTileWasHit(tileCoordinatesToHit) == constants.EMPTY_TILE:
            self.__userBoard.hitTile(tileCoordinatesToHit)
            self.__computerHitsAI.pop(constants.INDEX_OF_FIRST_TILE_THAT_SHOULD_BE_HIT_BY_AI)
            self.handleHitStackAI(tileCoordinatesToHit)
            return self.checkIfTileIsOccupiedOnUserBoard(tileCoordinatesToHit)
        else:
            self.__computerHitsAI.pop(constants.INDEX_OF_FIRST_TILE_THAT_SHOULD_BE_HIT_BY_AI)
            return self.hitTileNearOtherSuccessfullyHitTiles()


    def handleHitOnUserBoard(self):
        if len(self.__computerHitsAI) == 0:
            return self.hitRandomTileAI()
        else:
            return self.hitTileNearOtherSuccessfullyHitTiles()



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
        if self.__computerBoard.isGameOver():
            return constants.USER_WON
        if self.__userBoard.isGameOver():
            return constants.COMPUTER_WON
        return
