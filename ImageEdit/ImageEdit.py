from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import (QMainWindow, QApplication, QGridLayout, QLayout, QLineEdit, QSizePolicy, QToolButton, QWidget)
import cv2
from PIL import Image
import os.path

from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon

FormUi = uic.loadUiType("ImageEdit.ui")[0]

class SearchDir(QWidget):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.initUI()
    
    def initUI(self):
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)
        self.show()

    def getPath(self):
        index = self.tree.currentIndex()
        return self.model.filePath(index)

class ImageEdit(QMainWindow, FormUi):
    
    def __init__(self, parent=None):
        super(ImageEdit, self).__init__(parent)
        self.supportExt = ['png', 'jpg']
        self.setupUi(self)
        self.initUI()
        self.pu_run.clicked.connect(self.run)

    def initUI(self):
        self.searchDir = SearchDir()
        self.gridLayout.addWidget(self.searchDir, 6, 1, 1, 4)
        self.show()

    def run(self):
        if self.ra_mouse_path.isChecked():
            imagePath = self.searchDir.getPath()
            if os.path.splitext(imagePath)[1] not in self.supportExt:
                self.inform.setText(' '.join(self.supportExt) + " file is supported..")
            input = imagePath
        elif self.ra_key_path.isChecked():
            if not self.li_path.text():
                self.inform.setText("Please enter a file path..")
            input = self.li_path.text()
            
        output = ""
        if self.chk_resize.isChecked() == True:
            if not self.li_width.text() or not self.li_height.text():
                self.inform.setText("Please enter width and height..")
                return

            output = self.ex_resize(input, self.li_width.text(), self.li_height.text())
            if not output:
                self.inform.setText("resize failed..")
                return

        if self.chk_rotate.isChecked() == True:
            if not self.li_rotate.text():
                self.inform.setText("Please enter a angle..")
                return

            output = self.ex_rotate(input if not output else output, self.li_rotate.text())
            if not output:
                self.inform.setText("rotate failed..")
                return

        if self.chk_hflip.isChecked() == True:
            output = self.ex_hflip(input if not output else output)
            if not output:
                self.inform.setText("hflip failed..")
                return

        if self.chk_vflip.isChecked() == True:
            output = self.ex_vflip(input if not output else output)
            if not output:
                self.inform.setText("vflip failed..")
                return

        if self.chk_rename.isChecked() == True:
            if os.path.splitext(self.li_rename.text())[1] not in self.supportExt:
                self.inform.setText(' '.join(self.supportExt) + " file is supported..")
            output = self.ex_rename(input if not output else output)
            if not output:
                self.inform.setText("rename failed..")
                return
        
        if output is "":
            return

        self.inform.setText("Saved file.. " + output)
        self.preview(output, output)


    def getOutputFileName(self, imagePath, *args):
        filename, ext = os.path.splitext(imagePath)[0], os.path.splitext(imagePath)[1]
        for i in args:
            filename = filename + '_' + i
        
        return filename + ext


    def ex_resize(self, imagePath, width, height):
        img = Image.open(imagePath)
        img2 = img.resize((int(width), int(height)))
        OutputFileName = self.getOutputFileName(imagePath, width, height)
        if not OutputFileName:
            return

        img2.save(OutputFileName)
        return OutputFileName

    def ex_rotate(self, imagePath, angle):
        img = Image.open(imagePath)
        img2 = img.rotate(int(angle))
        OutputFileName = self.getOutputFileName(imagePath, angle)
        if not OutputFileName:
            return

        img2.save(OutputFileName)
        return OutputFileName

    def ex_hflip(self, imagePath):
        img = cv2.imread(imagePath)
        img2 = cv2.flip(img, 0)
        OutputFileName = self.getOutputFileName(imagePath, "h")
        if not OutputFileName:
            return

        cv2.imwrite(OutputFileName, img2)
        return OutputFileName

    def ex_vflip(self, imagePath):
        img = cv2.imread(imagePath)
        img2 = cv2.flip(img, 1)
        OutputFileName = self.getOutputFileName(imagePath, "v")
        if not OutputFileName:
            return

        cv2.imwrite(OutputFileName, img2)
        return OutputFileName

    def ex_rename(self, imagePath):
        img = cv2.imread(imagePath)
        OutputFileName = self.li_rename.text()
        cv2.imwrite(OutputFileName, img)
        return OutputFileName

    def preview(self, imagePath, description = ""):
        img = cv2.imread(imagePath)
        cv2.imshow(description, img)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    ex = ImageEdit()
    sys.exit(app.exec_())
