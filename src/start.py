from src.GUI.buildBoard import BuildBoardMenu
from src.GUI.endingScreen import EndingMenu
from src.GUI.playingMenu import GameWindow
from src.GUI.startMenu import StartMenu
from src.services.services import Services




def main():
    services = Services()

    start = StartMenu()
    start.gameLoop()


    services.buildBoardForComputer()
    buildBoard = BuildBoardMenu(services)
    buildBoard.gameLoop()

    actualGame = GameWindow(services)
    gameResult = actualGame.gameLoop()

    endingScreen = EndingMenu(gameResult)
    endingScreen.gameLoop()


main()
