"""Argparse Example

Script that reads arguments and prints them.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('foo')
args = parser.parse_args()
print(f'argument "foo" has the value "{args.foo}"')

