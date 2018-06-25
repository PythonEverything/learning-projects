import sys
import os
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.text = QtWidgets.QTextEdit()
        self.clear = QtWidgets.QPushButton("Clear")
        self.save = QtWidgets.QPushButton("Save")
        self.open = QtWidgets.QPushButton("Open")

        self.create_widgets()

    def create_widgets(self):
        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.clear)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text)
        v_box.addLayout(h_box)

        self.clear.clicked.connect(self.clearf)
        self.open.clicked.connect(self.openf)
        self.save.clicked.connect(self.savef)

        self.setLayout(v_box)
        self.show()

    def clearf(self):
        self.text.clear()

    def openf(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "open this shit", os.getenv("HOME"))
        with open(filename[0], "r") as f:
            tex = f.read()
            self.text.setText(tex)

    def savef(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self ,"save this shit", os.getenv("HOME"))
        with open(filename[0], "w") as f:
            tex = self.text.toPlainText()
            f.write(tex)

class Notepad(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = Window()
        self.setCentralWidget(self.w)

        self.create_widgets()

    def create_widgets(self):
        bar = self.menuBar()

        file = bar.addMenu("File")
        edit = bar.addMenu("Edit")

        new_action = QtWidgets.QAction ("&New",self)
        new_action.setShortcut("Ctrl+N")

        save_action = QtWidgets.QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")

        quit_action = QtWidgets.QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")

        open_action = QtWidgets.QAction("&Open", self)

        find_action = QtWidgets.QAction("Find...", self)
        replace_action = QtWidgets.QAction("Replace...", self)
        find = edit.addMenu("Find")

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)
        find.addAction(find_action)
        find.addAction(replace_action)

        quit_action.triggered.connect(self.quitt)
        open_action.triggered.connect(self.w.openf)
        save_action.triggered.connect(self.w.savef)
        new_action.triggered.connect(self.w.clearf)

        self.show()

    def quitt(self):
        QtWidgets.qApp.exit()



app = QtWidgets.QApplication(sys.argv)
np = Notepad()
sys.exit(app.exec_())




