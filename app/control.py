import re
import json

def read_json(filename):
    '''Read in a json file.'''
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

class Controller(object):
    """docstring for Controller"""
    def __init__(self, intent_pattern, entity_info):
        super(Controller, self).__init__()
        self.intent_pattern = read_json(intent_pattern)
        self.entity_info = read_json(entity_info)
        

def control(cmd):
    ctrl = Controller('app/pattern/intent_pattern.json', 'app/pattern/entity_info.json')
    if cmd == 'ddd':
        cmd_string = 'lll'
    else:
        cmd_string = 'index'
    return cmd_string