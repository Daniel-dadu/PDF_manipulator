import sys
from PyQt5 import QtWidgets
from app import PDFPreviewerApp

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PDFPreviewerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
