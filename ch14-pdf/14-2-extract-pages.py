from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


def main():
    input_pdf = Path().cwd() / "ch14-pdf" / "practice_files" / "Pride_and_Prejudice.pdf"
    output_pdf_last_page = Path().cwd() / "ch14-pdf" / "last_page.pdf"
    output_pdf_even = Path().cwd() / "ch14-pdf" / "every_other_page.pdf"
    output_pdf_first_150 = Path().cwd() / "ch14-pdf" / "part_1.pdf"
    output_pdf_part2 = Path().cwd() / "ch14-pdf" / "part_2.pdf"
    pdf_reader = PdfFileReader(str(input_pdf))
    pdf_writer_last_page = PdfFileWriter()
    pdf_writer_even_pages = PdfFileWriter()
    pdf_writer_first_150 = PdfFileWriter()
    pdf_writer_part2 = PdfFileWriter()

    # ----
    # 1) Last page to last_page.pdf
    # ----
    # Get the last page
    last_page = pdf_reader.pages[-1]
    # Add to the output_file
    pdf_writer_last_page.addPage(last_page)
    with output_pdf_last_page.open(mode="wb") as output_file:
        pdf_writer_last_page.write(output_file)

    # ----
    # 2) Extract all pages with even-numbered indices
    # ----
    num_pages = pdf_reader.getNumPages()
    for idx in range(num_pages):
        if idx % 2 == 0:
            page = pdf_reader.getPage(idx)
            pdf_writer_even_pages.addPage(page)
    # Add pages from writer to .pdf file
    with output_pdf_even.open(mode="wb") as output_file:
        pdf_writer_even_pages.write(output_file)

    # ----
    # 3) Split the Pride pdf into two new files
    # The first 150 pages and the rest
    # ----
    for page in pdf_reader.pages[:150]:
        pdf_writer_first_150.addPage(page)
    with output_pdf_first_150.open(mode="wb") as output_file:
        pdf_writer_first_150.write(output_file)

    for page in pdf_reader.pages[150:]:
        pdf_writer_part2.addPage(page)
    with output_pdf_part2.open(mode="wb") as output_file:
        pdf_writer_part2.write(output_file)



if __name__ == '__main__':
    main()