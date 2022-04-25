import easygui as gui


def main():
    # ----
    # 1)
    # ----
    gui.msgbox(msg="Warning!", title="Watch out!", ok_button="I'll be careful")

    # ----
    # 2)
    # ----
    name = gui.enterbox(msg="What is your name", title="")
    print(name)


if __name__ == "__main__":
    main()
