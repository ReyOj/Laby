import json
# TODO решите задачу
filename = 'input.json'
def task() -> float:
    file = open(filename, mode='r', encoding='utf-8')
    data = json.load(file)
    res = 0
    for i in data:
        res+=i['score']*i['weight']
    return round(res, 3)


print(task())
