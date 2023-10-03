from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from pdf_manipulator import pdf_combiner, pdf_rotator, pdf_deleter, pdf_rearranger, rename_and_move_pdf, delete_pdf
from page_rotation_dialog import PageRotationDialog
from pages_deletion_dialog import PagesDeletionDialog

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

    def rotatePDF(self):
        if self.current_pdf_path is not None:
            dialog = PageRotationDialog(self.current_pdf_path)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                pages_to_rotate = dialog.pages_to_rotate
                rotation_degrees = dialog.rotation_degrees
                if pages_to_rotate:
                    self.edited_pdf_path = pdf_rotator(self.current_pdf_path, pages_to_rotate, rotation_degrees)
                    self.loadPDF(self.edited_pdf_path)

    def deletePages(self):
        if self.current_pdf_path is not None:
            dialog = PagesDeletionDialog(self.current_pdf_path)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                pages_to_delete = dialog.pages_to_delete
                if pages_to_delete:
                    self.edited_pdf_path = pdf_deleter(self.current_pdf_path, pages_to_delete)
                    self.loadPDF(self.edited_pdf_path)

    def rearrangePages(self, page_order):
        if self.current_pdf_path is not None:
            self.edited_pdf_path = pdf_rearranger(self.current_pdf_path, page_order)
            self.loadPDF(self.edited_pdf_path)

    def saveAsPDF(self, new_name, new_location):
        if self.edited_pdf_path is not None:
            # Load a blank page to release the hold on the current PDF
            self.load(QtCore.QUrl('about:blank'))

            saved_path = rename_and_move_pdf(self.edited_pdf_path, new_name, new_location)
            if saved_path:
                delete_pdf(self.edited_pdf_path)  # Delete the edited PDF
                self.edited_pdf_path = None  # Reset the edited PDF path
                self.loadPDF(saved_path.replace('\\', '/')) # To keep editing