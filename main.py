# create a PDF manipulator that uses the PyPDF2 library
# it should be able to:
# - merge multiple PDFs into a single PDF
# - split a PDF into multiple PDFs
# - rotate pages of a PDF
# - delete pages of a PDF
# - reaarange pages of a PDF

import PyPDF2

# function to merge PDFs
def pdf_combiner(pdf_list):
    # create a PDFFileMerger object
    merger = PyPDF2.PdfMerger()
    # loop through the list of PDFs
    for pdf in pdf_list:
        # append each PDF to the merger object
        merger.append(pdf)
    # write the merger object to a new PDF file
    merger.write('merged.pdf')

# function to rotate PDFs
def pdf_rotator(pdf, rotation):
    # create a PdfFileReader object
    reader = PyPDF2.PdfFileReader(pdf)
    # create a PdfFileWriter object
    writer = PyPDF2.PdfFileWriter()
    # loop through the pages of the PDF
    for page in range(reader.numPages):
        # grab each page
        page = reader.getPage(page)
        # rotate each page
        page.rotateClockwise(rotation)
        # add each page to the writer object
        writer.addPage(page)
    # write the writer object to a new PDF file
    with open('rotated.pdf', 'wb') as new_file:
        writer.write(new_file)

# function to split PDFs
def pdf_splitter(pdf):
    # create a PdfFileReader object
    reader = PyPDF2.PdfFileReader(pdf)
    # loop through the pages of the PDF
    for page in range(reader.numPages):
        # create a PdfFileWriter object
        writer = PyPDF2.PdfFileWriter()
        # grab each page
        page = reader.getPage(page)
        # add each page to the writer object
        writer.addPage(page)
        # write the writer object to a new PDF file
        with open(f'page-{page}.pdf', 'wb') as new_file:
            writer.write(new_file)

# function to delete pages of a PDF
def pdf_deleter(pdf, pages):
    # create a PdfFileReader object
    reader = PyPDF2.PdfFileReader(pdf)
    # create a PdfFileWriter object
    writer = PyPDF2.PdfFileWriter()
    # loop through the pages of the PDF
    for page in range(reader.numPages):
        # grab each page
        page = reader.getPage(page)
        # check if the page is in the list of pages to delete
        if page not in pages:
            # add each page to the writer object
            writer.addPage(page)
    # write the writer object to a new PDF file
    with open('deleted.pdf', 'wb') as new_file:
        writer.write(new_file)

# function to rearrange pages of a PDF
def pdf_rearranger(pdf, page_order):
    # create a PdfFileReader object
    reader = PyPDF2.PdfFileReader(pdf)
    # create a PdfFileWriter object
    writer = PyPDF2.PdfFileWriter()
    # loop through the pages of the PDF
    for page in page_order:
        # grab each page
        page = reader.getPage(page)
        # add each page to the writer object
        writer.addPage(page)
    # write the writer object to a new PDF file
    with open('rearranged.pdf', 'wb') as new_file:
        writer.write(new_file)

# the user should first be asked what they want to do
# then they should be asked for the amount of PDFs they want to manipulate (if applicable)
# then they should be asked for the names PDFs they want to manipulate
# then they should be asked for any other information needed to manipulate the PDFs
# then the PDFs should be manipulated

# ask the user what they want to do
print('What do you want to do?')
print('1. Merge PDFs')
print('2. Rotate PDFs')
print('3. Split PDFs')
print('4. Delete pages of a PDF')
print('5. Rearrange pages of a PDF')
# get the user's choice
choice = int(input('Enter the number of your choice: '))
# ask the user for the amount of PDFs they want to manipulate (if applicable)
num_of_pdfs = int(input('How many PDFs do you want to manipulate? '))
# create an empty list to store the PDFs
inputs = []
# loop through the amount of PDFs the user wants to manipulate
for pdf in range(num_of_pdfs):
    # ask the user for the names of the PDFs they want to manipulate
    pdf_name = input('Enter the name of the PDF: ')
    # append the PDFs to the list
    inputs.append(pdf_name)

# if the user wants to merge PDFs
if choice == 1:
    # call the function
    pdf_combiner(inputs)

# if the user wants to rotate PDFs
elif choice == 2:
    # ask the user how much they want to rotate the PDFs
    rotation = int(input('How much do you want to rotate the PDFs? '))
    # call the function
    pdf_rotator(inputs[0], rotation)

# if the user wants to split PDFs
elif choice == 3:
    # call the function
    pdf_splitter(inputs[0])

# if the user wants to delete pages of a PDF
elif choice == 4:
    # ask the user which pages they want to delete
    pages = input('Which pages do you want to delete? (separate with commas) ')
    # split the pages into a list
    pages = pages.split(',')
    # convert the list of strings into a list of integers
    pages = [int(page) for page in pages]
    # call the function
    pdf_deleter(inputs[0], pages)

# if the user wants to rearrange pages of a PDF
elif choice == 5:
    # ask the user for the new order of the pages
    page_order = input('What is the new order of the pages? (separate with commas) ')
    # split the pages into a list
    page_order = page_order.split(',')
    # convert the list of strings into a list of integers
    page_order = [int(page) for page in page_order]
    # call the function
    pdf_rearranger(inputs[0], page_order)

# if the user enters an invalid choice
else:
    print('Invalid choice')

# end of program