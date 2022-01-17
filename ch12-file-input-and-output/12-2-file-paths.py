import pathlib


def main():
    path = pathlib.Path().cwd() / "ch12-file-input-and-output" / "my_folder" / "my_file.txt"
    if path.exists():
        print(f"{path} Exists")

    print(f"The name of the file in the path is: {path.name}")
    parent = str(path.parent).split('/')[-1]
    print(f"The parent of the file in the path is: {parent}")

if __name__ == '__main__':
    main()