from tqdm import tqdm

from utils.Bib import Bib


class SimBiber():
    def __init__(self, args):
        self.args = args

    def init(self):
        with open(self.args.output_path, 'w', encoding='utf-8') as bibfile:
            bibfile.write('')

    def __simplify_and_write__(self,s):
        bib = Bib(self.args, s)
        bib.simplify_bib()
        bib.write_to_file()

    def simplify(self):
        if not self.args.if_append_output:
            self.init()
        with open(self.args.input_path, encoding='utf-8') as bibtex_file:
            l = []
            s = ''
            index = 0
            for line in tqdm(bibtex_file.readlines()):
                # ignore useless line
                if len(l) == 0 and line[0] != '@':
                    continue
                for i, x in enumerate(line):
                    if x == '{':
                        l.append('{')
                    elif x == '}':
                        l.pop()
                s += line
                if len(l) == 0:
                    index += 1
                if len(l) == 0 and index == self.args.cache_num:
                    self.__simplify_and_write__(s)
                    s = ''
                    index = 0
            if index != 0:
                self.__simplify_and_write__(s)