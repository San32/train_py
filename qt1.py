import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    """[summary]
    
    Arguments:
        QWidget {[type]} -- [description]
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """[summary]
        """

        self.resize(450, 400)
        btn = QPushButton('버튼', self)
        btn.move(30, 40)
        self.show()

APP = QApplication(sys.argv)
WIN = Exam()
sys.exit(APP.exec_())
