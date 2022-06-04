import json


def get_data(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        return json.load(f)


def insert_data(data,file_name):
    with open(file_name, 'w', encoding='utf8') as f:
        data = json.dumps(data, indent=4)
        f.write(data)
