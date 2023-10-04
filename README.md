# PDF Manipulator

PDF Manipulator is a Python application that allows users to manipulate PDF files. It provides features for merging PDFs, rotating pages, deleting pages, rearranging pages, and saving edited PDFs.

## Acknowledgments

This project was primarily developed with the assistance of GitHub Copilot and ChatGPT (GPT-3). Their invaluable contributions in generating code, suggesting improvements, and providing guidance throughout the development process greatly facilitated the creation of this PDF manipulation application.


## Dependencies

This project relies on the following Python libraries, which can be installed via pip:

- [PyPDF2](https://github.com/mstamy2/PyPDF2): A Python library to work with PDF files.
```
pip install PyPDF2
```

- [PyQt5](https://pypi.org/project/PyQt5/): A set of Python bindings for Qt libraries.
```
pip install PyQt5
```

- [PyQtWebEngine](https://pypi.org/project/PyQtWebEngine/): A set of Python bindings for QtWebEngine.
```
pip install PyQtWebEngine
```


## MVC Pattern Wannabe

In this application, there is an attempt to organize the code following a Model-View-Controller (MVC) pattern. The user interface components, represented by `window.py` and various dialog files, form the view. The controller is embodied by `app.py`, which handles user interactions and invokes model methods for PDF manipulation. However, the full separation of concerns, especially isolating data operations into a dedicated model module or class, is not fully realized. To align more closely with the MVC pattern, consider further segregating data operations into a distinct model layer while the controller manages user interactions, invoking model methods to manipulate data. This evolution will enhance code modularity and maintainability.

## Planned Improvements

While the current version of the PDF Manipulator provides essential PDF editing functionality, there are several planned improvements to make the application even more powerful and versatile:

### Undo and Redo Functionality

We plan to implement an "Undo" and "Redo" feature, allowing users to revert their actions and step forward through their editing history.

### Insert Images as New Pages

Enhance the application to enable users to insert images as new pages into PDF documents, expanding the types of content that can be added.

### Password and Encryption Protection

Add features for setting passwords and encrypting PDF documents to enhance security and restrict access to sensitive information.

### Improved PDF viewer

Upgrade the PDF viewer to deliver a more reliable and seamless experience, addressing the existing bugs for smoother document navigation and readability.
