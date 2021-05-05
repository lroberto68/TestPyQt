from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.pbClick = QPushButton("Click", self)
        self.pbClick.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.pbClick.setText("Clicked")
        self.setEnabled(False)
        self.setWindowTitle(self.windowTitle() + " one time")
        print (self.pbClick.text)
        print(dir(MainWindow))
        


app = QApplication(sys.argv)
win = MainWindow()
win.show()

app.exec_()
