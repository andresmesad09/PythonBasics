from importlib.util import find_spec
from pathlib import Path
from PyPDF2 import PdfFileReader


def main():
    pdf_path = Path().cwd() / "ch14-pdf" / "practice_files" / "Pride_and_Prejudice.pdf"
    # 1) Create a PdfFileReader instance from the PDF
    pdf_reader = PdfFileReader(str(pdf_path))

    # 2) Print the number of pages
    num_pages = pdf_reader.getNumPages()
    print(f"Pages in file are: {num_pages}")

    # 3) Print the file from the first page
    first_page = pdf_reader.getPage(0)
    text_first_page = first_page.extractText()
    print(text_first_page)


if __name__ == '__main__':
    main()
