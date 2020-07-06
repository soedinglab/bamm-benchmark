#!/usr/bin/env python

import os
import sys
import argparse
import numpy as np

def main():
    
    description = 'Transform MEME text output to meme minimal output format'

    # Initiate a ArgumentParser Class
    parser = argparse.ArgumentParser(description=description)

    # Call add_options to the parser
    parser.add_argument('ifile',
                        help='input meme matrix file')
    parser.add_argument('--prefix',
                        help='prefix for output file')

    args = parser.parse_args(sys.argv[1:])

    ifile = args.ifile
    prefix = args.prefix

    convert_meme(ifile, prefix)


def convert_meme(ifile, prefix='new_meme'):
    
    odir = os.path.dirname(ifile)
    if not odir:
        odir = './'
    suffix = ".meme"
    ofile = odir + '/' + prefix + suffix
    fw = open(ofile, "w")
    print("MEME version 4", file=fw)
    print(file=fw)

    print("ALPHABET= ACGT", file=fw)
    print(file=fw)

    print("Background letter frequencies", file=fw)

    nmotif = 0
    with open(ifile) as fh:
        for line in fh:
            line = line.strip()
            if line.startswith("Background letter frequencies"):
                row = fh.readline().strip()
                print(row, file=fw)
                print(file=fw)

            if line.startswith("letter-probability matrix"):
                nmotif += 1
                print("MOTIF "+str(nmotif), file=fw)
                print(line, file=fw)
                w = line.split(" ")[5]
                for ln in range(int(w)):
                    row = fh.readline().strip()
                    print(row, file=fw)
                print(file=fw)

    fw.close()
    
    
if __name__ == "__main__":
    main()
