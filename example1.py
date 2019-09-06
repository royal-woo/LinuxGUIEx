import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QSizePolicy, QComboBox

class inform_text(QLineEdit):
    def __init__(self, text, read=False, parent=None):
        super(inform_text, self).__init__(parent)
        if read is True:
            self.setReadOnly(True)
        self.setPlaceholderText(text)



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.length = 0
        self.weight = 0
        self.length_unit = "m"
        self.weight_unit = "kg"
        self.result = {"mm": 0, "cm" : 0, "m" : 0, "km" : 0, "mg" : 0, "g" : 0, "kg" : 0, "t" : 0}


    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.lbl = QLabel(self)
        grid.addWidget(self.lbl, 4, 0)

        qle_length = inform_text("길이")
        qle_length.textChanged[str].connect(self.onChanged)
        grid.addWidget(qle_length, 0, 0)
        qle_length.textChanged[str].connect(self.onChanged)

        qle_weight = inform_text("무게")
        qle_weight.textChanged[str].connect(self.onChanged)
        grid.addWidget(qle_weight, 0, 2)
        qle_weight.textChanged[str].connect(self.onChanged)

        cb_length = QComboBox(self)
        grid.addWidget(cb_length, 1, 0)
        cb_length.addItem('mm')
        cb_length.addItem('cm')
        cb_length.addItem('m')
        cb_length.addItem('km')
        cb_length.setCurrentIndex(2)
        cb_length.activated[str].connect(self.onActivated)

        cb_weight = QComboBox(self)
        grid.addWidget(cb_weight, 1, 2)
        cb_weight.addItem('mg')
        cb_weight.addItem('g')
        cb_weight.addItem('kg')
        cb_weight.addItem('t')
        cb_weight.setCurrentIndex(2)
        cb_weight.activated[str].connect(self.onActivated)

        self.qle_length_result = inform_text("result..", True)
        grid.addWidget(self.qle_length_result, 2, 0, 2, 2)
        self.qle_length_result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.qle_weight_result = inform_text("result..", True)
        grid.addWidget(self.qle_weight_result, 2, 2, 2, 2)
        self.qle_weight_result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def transform_unit(self):
        if self.length_unit is "mm":
            self.result["mm"], self.result["cm"],self.result["m"],self.result["km"] = self.calc_length_m(self.length / 1000)
        elif self.length_unit is "cm":
            self.result["mm"], self.result["cm"],self.result["m"],self.result["km"] = self.calc_length_m(self.length / 100)
        elif self.length_unit is "m":
            self.result["mm"], self.result["cm"],self.result["m"],self.result["km"] = self.calc_length_m(self.length)
        elif self.length_unit is "km":
            self.result["mm"], self.result["cm"],self.result["m"],self.result["km"] = self.calc_length_m(self.length * 1000)
        elif self.weight_unit is "mg":
            self.result["mg"], self.result["g"], self.result["kg"], self.result["t"] = self.calc_weight_g(self.weight / 1000)
        elif self.weight_unit is "g":
            self.result["mg"], self.result["g"], self.result["kg"], self.result["t"] = self.calc_length_g(self.weight)
        elif self.weight_unit is "kg":
            self.result["mg"], self.result["g"], self.result["kg"], self.result["t"] = self.calc_length_g(self.weight * 1000)
        elif self.weight_unit is "t":
            self.result["mg"], self.result["g"], self.result["kg"], self.result["t"] = self.calc_length_g(self.weight * 1000 * 1000)
        else:
            return

    def calc_length_m(self, value):
        return [value * 1000, value * 100, value, value / 1000]

    def calc_weight_kg(self, value):
        return [value * 1000 * 1000, value * 1000, value, value / 1000]

    def onActivated(self, unit):
        self.transform_unit()
        if unit[-1] is "m":
            self.qle_length_result.setText(str(self.result))
        elif unit[-1] is "g":
            self.qle_weight_result.setText(str(self.result))
        else:
            return


    def onChanged(self, text):
        self.length = int(text)
        self.transform_unit()
        self.qle_length_result.setText(str(self.result))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
