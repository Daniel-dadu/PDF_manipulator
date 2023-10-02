# PDF manipulator that uses the PyPDF2 library
# It can:
# - merge multiple PDFs into a single PDF
# - split a PDF into multiple PDFs
# - rotate pages of a PDF
# - delete pages of a PDF
# - reaarange pages of a PDF

import PyPDF2

def deleteFileExtension(fileName):
    return fileName[:-4] if len(fileName) > 4 and fileName[-4:] == '.pdf' else fileName

# function to merge PDFs
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged.pdf')

# function to rotate PDFs
def pdf_rotator(pdf, rotation):
    reader = PyPDF2.PdfReader(pdf)
    writer = PyPDF2.PdfWriter()
    for i in range(len(reader.pages)):
        writer.add_page(reader.pages[i])
        writer.pages[i].rotate(rotation)
    with open('rotated.pdf', 'wb') as new_file:
        writer.write(new_file)

# function to split all the pages of a PDF into independent files
def pdf_splitter(pdf):
    reader = PyPDF2.PdfReader(pdf)
    for i in range(len(reader.pages)):
        writer = PyPDF2.PdfWriter()
        writer.add_page(reader.pages[i])
        with open(f'page-{i+1}_{deleteFileExtension(pdf)}.pdf', 'wb') as new_file:
            writer.write(new_file)

# function to delete pages of a PDF
def pdf_deleter(pdf, to_delete):
    reader = PyPDF2.PdfReader(pdf)
    writer = PyPDF2.PdfWriter()
    for i in range(len(reader.pages)):
        if i+1 not in to_delete:
            writer.add_page(reader.pages[i])
    with open(f'{deleteFileExtension(pdf)}_shorter.pdf', 'wb') as new_file:
        writer.write(new_file)

# function to rearrange pages of a PDF
def pdf_rearranger(pdf, page_order):
    reader = PyPDF2.PdfReader(pdf)
    writer = PyPDF2.PdfWriter()
    for i in page_order:
        writer.add_page(reader.pages[i-1])
    with open('rearranged.pdf', 'wb') as new_file:
        writer.write(new_file)

# ask the user what they want to do
print('What do you want to do?')
print('1. Merge PDFs')
print('2. Rotate PDFs')
print('3. Split PDFs')
print('4. Delete pages of a PDF')
print('5. Rearrange pages of a PDF')
# get the user's choice
choice = int(input('Enter the number of your choice: '))

# if the user wants to merge PDFs
if choice == 1:
    num_of_pdfs = int(input('How many PDFs do you want to manipulate? '))
    inputs = []
    for pdf in range(num_of_pdfs):
        pdf_name = input('Enter the name of the PDF: ')
        inputs.append(deleteFileExtension(pdf_name) + '.pdf')
    pdf_combiner(inputs)

else:
    fileName = input('Enter the name of the PDF: ')

    # if the user wants to rotate PDFs
    if choice == 2:
        print('How much do you want to rotate the PDF (clockwise)?')
        print('1. 90 degrees')
        print('2. 180 degrees')
        print('3. 270 degrees')
        rotation = int(input('Option: '))
        if 1 <= rotation <= 3: 
            pdf_rotator(fileName, 90 if rotation == 1 else 180 if rotation == 2 else 270)

    # if the user wants to split PDFs
    elif choice == 3:
        pdf_splitter(fileName)

    # if the user wants to delete pages of a PDF
    elif choice == 4:
        pages = input('Which pages do you want to delete? (separate with commas) ')
        pages = pages.split(',')
        pages = [int(page) for page in pages]
        # call the function
        pdf_deleter(fileName, pages)

    # if the user wants to rearrange pages of a PDF
    elif choice == 5:
        page_order = input('What is the new order of the pages? (separate with commas) ')
        page_order = page_order.split(',')
        page_order = [int(page) for page in page_order]
        pdf_rearranger(fileName, page_order)

    # if the user enters an invalid choice
    else:
        print('Invalid choice')

# end of program