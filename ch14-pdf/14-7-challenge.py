from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


def get_page_text(page):
    return page.extractText()


def main():
    pdf_path = Path().cwd() / "ch14-pdf" / "practice_files" / "scrambled.pdf"
    output_pdf = Path().cwd() / "ch14-pdf" / "unscrambled.pdf"
    pdf_reader = PdfFileReader(str(pdf_path))
    pdf_writer = PdfFileWriter()

    pdf_reader = PdfFileReader(str(pdf_path))
    pdf_writer = PdfFileWriter()

    pages = list(pdf_reader.pages)
    pages.sort(key=get_page_text)

    for page in pages:
        rotation_degrees = page["/Rotate"]
        if rotation_degrees != 0:
            page.rotateCounterClockwise(rotation_degrees)
        pdf_writer.addPage(page)

    with output_pdf.open(mode="wb") as output_file:
        pdf_writer.write(output_file)


if __name__ == '__main__':
    main()
