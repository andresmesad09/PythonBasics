import enum
from multiprocessing.sharedctypes import Value
import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter


def main():

    # 1 - Ask the user to select a PDF File to open
    pdf_path = gui.fileopenbox(
        msg="Select the PDF file", default="*.pdf", title="Select the file"
    )
    # 2 - if no pdf file is chosen, then exit the program
    if pdf_path is None:
        gui.msgbox("Now you need to restart the program. And next time, chose a file")
        exit()

    # 3 to 7 - Ask for a starting page number
    pdf_reader = PdfFileReader(pdf_path)
    num_pages = pdf_reader.getNumPages()

    selected_pages = []
    for i in range(2):
        if i == 0:
            msg = f"Select a starting page. The doc has {num_pages} pages"
            title = f"Select a starting page"
        else:
            msg = f"Select an ending page. The doc has {num_pages} pages"
            title = f"Select an ending page"

        try:
            page = gui.enterbox(
                msg=msg,
                title=title
            )
            while i == 1 and int(page) < selected_pages[0]:
                gui.msgbox(f"{page} is less than {selected_pages[0]}. Try it again")
                page = gui.enterbox(
                    msg=msg,
                    title=title
                )
            while int(page) <= 0 or int(page) > num_pages:
                gui.msgbox(f"{page} is not in the range of  1-{num_pages}. Try it again")
                page = gui.enterbox(
                    msg=msg,
                    title=title
                )
        except ValueError:
            gui.msgbox(f"{page} is not a valid page number")
            exit()
        except TypeError:
            gui.msgbox("You must insert a valid page number")
            exit()

        if page is None:
            gui.msgbox("Without page numbers I can't do anything")
            exit()

        selected_pages.append(int(page))

    # 9 - Ask for the location to sabe the extracted pages
    output_path = gui.filesavebox(
        msg="Pick destination file",
        title="output file",
        default=".pdf"
    )
    # 10 - If the user doesn't select a save location, exit the program
    if output_path is None:
        gui.msgbox("Now you need to restart the program. And next time, chose a destination file")
        exit()

    # 11 - Check output and original pdf aren't the same
    while output_path == pdf_path:
        gui.msgbox("pick a different file")
        output_path = gui.filesavebox(
            msg="Pick destination file",
            title="output file",
            default=".pdf"
        )

    # 12 - Perform the page extraction
    start_idx, end_idx = selected_pages
    # create instance for PdfFileWriter
    pdf_writer = PdfFileWriter()
    for page in pdf_reader.pages[start_idx-1:end_idx]:
        pdf_writer.addPage(page)

    # create the new file
    with open(output_path, mode="wb") as output_file:
        pdf_writer.write(output_file)

    gui.msgbox(f"Check your finder/exploerer.\n {output_path} was created")


if __name__ == "__main__":
    main()
