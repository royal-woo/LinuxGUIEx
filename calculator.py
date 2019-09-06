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

    def act_btn_number(self, number):
        self.string += number
        self.textbox.setText(self.string)

    def act_btn_operator(self, operator):
        if self.multi_operator is True :
            self.textbox.setText("operator is aleady set..")
            return
        self.string += operator
        self.textbox.setText(self.string)
        self.multi_operator = True
    
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
        self.multi_operator = False
        self.textbox = QLineEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setText(str(0))

        grid.addWidget(self.textbox, 0, 0, 1, 4)

        btn_0 = Button('0')
        grid.addWidget(btn_0, 5, 0, 1, 2)
        btn_0.clicked.connect(lambda: self.act_btn_number('0'))  

        #map(self.act_btn_number, [str(i) for i in range(1, 10)])
        '''
        lambdas = [lambda: self.act_btn_number(str(i)) for i in range(1, 10)]
        
        for (i, f) in zip(range(1, 10), lambdas):
            setattr(self, 'btn_%s' % (i), Button(str(i)))
            grid.addWidget(getattr(self, 'btn_%s' % (i)), 5 - (i / 3), (i  - 1) % 3)
            getattr(self, 'btn_%s' % (i)).clicked.connect(f)  
        '''
        
        for i in range(1, 10):
            print(str(i))
            setattr(self, 'btn_%s' % (i), Button(str(i)))
            grid.addWidget(getattr(self, 'btn_%s' % (i)), 5 - (i / 3), (i  - 1) % 3)
            getattr(self, 'btn_%s' % (i)).clicked.connect(lambda: self.act_btn_number(str(i)))
        
        btn_plus = Button('+')
        grid.addWidget(btn_plus, 1, 0)
        btn_plus.clicked.connect(lambda: self.act_btn_operator('+'))

        btn_minus = Button('-')
        grid.addWidget(btn_minus, 1, 1)
        btn_minus.clicked.connect(lambda: self.act_btn_operator('-'))

        btn_mult = Button('*')
        grid.addWidget(btn_mult, 1, 2)
        btn_mult.clicked.connect(lambda: self.act_btn_operator('*'))

        btn_divide = Button('/')
        grid.addWidget(btn_divide, 1, 3)
        btn_divide.clicked.connect(lambda: self.act_btn_operator('/'))

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
