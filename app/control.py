import re
import json
import pandas as pd
import numpy as np


def read_json(filename):
    '''Read in a json file.'''
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

class Controller(object):
    """docstring for Controller"""
    def __init__(self, intent_pattern, entity_info, styleme_processed, effect2ids, resp_info):
        super(Controller, self).__init__()
        self.intent_pattern = read_json(intent_pattern)
        self.entity_info = read_json(entity_info)
        self.item_info = pd.read_csv(styleme_processed, sep='\t')
        self.effect2ids = read_json(effect2ids)
        self.resp_info = read_json(resp_info)
        
        self.regex = {}
        self.prepare_regex()
        self.num_rand_product = 5
        self.neccess_info = [1, 2, 4, 6]
        self.prepare_item_regex()

    def prepare_item_regex(self):
        self.items_regex = {}
        for l in self.entity_info['item'][0]:
            str_list = []
            for item_name in self.entity_info[l][1]:
                str_list.append('(' + item_name + ')')
            self.items_regex[l] = '|'.join(str_list)

        self.brands_regex = {}
        for l in self.entity_info['brand'][0]:
            str_list = []
            for brand_name in self.entity_info[l][1]:
                str_list.append('(' + brand_name + ')')
            self.brands_regex[l] = '|'.join(str_list)

        self.effects_regex = {}
        for l in self.entity_info['effect'][0]:
            str_list = []
            for effect_name in self.entity_info[l][1]:
                str_list.append('(' + effect_name + ')')
            self.effects_regex[l] = '|'.join(str_list)

    def prepare_regex(self):
        # loop thru every items
        find_paren_exp = r'\(([\w\|]*)\)'

        for k, p_list in self.intent_pattern.items():
            self.regex[k] = []
            for p in p_list:
                # if p != "((brand_1)的)?(name)的(price|feeling|color|smell|volume|CP|url|brand_2|pic|listed_time|comment|effect|info|tips|article|texture)(是什麼|如何)":
                #     continue
                pattern = p
                m = re.findall(find_paren_exp, p)
                if m:
                    for subreg in m:
                        # if subreg[:5] == 'brand' or subreg[:4] == 'name':
                        #     continue
                        subreg_expand = subreg
                        if subreg_expand[-2:] == '_1' or subreg_expand[-2:] == '_2':
                            subreg_expand = subreg_expand[:-2]
                        
                        ent_list = subreg_expand.split('|')
                        for ent in ent_list:
                            if ent[:4] == 'name':
                                continue
                            elif ent[:5] == 'brand':
                                a = self.check_item_brand(ent)
                            else:
                                a = self.check_item(ent)
                            subreg_expand = subreg_expand.replace(ent, a)
                            # if ent == 'effect':
                            #     print('effect')
                            #     print('subre', subreg_expand)
                        pattern = pattern.replace(subreg, subreg_expand)

                try:
                    compiled = re.compile(pattern)
                except:
                    print(pattern)
                    exit(0)
                self.regex[k].append(compiled)

    def check_item(self, item):
        try:
            senses, terms = self.entity_info[item]
            # print('senses', senses)
            # print('terms', terms)
        except:
            return item
        sense_str_list = []
        
        terms = ['('+l+')' for l in terms]
        term_str = '|'.join(terms)
        if senses:
            for s in senses:
                sense_str = self.check_item(s)
                sense_str_list.append(sense_str)
            if terms:
                sense_str_list.append(term_str)
            return '|'.join(sense_str_list)
        else:
            return term_str

    def check_item_brand(self, item):
        try:
            senses, terms = self.entity_info[item]
        except:
            return item
        sense_str_list = []
        
        terms = ['('+l.replace('+', '\+').replace('.', '\.').replace('*', '\*').replace('(', '\(').replace(')', '\)').replace('=', '\=')+')' for l in terms]
        term_str = '|'.join(terms)
        if senses:
            for s in senses:
                sense_str = self.check_item_brand(s)
                sense_str_list.append(sense_str)
            if terms:
                sense_str_list.append(term_str)
            return '|'.join(sense_str_list)
        else:
            return term_str

    def check_intent(self, cmd):
        match_str = ""
        match_intent = None
        match_idx = 0
        get_item = False
        items = []
        for intent, reg_list in self.regex.items():
            for i, reg in enumerate(reg_list):
                search_str = re.search(reg, cmd)
                if search_str:
                    if len(search_str.group(0)) > len(match_str):
                        match_str = search_str.group(0)
                        match_intent = intent
                        match_idx = i
        if match_str == "":
            return "nomatch", "NO PATTERNS FOUND...", False, [], ""
        else:
            print('match_str', match_str)
            if match_intent == 'search_item':
                get_item = True
                items = self.get_items(cmd, match_idx not in [5, 6, 17], match_idx in [7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19])
                print('items', items)
                items_proc = self.process_item(items)
                print('processed', items_proc)
                items = items_proc

            return match_intent, self.intent_pattern[match_intent][match_idx], get_item, items, self.resp_info[match_intent][match_idx][0]

    def control(self, cmd):
        cmd_string, pattern_string, get_item, items, resp_string = self.check_intent(cmd)
        return cmd_string, pattern_string, get_item, items, resp_string

    def get_items(self, cmd, specify_item, brand_or_effect):
        items = self.item_info
        if specify_item:
            item_list = []
            if brand_or_effect:
                for effect, regex in self.effects_regex.items():
                    search_str = re.search(regex, cmd)
                    # means belong to a brand
                    if search_str:
                        ids = self.effect2ids[effect]
                        items = items.iloc[ids]
                        print('effect', effect)
                        break

                for brand, regex in self.brands_regex.items():
                    search_str = re.search(regex, cmd)
                    # means belong to a brand
                    if search_str:
                        items = items[items['brand'] == brand]
                        print('brand', brand)
                        break

                

            # check for if item
            for item_type, regex in self.items_regex.items():
                search_str = re.search(regex, cmd)
                # means belong to an item
                if search_str:
                    items = items[items['item'] == item_type]
                    print('item', item_type)
                    break

            

            return self.random_return(df=items, size=20)
            # else:
            #     return self.random_return(df=items, size=20)
        else:
            return self.random_return()

    def random_return(self, df=None, size=None):
        # all random
        if not isinstance(df, pd.DataFrame):
            rand_nums = np.random.randint(self.item_info.shape[0], size=self.num_rand_product)
            items = self.item_info.iloc[rand_nums, self.neccess_info]
            print(items)
            item_list = list(items.to_records(index=False))
            return item_list

        if not size:
            size = self.num_rand_product

        # if specify df
        if df.shape[0] <= size:
            return list(df.iloc[:, self.neccess_info].to_records(index=False))
        else:
            rand_nums = np.random.randint(df.shape[0], size=size)
            items = df.iloc[rand_nums, self.neccess_info]
            item_list = list(items.to_records(index=False))
            return item_list
            
    def process_item(self, items):
        if not items:
            return []
        else:
            new_items = []
            for item in items:
                if isinstance(item[1], str) and isinstance(item[3], str):
                    if isinstance(item[0], str):
                        new_items.append((item[0].replace('_', ' '), item[1], item[3]))
                    else:
                        new_items.append(('', item[1], item[3]))

            return new_items        
        


ctrl = Controller('app/pattern/intent_pattern.json', 'app/pattern/entity_info.json', 'app/pattern/styleme_new.tsv', 'app/pattern/effect2ids.json', 'app/pattern/response.json')





if __name__ == '__main__':
    ctrl = Controller('app/pattern/intent_pattern.json', 'app/pattern/entity_info.json')
    # ctrl = Controller('app/pattern/intent_pattern.json', 'ent.json')
    for k, v in ctrl.intent_pattern.items():
        print(k)
    # find_paren_exp = r'\(([\w\|]*)\)'

    # for k, p_list in ctrl.intent_pattern.items():
    #     for p in p_list:
    #         if p != "((brand_1)的)?(name)的(price|feeling|color|smell|volume|CP|url|brand_2|pic|listed_time|comment|effect|info|tips|article|texture)(是什麼|如何)":
    #             continue
    #         pattern = p
    #         m = re.findall(find_paren_exp, p)
    #         if m:
    #             # print('---------------------')
    #             # print('pattern', p)
    #             # print(m)
    #             for subreg in m:
    #                 subreg_expand = subreg
    #                 if subreg_expand[-2:] == '_1' or subreg_expand[-2:] == '_2':
    #                     subreg_expand = subreg_expand[:-2]
    #                 print('subreg', subreg_expand)
    #                 ent_list = subreg_expand.split('|')
    #                 for ent in ent_list:
    #                     a = ctrl.check_item(ent)
    #                     subreg_expand = subreg_expand.replace(ent, a)
    #                 pattern = pattern.replace(subreg, subreg_expand)

    #         # print('====')
    #         print('new pattern', pattern)
        
# 