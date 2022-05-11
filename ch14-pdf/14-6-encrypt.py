from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


def main():
    pdf_path = Path().cwd() / "ch14-pdf" / "practice_files" / "top_secret.pdf"

    # ----
    # 1) Encrypt the file with the pwd Unguessable
    # ----
    pdf_reader = PdfFileReader(str(pdf_path))
    pdf_writer = PdfFileWriter()

    pdf_writer.appendPagesFromReader(pdf_reader)
    pdf_writer.encrypt(user_pwd="Unguessable")

    # Save the encrypted file to your home directory
    output_pdf = pdf_path.parent.parent / "top_secret_encrypted.pdf"
    with output_pdf.open(mode="wb") as file:
        pdf_writer.write(file)

    # ----
    # 2) Open the encrypted file and print the text
    # ----
    pdf_reader = PdfFileReader(str(output_pdf))
    pdf_reader.decrypt("Unguessable")
    for page in pdf_reader.pages:
        print(page.extractText())


if __name__ == '__main__':
    main()
