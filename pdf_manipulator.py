import PyPDF2
import os

def deleteFileExtension(fileName):
    return fileName[:-4] if len(fileName) > 4 and fileName[-4:] == '.pdf' else fileName

# Function to get the number of pages in a PDF file
def get_num_pages(pdf):
    reader = PyPDF2.PdfReader(pdf)
    return len(reader.pages)

# Function to merge PDFs and save as "editing.pdf"
def pdf_combiner(pdf_list):
    merged_pdf_path = 'editing.pdf'
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(merged_pdf_path)
    return merged_pdf_path  # Return the path of the merged PDF

# Function to rotate PDFs and save as "editing.pdf"
def pdf_rotator(pdf, pages_to_rotate, rotation_degrees):
    edited_pdf_path = 'editing.pdf'
    reader = PyPDF2.PdfReader(pdf)
    writer = PyPDF2.PdfWriter()
    for i in range(len(reader.pages)):
        if i + 1 in pages_to_rotate:
            writer.add_page(reader.pages[i].rotate(rotation_degrees))
        else:
            writer.add_page(reader.pages[i])
    with open(edited_pdf_path, 'wb') as new_file:
        writer.write(new_file)
    return edited_pdf_path  # Return the path of the edited PDF

# Function to delete pages of a PDF and save as "editing.pdf"
def pdf_deleter(pdf, to_delete):
    edited_pdf_path = 'editing.pdf'
    reader = PyPDF2.PdfReader(pdf)
    writer = PyPDF2.PdfWriter()
    for i in range(len(reader.pages)):
        if i + 1 not in to_delete:
            writer.add_page(reader.pages[i])
    with open(edited_pdf_path, 'wb') as new_file:
        writer.write(new_file)
    return edited_pdf_path  # Return the path of the edited PDF

# Function to rearrange pages of a PDF and save as "editing.pdf"
def pdf_rearranger(pdf, page_order):
    edited_pdf_path = 'editing.pdf'
    reader = PyPDF2.PdfReader(pdf)
    writer = PyPDF2.PdfWriter()
    for i in page_order:
        writer.add_page(reader.pages[i - 1])
    with open(edited_pdf_path, 'wb') as new_file:
        writer.write(new_file)
    return edited_pdf_path  # Return the path of the edited PDF

# Function to rename and move a PDF file to a different location
def rename_and_move_pdf(old_path, new_name, new_location):
    if os.path.exists(old_path):
        new_path = os.path.join(new_location, new_name)
        os.rename(old_path, new_path)
        return new_path
    else:
        return None  # File does not exist

# Function to delete a PDF file
def delete_pdf(pdf_path):
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
