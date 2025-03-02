"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 02/03/2025.
    Version: 1.005
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from game import Game

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class GameWindow(QWidget):

    def __init__(self):
        super(GameWindow, self).__init__()
        self.setGeometry(500, 500, 800, 600)
        self.setWindowTitle("Tic-Tac-Toe")
        self.setWindowIcon(QIcon("ICON\icon.jpg"))

        self.newGameButton = QtWidgets.QPushButton(self)
        self.newGameButton.setObjectName("Button New Game")
        self.backToMainButton = QtWidgets.QPushButton(self)
        self.backToMainButton.setObjectName("Button Back To Main")

        self.listOfButtons = []
        self.game = Game()
        self.__initUi()

        # self.game.pl(self.newGameButton, self.backToMainButton)

    def __initUi(self):    #Function to init UI
        #TODO: Init main view of game

        self.__initCharButtons(4)

    def initMainView(self):
        #TODO: Init main view of game
        pass

    def __initCharButtons(self, buttonsInRow):       #Function to create buttons with chars
        buttonSize = 555//buttonsInRow
        for i in range(0, buttonsInRow*buttonsInRow):
            self.charButton = QtWidgets.QPushButton(self)
            self.charButton.setObjectName("Button " + str(i))
            self.listOfButtons.append(self.charButton)
            self.listOfButtons[i].setGeometry((i%buttonsInRow)*(buttonSize+5)+15, (i//buttonsInRow)*(buttonSize+5)+15, buttonSize, buttonSize)       #Size and position of char buttons
        self.game.initGameButtons(self.listOfButtons, buttonSize)

