from argparse import ArgumentParser
import Simbiber
import sys
import os

from Simbiber.SimBiberTool import SimBiberTool
filepath = os.path.dirname(os.path.abspath(__file__)) + '/'

def main():
    def str2bool(v):
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            return False

    parser = ArgumentParser()
    parser.add_argument("-i", '--input_path', type=str, default=filepath+"data/bibtex.bib")
    parser.add_argument("-o", '--output_path', type=str, default=filepath+"out/bibtex.bib")
    parser.add_argument("-c", '--config_path', type=str, default=filepath+"config")
    parser.add_argument("-a",'--if_append_output', type=str2bool, default='False')
    parser.add_argument("-cch", '--cache_num', type=int, default=100)
    parser.add_argument("-r", '--remove_duplicate', type=str2bool, default='False')
    args = parser.parse_args()
    sim_biber = SimBiberTool(args)
    sim_biber.simplify()


if __name__ == '__main__':
    main()