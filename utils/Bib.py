import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
import json
import re
import os
class Bib:
    # Assume that bib_string has valid structure
    def __init__(self, args, bib_string):
        self.args = args
        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = True
        self.bib_database = bibtexparser.loads(bib_string, parser=parser)

    def reset_bib_string(self,bib_string):
        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = True
        self.bib_database = bibtexparser.loads(bib_string, parser=parser)

    def get_bib_text(self):
        return bibtexparser.dumps(self.bib_database)

    def simplify_bib(self):
        pattern_list= {}
        if(os.path.isdir(self.args.config_path)):
            for root, ds, fs in os.walk(self.args.config_path):
                for f in fs:
                    with open(os.path.join(root, f), "r", encoding='utf-8') as f:
                        pattern_list.update(json.loads(f.read()))
        else:
            with open(self.args.config_path, "r", encoding='utf-8') as f:
                pattern_list = json.loads(f.read())
        for index, item in enumerate(self.bib_database.entries):
            if 'archiveprefix' in item:
                self.bib_database.entries[index]['archivePrefix'] = self.bib_database.entries[index]['archiveprefix']
                del self.bib_database.entries[index]['archiveprefix']
                if 'primaryclass' in item:
                    self.bib_database.entries[index]['primaryClass'] = self.bib_database.entries[index]['primaryclass']
                    del self.bib_database.entries[index]['primaryclass']
                continue
            if 'author' not in item:
                continue
            self.bib_database.entries[index] = {'ENTRYTYPE': item['ENTRYTYPE'],
                                                'ID': item['ID'],
                                                'author': item['author'],
                                                'title': item['title'], }
            if item['ENTRYTYPE'] == 'book':
                if 'address' in item:
                    self.bib_database.entries[index]['address'] = item['address']
                if 'publisher' in item:
                    self.bib_database.entries[index]['publisher'] = item['publisher']
                if 'year' in item:
                    self.bib_database.entries[index]['year'] = item['year']
                continue
            if 'booktitle' in item:
                booktitle = item['booktitle'].replace('\n', ' ')
                for key in pattern_list.keys():
                    m = re.search(key, booktitle)
                    if m is not None:
                        booktitle = 'Proc. of ' + pattern_list[key]
                        break
                self.bib_database.entries[index]['booktitle'] = booktitle
            if ('year' in item):
                self.bib_database.entries[index]['year'] = item['year']

            if 'journal' in item:
                self.bib_database.entries[index]['journal'] = item['journal']
                continue

    def write_to_file(self):
        writer = BibTexWriter()
        with open(self.args.output_path, 'a', encoding='utf-8') as bibfile:
            bibfile.write(writer.write(self.bib_database))