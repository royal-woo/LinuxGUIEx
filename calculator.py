import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QSizePolicy

class Button(QPushButton):
    def __init__(self, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setStyleSheet('Button {background-color: #A0FFDA; color: red;}')

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def act_btn_0(self):
        self.string += '0'
        self.textbox.setText(self.string)

    def act_btn_1(self):
        self.string += '1'
        self.textbox.setText(self.string)

    def act_btn_2(self):
        self.string += '2'
        self.textbox.setText(self.string)

    def act_btn_3(self):
        self.string += '3'
        self.textbox.setText(self.string)

    def act_btn_4(self):
        self.string += '4'
        self.textbox.setText(self.string)

    def act_btn_5(self):
        self.string += '5'
        self.textbox.setText(self.string)

    def act_btn_6(self):
        self.string += '6'
        self.textbox.setText(self.string)

    def act_btn_7(self):
        self.string += '7'
        self.textbox.setText(self.string)

    def act_btn_8(self):
        self.string += '8'
        self.textbox.setText(self.string)

    def act_btn_9(self):
        self.string += '9'
        self.textbox.setText(self.string)

    def act_btn_mult(self):
        self.string += '*'
        self.textbox.setText(self.string)

    def act_btn_plus(self):
        self.string += '+'
        self.textbox.setText(self.string)

    def act_btn_minus(self):
        self.string += '-'
        self.textbox.setText(self.string)

    def act_btn_divide(self):
        self.string += '/'
        self.textbox.setText(self.string)
    
    def act_btn_equal(self):
        if self.string is '':
            return
        self.string = str(eval(self.string))
        self.textbox.setText(self.string)

    def act_btn_clear(self):
        self.string = ''
        self.textbox.setText(str(0))

    def act_btn_delete(self):
        if self.string is '':
            self.textbox.setText(str(0))
            return
        self.string = self.string[:-1]
        self.textbox.setText(self.string)

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.string = ''
        self.textbox = QLineEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setText(str(0))

        grid.addWidget(self.textbox, 0, 0, 1, 4)

        btn_0 = Button('0')
        grid.addWidget(btn_0, 5, 0, 1, 2)
        for i in range(1, 10):
            setattr(self, 'btn_%s' % (i), Button(str(i)))
            grid.addWidget(getattr(self, 'btn_%s' % (i)), 5 - (i / 3), (i  - 1) % 3)
            getattr(self, 'btn_%s' % (i)).clicked.connect(getattr(self, 'act_btn_%s' % (i)))  

        btn_plus = Button('+')
        grid.addWidget(btn_plus, 1, 0)
        btn_plus.clicked.connect(self.act_btn_plus)

        btn_minus = Button('-')
        grid.addWidget(btn_minus, 1, 1)
        btn_minus.clicked.connect(self.act_btn_minus)

        btn_mult = Button('*')
        grid.addWidget(btn_mult, 1, 2)
        btn_mult.clicked.connect(self.act_btn_mult)

        btn_divide = Button('/')
        grid.addWidget(btn_divide, 1, 3)
        btn_divide.clicked.connect(self.act_btn_divide)

        btn_equal = Button('=')
        grid.addWidget(btn_equal, 4, 3, 2, 1)
        btn_equal.clicked.connect(self.act_btn_equal)
        btn_equal.setStyleSheet('Button {background-color: #A3C1DA; color: red;}')

        btn_clear = Button('CE')
        grid.addWidget(btn_clear, 5, 2)
        btn_clear.clicked.connect(self.act_btn_clear)

        btn_delete = Button('DEL')
        grid.addWidget(btn_delete, 2, 3, 2, 1)
        btn_delete.clicked.connect(self.act_btn_delete)

        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
