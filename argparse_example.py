"""Argparse Example

Script that reads arguments and prints them.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('foo', help="first named/positional argument", default='bar')
parser.add_argument('int', help="named/positional non-string argument (type: int)", type=int, choices=list(range(5)))
parser.add_argument('-o', '--opt', help="optional argument")
parser.add_argument('-f', '--flag', help="optional flag, True when given, False otherwise", action="store_true")
args = parser.parse_args()
for arg, val in vars(args).items():
    print(f'argument "{arg}" has the value "{val}"')


