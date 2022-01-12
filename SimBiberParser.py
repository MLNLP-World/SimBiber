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
    parser.add_argument('--input_path', type=str, default="./data/bib.bib")
    parser.add_argument('--output_path', type=str, default="")
    parser.add_argument('--config_path', type=str, default="./config")
    parser.add_argument('--if_append_output', type=str2bool, default='False')
    parser.add_argument('--cache_num', type=int, default=100)
    parser.add_argument('--remove_duplicate', type=str2bool, default='False')
    args = parser.parse_args()
    sim_biber = SimBiber(args)
    sim_biber.simplify()
