from PyQt5.QtWidgets import *


class Dialog(QDialog):

    def __init__(self, parent=None, state=None):
        super(Dialog, self).__init__(parent)
        self.setModal(True)

        layout = QGridLayout(self)

        pixmapLabel = QLabel("")
        label = QLabel("")
        okButton = QPushButton("Ok")

        if state == 1:
            label.setText("You have won")
            layout.addWidget(pixmapLabel, 0, 0)
            layout.addWidget(label, 0, 1)
            layout.addWidget(okButton, 1, 1)

        elif state == 2:
            label.setText("You have lost")
            layout.addWidget(pixmapLabel, 0, 0)
            layout.addWidget(label, 0, 1)
            layout.addWidget(okButton, 1, 1)

        else:
            label.setText("It's a draw")
            layout.addWidget(pixmapLabel, 0, 0)
            layout.addWidget(label, 0, 1)
            layout.addWidget(okButton, 1, 1)

        okButton.clicked.connect(self.hide)

