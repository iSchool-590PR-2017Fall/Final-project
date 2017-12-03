import os
import random
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Controller.Dialog import Dialog
from View.Board_GUI import Ui_tictactoe


class Game(QMainWindow, Ui_tictactoe):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Shows only the close button
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        xIconPath = os.path.join("../icon", "X.png")
        oIconPath = os.path.join("../icon", "O.png")

        self.xIcon = QIcon(xIconPath)
        self.oIcon = QIcon(oIconPath)

        # To make the icons appear in full color while disabled
        self.xIcon.addPixmap(QPixmap(xIconPath), QIcon.Disabled)
        self.oIcon.addPixmap(QPixmap(oIconPath), QIcon.Disabled)

        self.allButtons = self.frame.findChildren(QToolButton)
        self.availabeButtons = self.allButtons[:]
        """"
        board
        """
        self.board = list('---------')

        # connections
        for button in self.allButtons:
            button.clicked.connect(self.button_clicked)

        self.actionNew_Game.triggered.connect(self.new_game)
        self.action_Exit.triggered.connect(self.close)

        self.setFocus()  # sets the focus to the main window
        self.new_game()  # starts a new game

    def new_game(self):
        self.reset()

    def reset(self):
        self.frame.setEnabled(True)
        self.availabeButtons = self.allButtons[:]
        self.board = list('---------')
        self.statusbar.showMessage("You are X. You play first")

        for button in self.availabeButtons:
            button.setText("")
            button.setIcon(QIcon())
            button.setEnabled(True)

    def end_game(self, state):
        """Ends the game"""

        if state == 1:
            # the computer win the game
            Dialog(self, state).show()

            for button in self.availabeButtons:
                button.setEnabled(False)
            self.availabeButtons.clear()
            return True

        elif state == 2:
            # the computer lose the game
            Dialog(self, state).show()

            for button in self.availabeButtons:
                button.setEnabled(False)
            self.availabeButtons.clear()
            return True

        elif state == 3:
            # it's a draw
            Dialog(self, state).show()

            for button in self.allButtons:
                button.setEnabled(False)
            return True
        return False

    def button_clicked(self):
        button = self.sender()

        buttonName = str(button.objectName())
        buttonIndex = int(buttonName[-1]) - 1
        print(buttonIndex)

        """
        transfer index into board list position
        """
        self.board[buttonIndex] = 'X'

        # self.sounds["cross"].play()
        button.setText("1")
        button.setIcon(self.xIcon)
        button.setEnabled(False)
        self.availabeButtons.remove(button)

        winTest = self.check_win('X')
        if winTest != 2:
            if winTest == 1:
                self.end_game(2)
                return
            if winTest == -1:
                self.end_game(1)
                return

            self.end_game(3)
            return

        self.frame.setEnabled(False)
        # computer trail
        self.MC_round()

    def MC_round(self):
        buttonIndex = self.chooseRandomMoveFromList()
        # msg = "This game is headed towards a DRAW!"
        # if self.isWin(self.board) is True:
        #     msg = "Soon you are going to WIN :)"
        # if self.isWin(self.board) is False:
        #     msg =  "Soon you are going to LOOSE :("
        # self.statusbar.showMessage(msg)

        """

        player positions
        """
        self.board[buttonIndex] = '0'

        for buttonAvail in self.availabeButtons:
            buttonName = str(buttonAvail.objectName())
            buttonIndexNew = int(buttonName[-1]) - 1
            if buttonIndexNew == buttonIndex:
                button = buttonAvail
                # self.sounds["circle"].play()
                button.setText("2")
                button.setIcon(self.oIcon)
                button.setEnabled(False)
                self.availabeButtons.remove(button)
                break

        winTest = self.check_win('0')
        if winTest != 2:
            if winTest == 1:
                self.end_game(2)
                return
            if winTest == -1:
                self.end_game(1)
                return

            self.end_game(3)
            return

        self.frame.setEnabled(True)

    def isSpaceFree(self, board, move):
        return board[move] == ' '

    def chooseRandomMoveFromList(self):
        possibleMoves = []
        for i in range(len(self.board)):
            if self.board[i] == '-':
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def isWin(self, board):
        """
        GIven a board checks if it is in a winning state.
        Arguments:
              board: a list containing X,O or -.
        Return Value:
               True if board in winning state. Else False
        """
        #  check if any of the rows has winning combination
        for i in range(3):
            if (
                            len(set(board[i * 3:i * 3 + 3])) is 1 and
                            board[i * 3] is not '-'
            ):
                return True

        # check if any of the Columns has winning combination
        for i in range(3):
            if (
                            (board[i] is board[i + 3]) and
                            (board[i] is board[i + 6]) and
                            board[i] is not '-'
            ):
                return True

        # 2,4,6 and 0,4,8 cases
        # diagonal
        if (
                            board[0] is board[4] and
                            board[4] is board[8] and
                        board[4] is not '-'
        ):
            return True

        if (
                            board[2] is board[4] and
                            board[4] is board[6] and
                        board[4] is not '-'
        ):
            return True

        return False

    def check_win(self, player):
        if self.isWin(self.board):
            if player is 'X':
                return -1
            else:
                return 1

        c = self.board.count('-')
        if c is 0:
            return 0
        return 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    app.exec_()
