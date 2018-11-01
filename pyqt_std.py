import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('라벨1', self)
        lbl.move(10, 10)

        lbl2 = QLabel('라벨2', self)
        lbl2.move(10, 40)

        lbl3 = QLabel('라벨3', self)
        lbl3.move(10, 60)

        self.setGeometry(50, 50, 300, 400)
        self.setWindowTitle('test app')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = win()
    sys.exit(app.exec_())