import PyPDF2
import os

edited_pdf_path = '.editing.pdf'

def deleteFileExtension(fileName):
    return fileName[:-4] if len(fileName) > 4 and fileName[-4:] == '.pdf' else fileName

# Function to get the number of pages in a PDF file
def get_num_pages(pdf):
    reader = PyPDF2.PdfReader(pdf)
    return len(reader.pages)

# Function to merge PDFs and save as '.editing.pdf'
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    os.system(f'attrib -h "{edited_pdf_path}"')
    merger.write(edited_pdf_path)
    os.system(f'attrib +h "{edited_pdf_path}"')
    return edited_pdf_path  # Return the path of the merged PDF

# Function to rotate PDFs and save as '.editing.pdf'
def pdf_rotator(pdf, pages_to_rotate, rotation_degrees):
    reader = PyPDF2.PdfReader(pdf)
    writer = PyPDF2.PdfWriter()
    for i in range(len(reader.pages)):
        if i + 1 in pages_to_rotate:
            writer.add_page(reader.pages[i].rotate(rotation_degrees))
        else:
            writer.add_page(reader.pages[i])
    os.system(f'attrib -h "{edited_pdf_path}"')
    with open(edited_pdf_path, 'wb') as new_file:
        writer.write(new_file)
    os.system(f'attrib +h "{edited_pdf_path}"')
    return edited_pdf_path  

# Function to delete pages of a PDF and save as '.editing.pdf'
def pdf_deleter(pdf, to_delete):
    reader = PyPDF2.PdfReader(pdf)
    writer = PyPDF2.PdfWriter()
    for i in range(len(reader.pages)):
        if i + 1 not in to_delete:
            writer.add_page(reader.pages[i])
    os.system(f'attrib -h "{edited_pdf_path}"')
    with open(edited_pdf_path, 'wb') as new_file:
        writer.write(new_file)
    os.system(f'attrib +h "{edited_pdf_path}"')
    return edited_pdf_path  

# Function to rearrange pages of a PDF and save as '.editing.pdf'
def pdf_rearranger(pdf, page_order):
    reader = PyPDF2.PdfReader(pdf)
    writer = PyPDF2.PdfWriter()
    for i in page_order:
        writer.add_page(reader.pages[i - 1])
    os.system(f'attrib -h "{edited_pdf_path}"')
    with open(edited_pdf_path, 'wb') as new_file:
        writer.write(new_file)
    os.system(f'attrib +h "{edited_pdf_path}"') 
    return edited_pdf_path  

# Function to rename and move a PDF file to a different location
def rename_and_move_pdf(old_path, new_name, new_location):
    if os.path.exists(old_path):
        os.system(f'attrib -h "{edited_pdf_path}"')
        new_path = os.path.join(new_location, new_name)
        
        # Close the file before renaming
        try:
            with open(old_path, 'rb') as pdf_file:
                with open(new_path, 'wb') as new_file:
                    new_file.write(pdf_file.read())
            os.remove(old_path)  # Delete the old file
            return new_path
        except Exception as e:
            print(f"Error renaming and moving the file: {e}")
            return None
    else:
        return None  # File does not exist

# Function to delete a PDF file
def delete_pdf(pdf_path):
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
