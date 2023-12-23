from src import constants


class Ship:
    def __init__(self, idOfShip: int):
        self.__idOfShip = idOfShip
        self.__hits = constants.STARTING_NUMBER_OF_HITS

    def getName(self):
        return constants.NAME_OF_SHIPS[self.__idOfShip]

    def getLength(self):
        return constants.LENGTH_OF_SHIPS[self.__idOfShip]

    def getHits(self):
        return self.__hits

    def addHit(self):
        self.__hits += 1

    def removeHit(self):
        self.__hits -= 1
