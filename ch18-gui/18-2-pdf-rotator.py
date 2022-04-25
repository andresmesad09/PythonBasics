import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter


def output_gui():
    output_pdf = gui.filesavebox(
        msg="Select destination file",
        title="Select output file",
        default='*.pdf'
    )
    return output_pdf


def indexbox_gui():
    rotate_by = gui.buttonbox(
        msg="Select one option to rotate the doc",
        title="Selecting degrees",
        choices=('90', '180', '270')
    )
    return rotate_by


def main():
    # ----
    # 1) Display a file selection dialog
    # ----
    input_path = gui.fileopenbox(
        title="Select a PDF to rotate",
        default='*.pdf'
    )

    # ----
    # 2) If the user cancels the dialog, then exit the program
    # ----
    if input_path is None:
        exit()

    # ----
    # 3) Ask the user to select 90, 180 or 270
    # ----
    rotate_by = indexbox_gui()

    while rotate_by is None:
        gui.msgbox(msg="You should select an option")
        rotate_by = indexbox_gui()

    degrees = int(rotate_by)

    # ----
    # 4) Display a file selection dialog for saving the rotated PDF
    # ----
    output_pdf = output_gui()

    # ----
    # 5) Check if they are the same
    # ----
    while input_path == output_pdf:
        gui.msgbox(msg="Files can't be the same", title="Alert")
        # Returns to step 4
        output_pdf = output_gui()

    print(output_pdf)

    # ----
    # 6) If the user cancels the file save dialog, then exit the program
    # ----
    if output_pdf is None:
        gui.msgbox(msg="You must select an output file", title="Alert")
        exit()

    # ----
    # 7) Perform the page rotation
    # ----
    pdf_reader = PdfFileReader(input_path)
    pdf_writer = PdfFileWriter()

    # Rotate the page
    for page in pdf_reader.pages:
        rotated_page = page.rotateClockwise(degrees)
        pdf_writer.addPage(rotated_page)

    # Save the new file
    with open(output_pdf, mode="wb") as file:
        pdf_writer.write(file)


if __name__ == '__main__':
    main()
