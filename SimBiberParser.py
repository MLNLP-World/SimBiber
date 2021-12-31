from argparse import ArgumentParser

from utils.SimBiber import SimBiber

if __name__ == '__main__':
    def str2bool(v):
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            return False

    parser = ArgumentParser()
    parser.add_argument('--input_path', type=str, default="./data/custom.bib")
    parser.add_argument('--output_path', type=str, default="./out/custom.bib")
    parser.add_argument('--config_path', type=str, default="./parserConfig.json")
    parser.add_argument('--if_append_output', type=str2bool, default='False')
    parser.add_argument('--cache_num', type=int, default=100)
    args = parser.parse_args()
    sim_biber = SimBiber(args)
    sim_biber.simplify()
