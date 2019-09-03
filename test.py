import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont

class MyApp(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    okButton = QPushButton('OK')
    cancelButton = QPushButton('Cancel')
    hbox = QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(okButton)
    hbox.addWidget(cancelButton)
    hbox.addStretch(1)

    vbox = QVBoxLayout()
    vbox.addStretch(3)
    vbox.addLayout(hbox)
    vbox.addStretch(1)

    self.setLayout(vbox)

    exitAction = QAction(QIcon('exit.png'), 'Exit', self)
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(qApp.quit)
    self.statusBar().showMessage('Ready')

    exitAction = QAction(QIcon('exit.png'), 'Exit', self)
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(qApp.quit)

    self.toolbar = self.addToolBar('Exit')
    self.toolbar.addAction(exitAction)

  # 
    saveAction = QAction(QIcon('save.png'), 'Save', self)
    saveAction.setShortcut('Ctrl+S')
    saveAction.setStatusTip('Save application')
    saveAction.triggered.connect(qApp.quit)

    self.toolbar = self.addToolBar('Save')
    self.toolbar.addAction(saveAction)

#
    menubar = self.menuBar()
    menubar.setNativeMenuBar(False)
    fileMenu = menubar.addMenu('&File')
    fileMenu.addAction(exitAction)  
    QToolTip.setFont(QFont('SansSerif', 10))
    self.setToolTip('This is a <b>QWidget</b> widget')

    btn = QPushButton('Quit', self)
    btn.move(100, 0)
    btn.resize(btn.sizeHint())
    btn.clicked.connect(QCoreApplication.instance().quit)
    btn.setToolTip('This is a <b>QPushButton</b>')

    self.setWindowTitle('Icon')
    self.setWindowIcon(QIcon('./web.png'))
    self.center()
    self.resize(500, 350)
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())
