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

        self.merge_button = QtWidgets.QPushButton("Append file", self)
        self.merge_button.clicked.connect(self.mergePDF)
        self.merge_button.setGeometry(120, 10, 100, 30)
        self.merge_button.setEnabled(False)  # Initially disabled

        self.rotate_button = QtWidgets.QPushButton("Rotate pages", self)
        self.rotate_button.clicked.connect(self.rotatePDF)
        self.rotate_button.setGeometry(230, 10, 100, 30)
        self.rotate_button.setEnabled(False)  # Initially disabled

        self.delete_button = QtWidgets.QPushButton("Delete Pages", self)
        self.delete_button.clicked.connect(self.deletePages)
        self.delete_button.setGeometry(340, 10, 100, 30)
        self.delete_button.setEnabled(False)  # Initially disabled

        self.rearrange_button = QtWidgets.QPushButton("Rearrange Pages", self)
        self.rearrange_button.clicked.connect(self.rearrangePages)
        self.rearrange_button.setGeometry(450, 10, 130, 30)
        self.rearrange_button.setEnabled(False)  # Initially disabled

        self.save_as_button = QtWidgets.QPushButton("Save As", self)
        self.save_as_button.clicked.connect(self.saveAsPDF)
        self.save_as_button.setGeometry(590, 10, 100, 30)
        self.save_as_button.setEnabled(False)  # Initially disabled

    def openPDF(self): self.web_view.openPDF()
    def mergePDF(self): self.web_view.mergePDF()
    def rotatePDF(self): self.web_view.rotatePDF()
    def deletePages(self): self.web_view.deletePages()
    def rearrangePages(self): self.web_view.rearrangePages()
    def saveAsPDF(self): self.web_view.saveAsPDF()

    def updateButtonStates(self, pdf_path):
        self.merge_button.setEnabled(pdf_path is not None)
        self.rotate_button.setEnabled(pdf_path is not None)
        self.delete_button.setEnabled(pdf_path is not None)
        self.rearrange_button.setEnabled(pdf_path is not None)
        self.save_as_button.setEnabled(pdf_path is not None)
