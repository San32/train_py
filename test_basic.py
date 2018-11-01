# coding: utf-8
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
 
class Form(QtWidgets.QDialog):
    """[summary]
    
    Arguments:
        QtWidgets {[type]} -- [description]
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("basic.ui", self)
        self.ui.show()
 
    @pyqtSlot()
    def add_number(self):
        # 문자열을 숫자로
        added_count = int(self.ui.num_btn.text()) + 1
        self.ui.num_btn.setText(str(added_count))
 
    @pyqtSlot()
    def slot_2nd(self):
        self.ui.label.setText("두번째 버튼")
 
    @pyqtSlot()
    def slot_3rd(self):
        self.ui.label.setText("세번째 버튼")
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())