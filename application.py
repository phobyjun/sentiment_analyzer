import sys
from mylib.analyzing_sentiment_F import analyzing_sentiment
from mylib.papagoNMT import translator
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot


class Form(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = uic.loadUi("form.ui", self)
        self.ui.show()
        self.txt = ""
        self.result = ()
        self.ta = ""
        self.ts = ""
        self.p = ""
        self.a = ""

    @pyqtSlot()
    def getSentence(self):
        self.txt = translator(self.ui.sentence.text())
        self.result = analyzing_sentiment(self.txt)
        self.ta = str(self.result[0])
        self.ts = str(self.result[1])
        self.p = str(self.result[2])
        self.a = str(self.result[3])

    @pyqtSlot()
    def click(self):
        self.ui.label_TA.setText(self.ta)
        self.ui.label_TS.setText(self.ts)
        self.ui.label_P.setText(self.p)
        self.ui.label_A.setText(self.a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec_())
