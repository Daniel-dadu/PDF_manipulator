from PyQt5 import QtWidgets
from pdf_manipulator import get_num_pages

class PageRotationDialog(QtWidgets.QDialog):
    def __init__(self, pdf_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Page Rotation")
        self.setGeometry(600, 150, 400, 300)

        self.pages_to_rotate = []  # List to store selected pages for rotation
        self.rotation_degrees = 90  # Default rotation is clockwise (90 degrees)

        num_pages = get_num_pages(pdf_path)

        # Widget to select pages
        page_label = QtWidgets.QLabel("Select Pages to Rotate:", self)
        self.page_list_widget = QtWidgets.QListWidget(self)
        self.page_list_widget.setGeometry(10, 30, 180, 150)
        self.page_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.page_list_widget.addItems([str(i + 1) for i in range(num_pages)])  # Display page numbers

        # Widget to select rotation degree
        degree_label = QtWidgets.QLabel("Select Rotation Degree:", self)
        clockwise_button = QtWidgets.QRadioButton("Clockwise (90 degrees)", self)
        anticlockwise_button = QtWidgets.QRadioButton("Anticlockwise (270 degrees)", self)
        upside_down_button = QtWidgets.QRadioButton("Upside Down (180 degrees)", self)

        self.rotation_group = QtWidgets.QButtonGroup(self)
        self.rotation_group.addButton(clockwise_button, 1)
        self.rotation_group.addButton(anticlockwise_button, 2)
        self.rotation_group.addButton(upside_down_button, 3)

        self.rotate_button = QtWidgets.QPushButton("Rotate", self)
        self.rotate_button.clicked.connect(self.rotatePages)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(page_label)
        layout.addWidget(self.page_list_widget)
        layout.addWidget(degree_label)
        layout.addWidget(clockwise_button)
        layout.addWidget(anticlockwise_button)
        layout.addWidget(upside_down_button)
        layout.addWidget(self.rotate_button)

        self.setLayout(layout)

        # Set the initial state of the "Rotate" button
        self.rotate_button.setEnabled(False)

        # Connect the button's state to page and degree selection
        self.page_list_widget.itemSelectionChanged.connect(self.updateRotateButtonState)
        self.rotation_group.buttonClicked.connect(self.updateRotateButtonState)

    def updateRotateButtonState(self):
        # Enable the "Rotate" button only when pages and degree are selected
        if self.page_list_widget.selectedItems() and self.rotation_group.checkedButton():
            self.rotate_button.setEnabled(True)
        else:
            self.rotate_button.setEnabled(False)

    def rotatePages(self):
        for item in self.page_list_widget.selectedItems():
            self.pages_to_rotate.append(int(item.text()))  # Get selected page numbers
        
        selected_button = self.rotation_group.checkedButton()
        if selected_button:
            rotation_type = selected_button.text()
            if "Clockwise" in rotation_type:
                self.rotation_degrees = 90
            elif "Anticlockwise" in rotation_type:
                self.rotation_degrees = 270
            elif "Upside Down" in rotation_type:
                self.rotation_degrees = 180

        # Close the dialog
        self.accept()
