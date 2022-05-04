import tkinter as tk
import numpy as np


def main():

    window = tk.Tk()

    window.title("Address Entry Form")
    window.geometry('600x500')

    fields = [
        "First Name",
        "Last Name",
        "Address Line 1",
        "Address Line 2",
        "City",
        "State/Province",
        "Postal Code",
        "Country",
    ]

    list_of_rows = list(np.arange(len(fields) + 1))

    window.rowconfigure(list_of_rows, minsize=50)
    window.columnconfigure([0, 1, 2], minsize=100)

    for field, row in zip(fields, list_of_rows[:-2]):
        label1 = tk.Label(text=f"{field}:")
        label1.grid(row=row, column=0, sticky="e")

        entry = tk.Entry(
            width=40,
            bg="white",
            fg="black"
        )
        entry.grid(row=row, column=1, sticky="we")

    button = tk.Button(
        text="Clear",
        bg="gray",
        fg="blue"
    )
    button.grid(row=list_of_rows[-1], column=1, sticky="nse")

    button2 = tk.Button(
        text="Submit",
        bg="gray",
        fg="blue"
    )
    button2.grid(row=list_of_rows[-1], column=2, sticky="nwes")

    window.mainloop()


if __name__ == '__main__':
    main()
