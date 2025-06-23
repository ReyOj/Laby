import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        data = list(reader)

    with open(OUTPUT_FILENAME, "w", encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
