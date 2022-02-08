from email.encoders import encode_noop
import pathlib


def main():
    file_path = pathlib.Path().cwd() / "ch12-file-input-and-output" / "starships.txt"
    with file_path.open(mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            print(line, end='')
    
    print('\n')

    with file_path.open(mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            if line.startswith('D'):
                print(line, end = '')


if __name__ == '__main__':
    main()