import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = csv.DictReader(open(INPUT_FILENAME, mode='r', encoding='utf-8'), delimiter=',', lineterminator='\n')
    res=[]
    for row in data:
        res.append(row)

    data_js = json.dump(res, open(OUTPUT_FILENAME, mode='w', encoding='utf-8'), indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
