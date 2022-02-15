import pathlib
import csv
from statistics import mode

numbers = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
]

favorite_colors = [
    {'name': 'Joe', 'favorite_color': 'blue'},
    {'name': 'Anne', 'favorite_color': 'green'},
    {'name': 'Bailey', 'favorite_color': 'red'},
]


def main():
    # ----
    # 1) Write numbers in csv file
    # ----
    file_path = pathlib.Path().cwd() / "ch12-file-input-and-output" / "numbers.csv"
    with file_path.open(mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for list in numbers:
            writer.writerow(list)

    # ----
    # 2) Read rumbers
    # ----
    numbers_readed = []
    with file_path.open(mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            int_row = [int(num) for num in row]
            numbers_readed.append(int_row)
        print(numbers_readed)

    # ----
    # 3) 
    # ----
    file_headers_path = pathlib.Path().cwd() / "ch12-file-input-and-output" / "favorite_colors.csv"
    with file_headers_path.open(mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=favorite_colors[0].keys())
        writer.writeheader()
        writer.writerows(favorite_colors)


    # ----
    # 4)
    # ----
    fav_colors_read = []
    with file_headers_path.open(mode='r', encoding='utf-8', newline='') as file:
        dict_reader = csv.DictReader(file)
        for row in dict_reader:
            fav_colors_read.append(row)
        print(fav_colors_read)

if __name__ == '__main__':
    main()