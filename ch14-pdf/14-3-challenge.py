from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


class PdfFileSplitter:

    def __init__(self, file_path) -> None:
        self.file_path = file_path


    # Methods
    def split(self, breakpoint: int):
        pdf_reader = PdfFileReader(str(self.file_path))
        self.writer1 = PdfFileWriter()
        for page in pdf_reader.pages[:breakpoint]:
            self.writer1.addPage(page)

        pdf_reader = PdfFileReader(str(self.file_path))
        self.writer2 = PdfFileWriter()
        for page in pdf_reader.pages[breakpoint:]:
            self.writer2.addPage(page)

    def write(self, output: str):
        self.output1 = Path().cwd() / "ch14-pdf" / f"{output}_1.pdf"
        self.output2 = Path().cwd() / "ch14-pdf" / f"{output}_2.pdf"

        with self.output1.open(mode="wb") as file:
            self.writer1.write(file)

        with self.output2.open(mode="wb") as file:
            self.writer2.write(file)


input_pdf = Path().cwd() / "ch14-pdf" / "practice_files" / "Pride_and_Prejudice.pdf"
pdf_splitter = PdfFileSplitter(input_pdf)
pdf_splitter.split(breakpoint=150)
pdf_splitter.write("mydoc_split")

