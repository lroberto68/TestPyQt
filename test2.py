from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QComboBox, QLineEdit, QListWidget
from PyQt5.QtCore import Qt
import sys
from random import choice


class MainWindow(QMainWindow):
    window_titles = [
        'finestra1',
        'finestra2',
        'finestra3',
        'finito'
    ]

    def __init__(self):
        super(MainWindow, self).__init__()

        self.num_time = 0
        print("ciao a tutti")

        self.setWindowTitle("My app")
        self.windowTitleChanged.connect(self.the_window_title_is_changed)
        self.setGeometry(0, 0, 400, 400)

        self.cmBox = QComboBox(self)
        self.cmBox.move(30, 100)
        self.cmBox.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.cmBox.addItems(['Roberto', 'Federica', 'Roberta'])

        self.lsWidget = QListWidget(self)
        self.lsWidget.move(30, 150)
        self.lsWidget.addItems(self.window_titles)
        self.lsWidget.adjustSize()

        self.pbClick = QPushButton("Click", self)
        self.pbClick.clicked.connect(self.window_title_change)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignVCenter)
        self.label.move(30, 20)

        self.chBox = QCheckBox("Test", self)
        self.chBox.setTristate(True)
        self.chBox.setChecked(Qt.PartiallyChecked)
        self.chBox.move(30, 60)
        self.chBox.stateChanged.connect(self.show_state)

        self.lnEdit = QLineEdit(self)
        self.lnEdit.move(200, 100)
        self.lnEdit.setText(self.cmBox.currentText())

        self.cmBox.currentTextChanged.connect(self.lnEdit.setText)
        self.lsWidget.currentTextChanged.connect(self.text_change)

    def window_title_change(self):
        new_window_title = choice(self.window_titles)
        self.setWindowTitle(new_window_title)
        self.cmBox.addItem(self.lnEdit.text())

    def the_window_title_is_changed(self, window_title):
        self.num_time += 1
        print(f"The new window title is {window_title}, cambiato {self.num_time} volte")
        self.label.setText(f"{self.num_time}")

        if window_title == 'finito':
            self.pbClick.setEnabled(False)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)

    def text_change(self,s):
        print(f"Valore = {s}")

app = QApplication(sys.argv)
win = MainWindow()
win.show()

app.exec_()
