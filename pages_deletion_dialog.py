from PyQt5 import QtWidgets
from pdf_manipulator import get_num_pages

class PagesDeletionDialog(QtWidgets.QDialog):
    def __init__(self, pdf_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Delete Pages")
        self.setGeometry(600, 150, 400, 300)

        self.pages_to_delete = []  # List to store selected pages for deletion

        num_pages = get_num_pages(pdf_path)  # Get the number of pages in the PDF

        self.page_list_widget = QtWidgets.QListWidget(self)
        self.page_list_widget.setGeometry(10, 10, 180, 150)
        self.page_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.page_list_widget.addItems([str(i + 1) for i in range(num_pages)])  # Display page numbers

        delete_button = QtWidgets.QPushButton("Delete", self)
        delete_button.clicked.connect(self.deletePages)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Select the pages to delete:"))
        layout.addWidget(self.page_list_widget)
        layout.addWidget(delete_button)

        self.setLayout(layout)

    def deletePages(self):
        for item in self.page_list_widget.selectedItems():
            self.pages_to_delete.append(int(item.text()))  # Get selected page numbers

        # Close the dialog
        self.accept()
