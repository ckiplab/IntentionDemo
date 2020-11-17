import sys
import json
def read_json(filename):
    '''Read in a json file.'''
    with open(filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def write_json(filename,data):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(data, fp)

a = read_json('app/pattern/entity_info.json')
b = {}

for k, v in a.items():
    print(v[1])
    b[k] = [v[0], [l.replace('+', '\+').replace('.', '\.').replace('*', '\*').replace('(', '\(').replace(')', '\)').replace('=', '\=') for l in v[1]]]
write_json('ent.json', b)