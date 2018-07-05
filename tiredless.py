import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui



class Time(QtWidgets.QWidget):
    def __init__(self):
        super(Time, self).__init__()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = QtWidgets.QLabel("cycles to sleep")
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setValue(4)
        self.slider.setMinimum(1)
        self.slider.setMaximum(8)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.lbl2 = QtWidgets.QLabel("minutes till you fall asleep")
        self.le = QtWidgets.QLineEdit()
        self.lbl3 = QtWidgets.QLabel("A_{n} =90 cdot 2^(n-1)  over {60}")#libre office
        self.lbl3.setFont(QtGui.QFont("SansSerif",30))
        self.setToolTip("the formula at the beginnig is the sequence of the\n cycles. n = number of the cycle\n A = minutes of that cycle")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.lbl)
        h_box.addWidget(self.slider)

        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addWidget(self.lbl2)
        h2_box.addWidget(self.le)

        h4_box = QtWidgets.QHBoxLayout()
        h4_box.addStretch()
        h4_box.addWidget(self.lbl3)
        h4_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h4_box)

        self.slider.valueChanged.connect(self.houur)

        self.setLayout(v_box)
        self.show()
        self.setWindowTitle("sleep well")



    def houur(self):
        if self.le.text():
            till_sleep = int(self.le.text())
            till_sleep *= 60
            now = QtCore.QTime.currentTime()
            cycle = 5400 + till_sleep
            multiplier = self.slider.value()
            self.lbl3.setText(now.addSecs(cycle*multiplier).toString())
        else:
            self.lbl3.setText("00")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    e = Time()
    sys.exit(app.exec_())































