import os
import time

from tqdm import tqdm

from Simbiber.BibTool import BibTool


class SimBiberTool():
    def __init__(self, args):
        self.args = args

    def init(self):
        with open(self.args.output_path, 'w', encoding='utf-8') as bibfile:
            bibfile.write('')

    def __simplify_and_write__(self,s):
        self.bib.simplify_bib(s)


    def __rewrite__(self):
        with open(self.args.output_path, 'r', encoding='utf-8') as file1:
            with open(self.args.input_path, 'w', encoding='utf-8') as file2:
                    file2.writelines(file1.readlines())

        os.remove(self.args.output_path)


    def __simplify__(self):
        if not self.args.if_append_output and not self.use_temp_file:
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
        self.bib.remove_duplication()
        self.bib.write_to_file()
        if self.use_temp_file:
            self.__rewrite__()

    def __judge_use_temp__(self):
        self.use_temp_file = False
        if self.args.output_path == '' or self.args.output_path == self.args.input_path:
            self.use_temp_file = True
            self.args.output_path = self.args.input_path + time.strftime("%Y%m%d%H%M%S", time.localtime())

    def simplify(self):
        input_path=self.args.input_path
        if os.path.isdir(input_path):
            for root, ds, fs in os.walk(input_path):
                for f in fs:
                    self.args.input_path=os.path.join(root, f)
                    self.args.output_path = os.path.join('out', f)
                    self.bib = BibTool(self.args)
                    self.__judge_use_temp__()
                    self.__simplify__()
        else:
            self.bib = BibTool(self.args)
            self.__judge_use_temp__()
            self.__simplify__()
