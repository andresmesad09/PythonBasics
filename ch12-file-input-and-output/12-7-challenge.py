import pathlib
import csv


def main():
    file_path = pathlib.Path().cwd() / "ch12-file-input-and-output" / "scores.csv"
    target_file = pathlib.Path().cwd() / "ch12-file-input-and-output" / "high_scores.csv"

    # ----
    # Get the max scores for each player
    # ----
    target_dict = {}
    with file_path.open(mode='r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)
        for row in reader:
            if row['name'] in target_dict and row['score'] > target_dict[row['name']]:
                target_dict[row['name']] = row['score']
            elif row['name'] in target_dict and row['score'] < target_dict[row['name']]:
                continue
            else:
                target_dict[row['name']] = row['score']

    print(target_dict)

    target_list = []
    for k,v in target_dict.items():
        temp_dict = {
            'name': k,
            'high_score': v
        }
        target_list.append(temp_dict)
    print(target_list[0].keys())

    with target_file.open(mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=target_list[0].keys())
        writer.writeheader()
        writer.writerows(target_list)

if __name__ == '__main__':
    main()