from __future__ import print_function

import sys
import argparse

import numpy as np

from zigzag import zigzag_pts

class Store_as_array(argparse._StoreAction):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, np.array(values))

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='zigzag points')
    parser.add_argument("step", help="steps for all 4 axes", type=int, nargs=4, action=Store_as_array)
    return parser.parse_args(argv)

def main(args):
    args = parse_args(args)
    for pt in zigzag_pts(args.step):
        print(','.join('{: 3d}'.format(x) for x in pt))

if __name__ == '__main__':
    main(sys.argv[1:])
