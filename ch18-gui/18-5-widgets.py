import tkinter as tk


def main():

    # ----
    # 1) Recreate
    # ----
    border_effects = {
        "FLAT": tk.FLAT,
        "SUNKEN": tk.SUNKEN,
        "RAISED": tk.RAISED,
        "GROOVE": tk.GROOVE,
        "RIDGE": tk.RIDGE,
    }
    window = tk.Tk()

    for relief_name, relief in border_effects.items():
        frame = tk.Frame(master=window, relief=relief, borderwidth=5)
        frame.pack(side=tk.TOP)
        label = tk.Label(text=relief_name, master=frame)
        label.pack()

    window.mainloop()

    # ----
    # 2) Button: Click me
    # ----
    window = tk.Tk()
    button = tk.Button(
        text="Click me",
        bg="white",
        fg="blue"
    )
    button.pack()
    window.mainloop()

    # ----
    # 4) Entry widget and insert what is your name?
    # ----
    window = tk.Tk()
    entry = tk.Entry(
        width=40,
        bg="white",
        fg="black"
    )
    entry.insert(0, 'What is your name?')
    entry.pack()
    window.mainloop()


if __name__ == '__main__':
    main()
