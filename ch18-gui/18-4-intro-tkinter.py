import tkinter as tk


def main():
    greetings = ["GUIs are great", "Python rocks!", "Engage!"]
    for greeting in greetings:
        window = tk.Tk()
        greet = tk.Label(text=greeting)
        greet.pack()
        window.mainloop()


if __name__ == '__main__':
    main()
