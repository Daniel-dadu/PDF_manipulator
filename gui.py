import sys
import os
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from pdf_manipulator import pdf_combiner, pdf_rotator, pdf_deleter, pdf_rearranger, rename_and_move_pdf, delete_pdf

class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super().__init__()
        self.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.current_pdf_path = None  # Store the path of the currently displayed PDF
        self.edited_pdf_path = None  # Store the path of the edited PDF

    def loadPDF(self, pdf_path):
        formatted_path = "file:///" + pdf_path.replace(" ", "%20")
        self.load(QtCore.QUrl.fromUserInput(formatted_path))
        self.current_pdf_path = pdf_path  # Update the current PDF path

    def mergePDF(self, pdf_to_merge):
        if self.current_pdf_path is not None:
            self.edited_pdf_path = pdf_combiner([self.current_pdf_path, pdf_to_merge])
            self.loadPDF(self.edited_pdf_path)

    def rotatePDF(self, rotation):
        if self.current_pdf_path is not None:
            self.edited_pdf_path = pdf_rotator(self.current_pdf_path, rotation)
            self.loadPDF(self.edited_pdf_path)

    def deletePages(self, pages_to_delete):
        if self.current_pdf_path is not None:
            self.edited_pdf_path = pdf_deleter(self.current_pdf_path, pages_to_delete)
            self.loadPDF(self.edited_pdf_path)

    def rearrangePages(self, page_order):
        if self.current_pdf_path is not None:
            self.edited_pdf_path = pdf_rearranger(self.current_pdf_path, page_order)
            self.loadPDF(self.edited_pdf_path)

    def saveAsPDF(self, new_name, new_location):
        if self.edited_pdf_path is not None:
            saved_path = rename_and_move_pdf(self.edited_pdf_path, new_name, new_location)
            if saved_path:
                delete_pdf(self.edited_pdf_path)  # Delete the edited PDF
                self.edited_pdf_path = None  # Reset the edited PDF path

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

    def openPDF(self):
        options = QtWidgets.QFileDialog.Options()
        pdf_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf);;All Files (*)", options=options)

        if pdf_file:
            self.web_view.loadPDF(pdf_file)

    def mergePDF(self):
        options = QtWidgets.QFileDialog.Options()
        pdf_to_merge, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select PDF to Merge", "", "PDF Files (*.pdf);;All Files (*)", options=options)

        if pdf_to_merge:
            self.web_view.mergePDF(pdf_to_merge)

    def rotatePDF(self):
        # Implement rotation logic here
        pass

    def deletePages(self):
        # Implement page deletion logic here
        pass

    def rearrangePages(self):
        # Implement page rearrangement logic here
        pass

    def saveAsPDF(self):
        options = QtWidgets.QFileDialog.Options()
        new_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save As PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if new_name:
            new_location = os.path.dirname(new_name)
            self.web_view.saveAsPDF(os.path.basename(new_name), new_location)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PDFPreviewerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
