import os
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from pdf_manipulation.pdf_manipulator import pdf_combiner, pdf_rotator, pdf_deleter, pdf_rearranger, rename_and_move_pdf, delete_pdf
from dialogs.page_rotation_dialog import PageRotationDialog
from dialogs.pages_deletion_dialog import PagesDeletionDialog
from dialogs.pages_rearrange_dialog import PagesRearrangeDialog

class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super().__init__()
        self.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.current_pdf_path = None  # Store the path of the currently displayed PDF

        # Connect the loadFinished signal to updateButtonStates
        self.loadFinished.connect(self.updateButtonStates)

    def loadPDF(self, pdf_path):
        formatted_path = "file:///" + pdf_path.replace(" ", "%20")
        self.load(QtCore.QUrl.fromUserInput(formatted_path))
        self.current_pdf_path = pdf_path  # Update the current PDF path
        self.updateButtonStates()  # Call the method when PDF is loaded

    def openPDF(self):
        options = QtWidgets.QFileDialog.Options()
        pdf_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if pdf_file:
            self.loadPDF(pdf_file)
            self.window().updateSaveAsState(False) # Disable Save as btn

    def mergePDF(self):
        if self.current_pdf_path is not None:
            options = QtWidgets.QFileDialog.Options()
            pdf_to_merge, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select PDF to Merge", "", "PDF Files (*.pdf);;All Files (*)", options=options)

            if pdf_to_merge:
                self.current_pdf_path = pdf_combiner([self.current_pdf_path, pdf_to_merge])
                self.loadPDF(self.current_pdf_path)
                self.window().updateSaveAsState(True) # Enable Save as btn

    def rotatePDF(self):
        if self.current_pdf_path is not None:
            dialog = PageRotationDialog(self.current_pdf_path)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                pages_to_rotate = dialog.pages_to_rotate
                rotation_degrees = dialog.rotation_degrees
                if pages_to_rotate:
                    self.current_pdf_path = pdf_rotator(self.current_pdf_path, pages_to_rotate, rotation_degrees)
                    self.loadPDF(self.current_pdf_path)
                    self.window().updateSaveAsState(True) # Enable Save as btn

    def deletePages(self):
        if self.current_pdf_path is not None:
            dialog = PagesDeletionDialog(self.current_pdf_path)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                pages_to_delete = dialog.pages_to_delete
                if pages_to_delete:
                    self.current_pdf_path = pdf_deleter(self.current_pdf_path, pages_to_delete)
                    self.loadPDF(self.current_pdf_path)
                    self.window().updateSaveAsState(True) # Enable Save as btn

    def rearrangePages(self):
        if self.current_pdf_path is not None:
            dialog = PagesRearrangeDialog(self.current_pdf_path)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                new_order_pages = dialog.new_order_pages
                if new_order_pages:
                    self.current_pdf_path = pdf_rearranger(self.current_pdf_path, new_order_pages)
                    self.loadPDF(self.current_pdf_path)
                    self.window().updateSaveAsState(True) # Enable Save as btn

    def saveAsPDF(self):
        if self.current_pdf_path is not None:
            options = QtWidgets.QFileDialog.Options()
            new_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save As PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)
            if new_name:
                new_location = os.path.dirname(new_name)
                new_name = os.path.basename(new_name)
                # Load a blank page to release the hold on the current PDF
                self.load(QtCore.QUrl('about:blank'))

                saved_path = rename_and_move_pdf(self.current_pdf_path, new_name, new_location)
                if saved_path:
                    delete_pdf(self.current_pdf_path)  # Delete the edited PDF
                    self.current_pdf_path = None  # Reset the edited PDF path
                    self.loadPDF(saved_path.replace('\\', '/')) # To keep editing
                    self.window().updateSaveAsState(False) # Disable Save as btn

    def updateButtonStates(self):
        pdf_path = self.current_pdf_path
        self.window().updateButtonStates(pdf_path)  # Call the parent's updateButtonStates method

    def on_close(self, event):
        if self.current_pdf_path:
            self.load(QtCore.QUrl("about:blank"))  # Load a blank page
        delete_pdf((os.getcwd() + "/.editing.pdf").replace("\\", "/"))
        event.accept()