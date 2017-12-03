from PyQt5 import QtCore
from qtpy import QtWidgets

"""
interface : choose Mode
Easy Mode
Hard Mode
"""

class Ui_tictactoe(object):
    def setupUi(self,tictactoe):
        """ init tictactoe"""
        tictactoe.setObjectName("tictactoe")

        tictactoe.resize(627,470)
        sizePolicy=QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tictactoe.sizePolicy().hasHeightForWidth())
        tictactoe.setSizePolicy(sizePolicy)

        tictactoe.setMinimumSize(QtCore.QSize(627,470))
        tictactoe.setMaximumSize(QtCore.QSize(627,470))
        tictactoe.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        self.centralwidget=QtWidgets.QWidget(tictactoe)
        self.centralwidget.setObjectName("centralwidget")

        """
        put the board on the frame, central widget
        """
        self.frame=QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10,0,601,411))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")

        """
        tictactoe layout
        """
        self.gridLayout=QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.button1 = QtWidgets.QToolButton(self.frame)
        self.button1.setText("")
        self.button1.setIconSize(QtCore.QSize(128, 128))
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1,0,0)

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


