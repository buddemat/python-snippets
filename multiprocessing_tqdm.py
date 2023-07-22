#!/usr/bin/env python3
'''
Small example that uses multiprocessing to count the lines of separate *.py files in parallel, displays a progress bar, and finally prints the sum of the lines. Uses 3 cores in parallel by default.
'''
from multiprocessing import Pool
import glob
import tqdm
import time

def process_file(file):
    '''Load file and count its lines.'''
    #print(file)
    with open(file, 'r') as f:
        time.sleep(1)
        for count, line in enumerate(f):
            pass
        #print(f'Total lines in "{f}" are {count + 1}')
        return count + 1

if __name__ == '__main__':
    mypath = "."
    fileslist = glob.glob('*.py')
    filenum = len(fileslist)

    with Pool(3) as p:
        # from https://stackoverflow.com/a/45276885/14015737
        # the enclosing 'list()' statement waits for the iterator to end
        # 'total' is mandatory as tqdm does not know the length of the iteration
        r = list(tqdm.tqdm(p.imap(process_file, fileslist), total=filenum))
    print(f'The sum of all lines in {filenum} .py files is {sum(r)}.')
