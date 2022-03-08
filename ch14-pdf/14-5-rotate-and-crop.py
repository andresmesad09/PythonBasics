from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
import copy


def main():
    pdf_path = Path().cwd() / "ch14-pdf" / "practice_files" / "split_and_rotate.pdf"
    rotated_pdf = Path().cwd() / "ch14-pdf" / "rotated.pdf"

    pdf_reader = PdfFileReader(str(pdf_path))
    pdf_writer = PdfFileWriter()

    # ----
    # 1) Rotate pages in split_rotate counterclockwise 90 degress and save in rotated.pdf
    # ----

    for page in pdf_reader.pages:
        page = page.rotateCounterClockwise(90)
        pdf_writer.addPage(page)

    with rotated_pdf.open(mode="wb") as output_file:
        pdf_writer.write(output_file)

    # ----
    # 2) Using the rotated.pdf, split each page vertically in the middle. And save in split.pdf
    # ----
    split_pdf = Path().cwd() / "ch14-pdf" / "split.pdf"

    pdf_reader = PdfFileReader(str(rotated_pdf))
    print(pdf_reader.getNumPages())
    pdf_writer = PdfFileWriter()
    for page in pdf_reader.pages:
        # Create the left side witha  copy of first page
        left_side = copy.deepcopy(page)
        # Get the current coords of upperRight
        current_coords = left_side.mediaBox.upperRight
        # Divide de widht by 2 and let the height intact
        new_coords = (current_coords[0] / 2, current_coords[1])
        # Change the upper right to new coords
        left_side.mediaBox.upperRight = new_coords

        # Create right side
        right_side = copy.deepcopy(page)
        # Modify upperleft to begin where left_side ends
        right_side.mediaBox.upperLeft = new_coords

        # Add two sides to the writer
        pdf_writer.addPage(left_side)
        pdf_writer.addPage(right_side)
    
    # Create the file
    with split_pdf.open(mode="wb") as file:
        pdf_writer.write(file)


if __name__ == '__main__':
    main()