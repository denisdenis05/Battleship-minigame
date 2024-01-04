from src.GUI.buildBoard import BuildBoardMenu
from src.GUI.startMenu import StartMenu
# from src.GUI.gameWindow import GameWindow

start = StartMenu()
start.gameLoop()

buildBoard = BuildBoardMenu()
buildBoard.gameLoop()

# actualGame = GameWindow()
# actualGame.gameLoop()
