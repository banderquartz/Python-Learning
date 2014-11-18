'''
Created on Nov 18, 2014

@author: mike
'''
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--n_print', type = int, help = 'number of times to print Hello, world!')
args = parser.parse_args()

if args.n_print <= 0:
    parser.print_help()
    sys.exit() 
else:
    for _ in range(args.n_print):
        print('Hello, world!')