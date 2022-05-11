from pathlib import Path
from PyPDF2 import PdfFileMerger


def main():
    # Define main directory and get the files that follow the merge_.pdf structure
    main_directory = Path().cwd() / "ch14-pdf" / "practice_files"
    concatenated_file = Path().cwd() / "ch14-pdf" / "concatenated.pdf"
    merged_file = Path().cwd() / "ch14-pdf" / "merged.pdf"
    list_pdfs = list(main_directory.glob("merge*.pdf"))
    list_pdfs.sort()

    # Create instance of PdfFileMerger
    pdf_merger = PdfFileMerger()
    # Append the first two pdf
    for pdf_file in list_pdfs[:2]:
        pdf_merger.append(str(pdf_file))

    # Save the concatenated PDFs to a file called concatenated.pdf
    with concatenated_file.open(mode="wb") as file:
        pdf_merger.write(file)

    # ----
    # 2) With a new PdfFileMerger instance, use merge to merge merge3.pdf between the two pages in the concatenated.pdf
    # ----
    pdf_merger = PdfFileMerger()
    pdf_merger.append(str(concatenated_file))
    pdf_merger.merge(1, str(list_pdfs[-1]))

    with merged_file.open(mode="wb") as file:
        pdf_merger.write(file)


if __name__ == '__main__':
    main()
