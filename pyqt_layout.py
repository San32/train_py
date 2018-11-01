import sys
from PyQt5.QtWidgets import (QWidget ,QLabel, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLCDNumber, QMainWindow, QFrame)

station_name = ["노포", "범어사", "남산", "두실", "구서", "장전", "부산대", "온천장", "명륜", "동래", "교대"]
station_btn = []

class Exam(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # okBtn = QPushButton("ok")
        # cancelBtn = QPushButton("cancel")

        for name in station_name:
            station_btn.append(QPushButton(name))

        hbox = QHBoxLayout()
        hbox.addStretch(1)

        for btn in station_btn:
            hbox.addWidget(btn)

        # hbox.addWidget(okBtn)
        # hbox.addWidget(cancelBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("layout")
        
        station_btn[1].setStyleSheet("background-color: rgb(255, 0, 0);")

        self.show()

class station_panel(QFrame):
    """make starion panel
    
    Arguments:
        QWidget {[type]} -- [description]
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

        self.initUI()


    def initUI(self):
        lcd_up_1 = QLCDNumber(4)
        lcd_up_2 = QLCDNumber(4)
        lcd_up_3 = QLCDNumber(4)

        # lcd_up_1.setStyleSheet("visible : false")

        hbox_up = QHBoxLayout()
        hbox_up.addWidget(lcd_up_1)
        hbox_up.addWidget(lcd_up_2)
        hbox_up.addWidget(lcd_up_3)


        lcd_dn_1 = QLCDNumber(4)
        lcd_dn_2 = QLCDNumber(4)
        lcd_dn_3 = QLCDNumber(4)

        hbox_dn = QHBoxLayout()
        hbox_dn.addWidget(lcd_dn_1)
        hbox_dn.addWidget(lcd_dn_2)
        hbox_dn.addWidget(lcd_dn_3)


        btn_station = QPushButton(self.name)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn_station)
        hbox.addStretch(1)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox_up)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox_dn)

        btn_station.setStyleSheet("background-color: rgb(255, 0, 0);")

        self.setLayout(vbox)
        self.show()


class line_map(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        p1 = station_panel('p1')
        p2 = station_panel('p2')

        hbox = QHBoxLayout()
        hbox.addWidget(p1)
        hbox.addWidget(p2)
        
        self.setStyleSheet("QLineEdit { background-color: yellow }");

        self.setLayout(hbox)
        self.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ex = station_panel('qqqq')
    # ex2 = station_panel('fffff')

    m = line_map()
    sys.exit(app.exec_())
