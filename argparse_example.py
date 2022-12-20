"""Argparse Example

Script that reads arguments and prints them.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('foo', help="First named argument", default='bar')
parser.add_argument('int', help="Named non-string argument (type: int)", type=int)
parser.add_argument('--option', help="Optional argument")
parser.add_argument('--flag', help="Optional flag, True when given, False otherwise", action="store_true")
args = parser.parse_args()
for arg, val in vars(args).items():
    print(f'argument "{arg}" has the value "{val}"')


