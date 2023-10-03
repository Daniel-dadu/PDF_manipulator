import os
from PyQt5 import QtWidgets
from window import Window

class PDFPreviewerApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Previewer")
        self.setGeometry(600, 50, 800, 600)

        self.web_view = Window()
        self.setCentralWidget(self.web_view)

        open_button = QtWidgets.QPushButton("Open PDF", self)
        open_button.clicked.connect(self.openPDF)
        open_button.setGeometry(10, 10, 100, 30)

        merge_button = QtWidgets.QPushButton("Merge PDF", self)
        merge_button.clicked.connect(self.mergePDF)
        merge_button.setGeometry(120, 10, 100, 30)

        rotate_button = QtWidgets.QPushButton("Rotate PDF", self)
        rotate_button.clicked.connect(self.rotatePDF)
        rotate_button.setGeometry(230, 10, 100, 30)

        delete_button = QtWidgets.QPushButton("Delete Pages", self)
        delete_button.clicked.connect(self.deletePages)
        delete_button.setGeometry(340, 10, 100, 30)

        rearrange_button = QtWidgets.QPushButton("Rearrange Pages", self)
        rearrange_button.clicked.connect(self.rearrangePages)
        rearrange_button.setGeometry(450, 10, 130, 30)

        save_as_button = QtWidgets.QPushButton("Save As", self)
        save_as_button.clicked.connect(self.saveAsPDF)
        save_as_button.setGeometry(590, 10, 100, 30)

    def openPDF(self): self.web_view.openPDF()
    def mergePDF(self): self.web_view.mergePDF()
    def rotatePDF(self): self.web_view.rotatePDF()
    def deletePages(self): self.web_view.deletePages()
    def rearrangePages(self): self.web_view.rearrangePages()
    def saveAsPDF(self): self.web_view.saveAsPDF()