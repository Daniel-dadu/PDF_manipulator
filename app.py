from PyQt5 import QtWidgets, QtGui
from window import Window

class PDFPreviewerApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Get information about the screen
        screen_info = QtWidgets.QDesktopWidget().screenGeometry()
        screen_width, screen_height = screen_info.width(), screen_info.height()

        self.setWindowTitle("PDF Manipulator (by @Daniel-dadu)")

        window_width = int(screen_width * 0.5) # 50% of width
        window_height = int(screen_height * 0.8) # 80% of height
        window_x = window_width - window_width//2
        window_y = int(window_height * 0.1)
        self.setGeometry(window_x, window_y, window_width, window_height)

        self.web_view = Window()  # PDF web view

        # Create a horizontal layout for the top row of buttons
        top_button_layout = QtWidgets.QHBoxLayout()

        open_button = QtWidgets.QPushButton("Open PDF")
        open_button.setFont(QtGui.QFont("Arial", 12))
        open_button.setMinimumHeight(40)
        open_button.clicked.connect(self.openPDF)
        top_button_layout.addWidget(open_button)

        self.merge_button = QtWidgets.QPushButton("Append file")
        self.merge_button.setFont(QtGui.QFont("Arial", 12))
        self.merge_button.setMinimumHeight(40)
        self.merge_button.clicked.connect(self.mergePDF)
        self.merge_button.setEnabled(False)  # Initially disabled
        top_button_layout.addWidget(self.merge_button)

        self.rotate_button = QtWidgets.QPushButton("Rotate pages")
        self.rotate_button.setFont(QtGui.QFont("Arial", 12))
        self.rotate_button.setMinimumHeight(40)
        self.rotate_button.clicked.connect(self.rotatePDF)
        self.rotate_button.setEnabled(False)  # Initially disabled
        top_button_layout.addWidget(self.rotate_button)

        self.delete_button = QtWidgets.QPushButton("Delete pages")
        self.delete_button.setFont(QtGui.QFont("Arial", 12))
        self.delete_button.setMinimumHeight(40)
        self.delete_button.clicked.connect(self.deletePages)
        self.delete_button.setEnabled(False)  # Initially disabled
        top_button_layout.addWidget(self.delete_button)

        self.rearrange_button = QtWidgets.QPushButton("Rearrange pages")
        self.rearrange_button.setFont(QtGui.QFont("Arial", 12))
        self.rearrange_button.setMinimumHeight(40)
        self.rearrange_button.clicked.connect(self.rearrangePages)
        self.rearrange_button.setEnabled(False)  # Initially disabled
        top_button_layout.addWidget(self.rearrange_button)

        self.save_as_button = QtWidgets.QPushButton("Save as")
        self.save_as_button.setFont(QtGui.QFont("Arial", 12))
        self.save_as_button.setMinimumHeight(40)
        self.save_as_button.clicked.connect(self.saveAsPDF)
        self.save_as_button.setEnabled(False)  # Initially disabled
        top_button_layout.addWidget(self.save_as_button)

        # Create a vertical layout for the entire window
        main_layout = QtWidgets.QVBoxLayout()

        # Add the top row of buttons to the main layout
        main_layout.addLayout(top_button_layout)

        # Add the PDF web view to the main layout
        main_layout.addWidget(self.web_view)

        # Create a central widget and set the main layout
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

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

    def closeEvent(self, event): self.web_view.on_close(event)