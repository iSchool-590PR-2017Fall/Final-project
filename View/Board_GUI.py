import random
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton, QApplication, QVBoxLayout, QFormLayout, QMainWindow, QWidget, QMessageBox
from PyQt5.QtCore import *
from qtpy import QtWidgets

# from Model.MonteCarlo_play import Game

"""
interface : choose Mode
Easy Mode
Hard Mode
"""


class First(QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        """
        cannot set a QLayout directly on QMainWindow
        """
        wid = QWidget(self)
        self.setCentralWidget(wid)

        self.b1 = QPushButton("battle")
        self.b2 = QPushButton("challenge")
        self.mainLayout = QVBoxLayout()
        wid.setLayout(self.mainLayout)

        self.mainLayout.addWidget(self.b1)
        self.mainLayout.addWidget(self.b2)

        """
        QWidget::setLayout: Attempting to set QLayout "" on First "", which already has a layout
        """
        # self.setLayout(self.mainLayout)
        self.setWindowTitle("Welcome!")

        self.b1.clicked.connect(self.on_boardButton_clicked)
        self.b2.clicked.connect(self.on_queryButton_clicked)

    def on_boardButton_clicked(self):
        msg = QMessageBox()
        msg.setText("Please choose the game mode!")
        msg.setWindowTitle("Enjoy the game with computer :)")
        msg.addButton(QPushButton('Easy Mode'), QMessageBox.YesRole)
        msg.addButton(QPushButton('Hard Mode'), QMessageBox.NoRole)
        msg.addButton(QPushButton('Med Mode'),QMessageBox.AcceptRole)
        msg.exec_()
        result = msg.buttonRole(msg.clickedButton())
        if result == QMessageBox.YesRole:
            print("this is easy")
            self.Easy_Mode()
        elif result == QMessageBox.NoRole:
            print("this is hard")
            self.Hard_Mode()
        else:
            self.Med_Mode()

    def Easy_Mode(self):
        """
               avoid dependency 
               """
        from Model.MonteCarlo_play import Game
        self.dialog = Game()
        self.dialog.show()

    def Hard_Mode(self):
        """

        haven't finished
        :return: 
        """
        from Model.Hard_MCplay import Hard_Test
        self.dialog1 = Hard_Test()
        self.dialog1.show()
        print("hard!!!")

    def Med_Mode(self):
        from Model.Med_MCplay import Med_Test
        self.dialog3=Med_Test()
        self.dialog3.show()

    def on_queryButton_clicked(self):
        self.dialog2=chalWindow()
        self.dialog2.show()
        # msg = QMessageBox()
        # buttonReply = msg.question(self, 'challenge', "beat with Monte Carlo Simulation!",
        #                            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # if buttonReply == QMessageBox.Yes:
        #     msg2 = QMessageBox()
        #     msg2.setText("What is the probability of the first player winning"
        #                  " in Tic Tac Toe as well as the second one winning")
        #     msg2.setWindowTitle("Try your best")
        #     msg2.addButton(QPushButton('50%'), QMessageBox.NoRole)
        #     msg2.addButton(QPushButton('60%'), QMessageBox.YesRole)
        #     msg2.addButton(QPushButton('30%'), QMessageBox.NoRole)
        #     result = msg2.exec_()
        #     if result == QMessageBox.YesRole:
        #         print("you are right")
        #     else:
        #         print("this is weird")


class BoardWindow(QMainWindow):
    def __init__(self, parent=None):
        super(BoardWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, tictactoe):
        """ init tictactoe"""
        tictactoe.setObjectName("tictactoe")

        tictactoe.resize(627, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tictactoe.sizePolicy().hasHeightForWidth())
        tictactoe.setSizePolicy(sizePolicy)

        tictactoe.setMinimumSize(QtCore.QSize(627, 470))
        tictactoe.setMaximumSize(QtCore.QSize(627, 470))
        tictactoe.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        self.centralwidget = QtWidgets.QWidget(tictactoe)
        self.centralwidget.setObjectName("centralwidget")

        """
        put the board on the frame, central widget
        """
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 601, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")

        """
        tictactoe layout
        """
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.button1 = QtWidgets.QToolButton(self.frame)
        self.button1.setText("")
        self.button1.setIconSize(QtCore.QSize(128, 128))
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 0, 0)

        self.button2 = QtWidgets.QToolButton(self.frame)
        self.button2.setText("")
        self.button2.setIconSize(QtCore.QSize(128, 128))
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 0, 1)

        self.button3 = QtWidgets.QToolButton(self.frame)
        self.button3.setText("")
        self.button3.setIconSize(QtCore.QSize(128, 128))
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 0, 2)

        self.button4 = QtWidgets.QToolButton(self.frame)
        self.button4.setText("")
        self.button4.setIconSize(QtCore.QSize(128, 128))
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 1, 0)

        self.button5 = QtWidgets.QToolButton(self.frame)
        self.button5.setText("")
        self.button5.setIconSize(QtCore.QSize(128, 128))
        self.button5.setObjectName("button5")
        self.gridLayout.addWidget(self.button5, 1, 1)

        self.button6 = QtWidgets.QToolButton(self.frame)
        self.button6.setText("")
        self.button6.setIconSize(QtCore.QSize(128, 128))
        self.button6.setObjectName("button6")
        self.gridLayout.addWidget(self.button6, 1, 2)

        self.button7 = QtWidgets.QToolButton(self.frame)
        self.button7.setText("")
        self.button7.setIconSize(QtCore.QSize(128, 128))
        self.button7.setObjectName("button7")
        self.gridLayout.addWidget(self.button7, 2, 0)

        self.button8 = QtWidgets.QToolButton(self.frame)
        self.button8.setText("")
        self.button8.setIconSize(QtCore.QSize(128, 128))
        self.button8.setObjectName("button8")
        self.gridLayout.addWidget(self.button8, 2, 1)

        self.button9 = QtWidgets.QToolButton(self.frame)
        self.button9.setText("")
        self.button9.setIconSize(QtCore.QSize(128, 128))
        self.button9.setObjectName("button9")
        self.gridLayout.addWidget(self.button9, 2, 2)
        tictactoe.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(tictactoe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 22))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        tictactoe.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(tictactoe)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("You are X AND Computer is 0. You play first")
        tictactoe.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(tictactoe)
        self.toolBar.setObjectName("toolBar")
        tictactoe.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionNew_Game = QtWidgets.QAction(tictactoe)
        self.actionNew_Game.setObjectName("actionNew_Game")

        self.action_Exit = QtWidgets.QAction(tictactoe)
        self.action_Exit.setObjectName("action_Exit")

        self.menuNew.addAction(self.actionNew_Game)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.action_Exit)
        self.menuNew.addSeparator()
        self.menubar.addAction(self.menuNew.menuAction())
        self.toolBar.addAction(self.actionNew_Game)

        self.retranslateUi(tictactoe)
        """
        connect with slot
        """
        QtCore.QMetaObject.connectSlotsByName(tictactoe)

    def retranslateUi(self, tictactoe):
        _translate = QtCore.QCoreApplication.translate
        tictactoe.setWindowTitle(_translate("tictactoe", "Tic Tac Toe"))
        self.menuNew.setTitle(_translate("tictactoe", "New"))
        self.toolBar.setWindowTitle(_translate("tictactoe", "toolBar"))
        self.actionNew_Game.setText(_translate("tictactoe", "New Game"))
        self.action_Exit.setText(_translate("tictactoe", "Exit"))


class chalWindow(QMainWindow):
    def __init__(self, parent=None):
        super(chalWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, challenge):
        """ init challenge"""
        challenge.setObjectName("challenge")

        challenge.resize(627, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(challenge.sizePolicy().hasHeightForWidth())
        challenge.setSizePolicy(sizePolicy)

        challenge.setMinimumSize(QtCore.QSize(627, 470))
        challenge.setMaximumSize(QtCore.QSize(627, 470))
        challenge.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        self.centralwidget = QtWidgets.QWidget(challenge)
        self.centralwidget.setObjectName("centralwidget")

        """
        put the board on the frame, central widget
        """
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 601, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")

        """
        challenge layout
        """
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.button1 = QtWidgets.QToolButton(self.frame)
        self.button1.setText("computer1")
        self.button1.setIconSize(QtCore.QSize(192, 40))
        self.button1.setObjectName("computer1")
        self.gridLayout.addWidget(self.button1, 0, 0)

        self.button2 = QtWidgets.QToolButton(self.frame)
        self.button2.setText("computer2")
        self.button2.setIconSize(QtCore.QSize(192, 40))
        self.button2.setObjectName("computer2")
        self.gridLayout.addWidget(self.button2, 0, 1)

        self.button3 = QtWidgets.QToolButton(self.frame)
        self.button3.setText("Hard")
        self.button3.setIconSize(QtCore.QSize(192, 40))
        self.button3.setObjectName("Hard")
        self.gridLayout.addWidget(self.button3, 1, 0)

        self.button4 = QtWidgets.QToolButton(self.frame)
        self.button4.setText("Hard")
        self.button4.setIconSize(QtCore.QSize(192, 40))
        self.button4.setObjectName("Hard")
        self.gridLayout.addWidget(self.button4, 1, 1)

        self.button5 = QtWidgets.QToolButton(self.frame)
        self.button5.setText("Hard")
        self.button5.setIconSize(QtCore.QSize(192, 40))
        self.button5.setObjectName("Hard")
        self.gridLayout.addWidget(self.button5, 2, 0)

        self.button6 = QtWidgets.QToolButton(self.frame)
        self.button6.setText("Med")
        self.button6.setIconSize(QtCore.QSize(192, 40))
        self.button6.setObjectName("Med")
        self.gridLayout.addWidget(self.button6, 2, 1)

        self.button7 = QtWidgets.QToolButton(self.frame)
        self.button7.setText("Hard")
        self.button7.setIconSize(QtCore.QSize(192, 40))
        self.button7.setObjectName("Hard")
        self.gridLayout.addWidget(self.button7, 3, 0)

        self.button8 = QtWidgets.QToolButton(self.frame)
        self.button8.setText("Easy")
        self.button8.setIconSize(QtCore.QSize(192, 40))
        self.button8.setObjectName("Easy")
        self.gridLayout.addWidget(self.button8, 3, 1)

        self.button9 = QtWidgets.QToolButton(self.frame)
        self.button9.setText("Med")
        self.button9.setIconSize(QtCore.QSize(192, 40))
        self.button9.setObjectName("Med")
        self.gridLayout.addWidget(self.button9, 4, 0)

        self.button10 = QtWidgets.QToolButton(self.frame)
        self.button10.setText("Hard")
        self.button10.setIconSize(QtCore.QSize(192, 40))
        self.button10.setObjectName("Hard")
        self.gridLayout.addWidget(self.button10, 4, 1)

        self.button11 = QtWidgets.QToolButton(self.frame)
        self.button11.setText("Med")
        self.button11.setIconSize(QtCore.QSize(192, 40))
        self.button11.setObjectName("Med")
        self.gridLayout.addWidget(self.button11, 5, 0)

        self.button12 = QtWidgets.QToolButton(self.frame)
        self.button12.setText("Med")
        self.button12.setIconSize(QtCore.QSize(192, 40))
        self.button12.setObjectName("Med")
        self.gridLayout.addWidget(self.button12, 5, 1)

        self.button13 = QtWidgets.QToolButton(self.frame)
        self.button13.setText("Med")
        self.button13.setIconSize(QtCore.QSize(192, 40))
        self.button13.setObjectName("Med")
        self.gridLayout.addWidget(self.button13, 6, 0)

        self.button14 = QtWidgets.QToolButton(self.frame)
        self.button14.setText("Easy")
        self.button14.setIconSize(QtCore.QSize(192, 40))
        self.button14.setObjectName("Easy")
        self.gridLayout.addWidget(self.button14, 6, 1)

        self.button15 = QtWidgets.QToolButton(self.frame)
        self.button15.setText("Easy")
        self.button15.setIconSize(QtCore.QSize(192, 40))
        self.button15.setObjectName("Easy")
        self.gridLayout.addWidget(self.button15, 7, 0)

        self.button16 = QtWidgets.QToolButton(self.frame)
        self.button16.setText("Hard")
        self.button16.setIconSize(QtCore.QSize(192, 40))
        self.button16.setObjectName("Hard")
        self.gridLayout.addWidget(self.button16, 7, 1)

        self.button17 = QtWidgets.QToolButton(self.frame)
        self.button17.setText("Easy")
        self.button17.setIconSize(QtCore.QSize(192, 40))
        self.button17.setObjectName("Easy")
        self.gridLayout.addWidget(self.button17, 8, 0)

        self.button18 = QtWidgets.QToolButton(self.frame)
        self.button18.setText("Med")
        self.button18.setIconSize(QtCore.QSize(192, 40))
        self.button18.setObjectName("Med")
        self.gridLayout.addWidget(self.button18, 8, 1)

        self.button19 = QtWidgets.QToolButton(self.frame)
        self.button19.setText("Easy")
        self.button19.setIconSize(QtCore.QSize(192, 40))
        self.button19.setObjectName("Easy")
        self.gridLayout.addWidget(self.button19, 9, 0)

        self.button20 = QtWidgets.QToolButton(self.frame)
        self.button20.setText("Hard")
        self.button20.setIconSize(QtCore.QSize(192, 40))
        self.button20.setObjectName("Hard")
        self.gridLayout.addWidget(self.button20, 9, 1)
        challenge.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(challenge)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 22))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        challenge.setMenuBar(self.menubar)

        QtCore.QMetaObject.connectSlotsByName(challenge)
        self.statusbar = QtWidgets.QStatusBar(challenge)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("Please choose the mode for each player")
        challenge.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(challenge)
        self.toolBar.setObjectName("toolBar")
        challenge.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionNew_Game = QtWidgets.QAction(challenge)
        self.actionNew_Game.setObjectName("actionNew_Game")

        self.action_Exit = QtWidgets.QAction(challenge)
        self.action_Exit.setObjectName("action_Exit")

        self.menuNew.addAction(self.actionNew_Game)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.action_Exit)
        self.menuNew.addSeparator()
        self.menubar.addAction(self.menuNew.menuAction())
        self.toolBar.addAction(self.actionNew_Game)

        self.retranslateUi(challenge)
        """
        connect with slot
        """
        QtCore.QMetaObject.connectSlotsByName(challenge)

    def retranslateUi(self, challenge):
        _translate = QtCore.QCoreApplication.translate
        challenge.setWindowTitle(_translate("challenge", "Tic Tac Toe"))
        self.menuNew.setTitle(_translate("challenge", "New"))
        self.toolBar.setWindowTitle(_translate("challenge", "toolBar"))
        self.actionNew_Game.setText(_translate("challenge", "New Game"))
        self.action_Exit.setText(_translate("challenge", "Exit"))


def main():
    app = QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

