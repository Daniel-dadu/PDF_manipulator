from PyQt5 import QtWidgets
from pdf_manipulation.pdf_manipulator import get_num_pages

class PagesRearrangeDialog(QtWidgets.QDialog):
    def __init__(self, pdf_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Rearrange Pages")
        self.setGeometry(600, 150, 400, 300)

        self.new_order_pages = []

        num_pages = get_num_pages(pdf_path)  # Get the number of pages in the PDF

        self.page_list_widget = QtWidgets.QListWidget(self)
        self.page_list_widget.setGeometry(10, 10, 180, 150)
        self.page_list_widget.addItems([str(i + 1) for i in range(num_pages)])  # Display page numbers
        self.page_list_widget.setDragEnabled(True)
        self.page_list_widget.setDropIndicatorShown(True)
        self.page_list_widget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        rearrange_button = QtWidgets.QPushButton("Rearrange", self)
        rearrange_button.clicked.connect(self.rearrangePages)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Drag and drop pages to rearrange them:"))
        layout.addWidget(self.page_list_widget)
        layout.addWidget(rearrange_button)

        self.setLayout(layout)

    def rearrangePages(self):
        for i in range(self.page_list_widget.count()):
            self.new_order_pages.append(int(self.page_list_widget.item(i).text()))  # Get selected page numbers

        # Close the dialog
        self.accept()
