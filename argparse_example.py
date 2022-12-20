"""Argparse Example

Script that reads arguments and prints them.
"""
import argparse

parser = argparse.ArgumentParser()
argument_group = parser.add_mutually_exclusive_group()
parser.add_argument('foo', help='first named/positional argument', default='bar')
parser.add_argument('int', help='named/positional non-string argument (type: int)', type=int, choices=list(range(5)))
parser.add_argument('-o', '--opt', help='optional argument')
parser.add_argument('-f', '--flag', help='optional flag, True when given, False otherwise', action='store_true')
parser.add_argument('-c', '--cnt', help='optional flag, counts occurences', action='count', default=0)
argument_group.add_argument('-v', '--verbose', help='optional flag, counts verbosity', action='count', default=0)
argument_group.add_argument('-q', '--quiet', help='optional flag, mutual exclusive with --verbose', action='store_true')
args = parser.parse_args()

if args.verbose >= 2:
    print(f"Running '{__file__}'")
if args.verbose >= 1:
    for arg, val in vars(args).items():
        print(f'...argument "{arg}" has the value "{val}"')


