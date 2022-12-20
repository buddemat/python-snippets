"""Argparse Example

Script that reads arguments and prints them.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('foo', default='bar', help="First argument")
parser.add_argument('int', type=int, help="Non-String argument")
args = parser.parse_args()
for arg, val in vars(args).items():
    print(f'argument "{arg}" has the value "{val}"')


