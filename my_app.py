from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from instr import *

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.connects()
    self.show()
  def set_appear(self): 
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
  def initUI(self):
    self.hello_text = QLabel(text_hello)
    self.instruction = QLabel(text_instruction)
    self.button = QPushButton(text_button)
    self.layout = QVBoxLayout()
    self.layout.addWidget(self.hello_text, )
    self.layout.addWidget(self.instruction)
    self.layout.addWidget(self.button)
    self.setLayout(self.layout)
  def connects(self):
    self.button.clicked.connect(self.next_click)
  def next_click(self):
    self.hide()
    self.tw = TestWin()
app = QApplication([])
mw = MainWin()
app.exec_()
