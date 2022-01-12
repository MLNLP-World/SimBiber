import sys
import time

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
import json
import re
import os
class Bib:
    # Assume that bib_string has valid structure
    def __init__(self, args):
        self.args = args
        self.dictionary={}
        self.bib_database = None
        self.index=0
        self.pattern_list = self.read_pattern_config()

    def get_bib_text(self):
        return bibtexparser.dumps(self.bib_database)

    def read_pattern_config(self):
        pattern_list={}
        if os.path.isdir(self.args.config_path):
            for root, ds, fs in os.walk(self.args.config_path):
                for f in fs:
                    with open(os.path.join(root, f), "r", encoding='utf-8') as f:
                        pattern_list.update(json.loads(f.read()))
        else:
            with open(self.args.config_path, "r", encoding='utf-8') as f:
                pattern_list = json.loads(f.read())
        return pattern_list

    def process_bar(self,percent, start_str='', end_str='', total_length=0):
        # bar = ''.join(["\033[31m%s\033[0m" % '   '] * int(percent * total_length)) + ''
        # bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent * 100) + end_str
        # print(bar, end='', flush=True)
        # sys.stdout.write(bar)
        print("\r", end="")
        i=int(percent*100)
        print("█" * (i // 2), "|Writing: {}%|100% ".format(i), end="")
        sys.stdout.flush()

    def simplify_bib(self,bib_string):
        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = True

        if self.bib_database is None:
            self.bib_database = bibtexparser.loads(bib_string, parser=parser)
        else:
            self.bib_database.entries += bibtexparser.loads(bib_string, parser=parser).entries



        while self.index < len(self.bib_database.entries):
            # if self.args.remove_duplicate:
            #     self.process_bar(index/len(self.bib_database.entries), start_str='', end_str='100%', total_length=15)
            item=self.bib_database.entries[self.index]
            if 'archiveprefix' in item:
                self.bib_database.entries[self.index]['archivePrefix'] = self.bib_database.entries[self.index]['archiveprefix']
                del self.bib_database.entries[self.index]['archiveprefix']
                if 'primaryclass' in item:
                    self.bib_database.entries[self.index]['primaryClass'] = self.bib_database.entries[self.index]['primaryclass']
                    del self.bib_database.entries[self.index]['primaryclass']
                self.index+=1
                continue
            if 'author' not in item:
                self.index += 1
                continue
            self.bib_database.entries[self.index] = {'ENTRYTYPE': item['ENTRYTYPE'],
                                                'ID': item['ID'],
                                                'author': item['author'],
                                                'title': item['title'], }
            if item['ENTRYTYPE'] == 'book':
                if 'address' in item:
                    self.bib_database.entries[self.index]['address'] = item['address']
                if 'publisher' in item:
                    self.bib_database.entries[self.index]['publisher'] = item['publisher']
                if 'year' in item:
                    self.bib_database.entries[self.index]['year'] = item['year']
                self.index += 1
                continue
            if 'booktitle' in item:
                booktitle = item['booktitle'].replace('\n', ' ').replace('\&', 'and')
                booktitle = booktitle.replace('{', '').replace('}', '').replace('  ', ' ').replace('[', '').replace(']', '')
                for key in self.pattern_list.keys():
                    m = re.search(key, booktitle)
                    if m is not None:
                        booktitle = 'Proc. of ' + self.pattern_list[key]
                        break
                self.bib_database.entries[self.index]['booktitle'] = booktitle
            if ('year' in item):
                self.bib_database.entries[self.index]['year'] = item['year']
            if self.args.remove_duplicate and 'booktitle' in item:
                if item['title'].lower() in self.dictionary:
                    self.bib_database.entries.pop(self.dictionary[item['title'].lower()])
                else:
                    self.dictionary[item['title'].lower()]=self.index
            if 'journal' in item:
                self.bib_database.entries[self.index]['journal'] = item['journal']
                if self.args.remove_duplicate and item['journal'].lower().find('arxiv')>=0:
                    if item['title'].lower() in self.dictionary:
                        self.bib_database.entries.pop(self.index)
                        continue
                    else:
                        self.dictionary[item['title'].lower()] = self.index
                self.index += 1
                continue
            self.index += 1

    def write_to_file(self):
        writer = BibTexWriter()
        print("Writing...")
        with open(self.args.output_path, 'a', encoding='utf-8') as bibfile:
            bibfile.write(writer.write(self.bib_database))
        print("Finished...")