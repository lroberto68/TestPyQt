from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
import sys


class Win(QMainWindow):
    def __init__(self):
        super(Win, self).__init__()

        self.button_checked=True

        self.setWindowTitle("My App")

        self.pbClick = QPushButton("ciao", self)
        self.pbClick.setCheckable(True)
        self.pbClick.clicked.connect(self.the_button_was_toggled)
        self.pbClick.setChecked(self.button_checked)

        self.label = QLabel()

    def the_button_was_toggled(self, checked):
        self.button_checked=checked
        print(self.button_checked)


app = QApplication(sys.argv)
window = Win()
window.show()
app.exec_()
