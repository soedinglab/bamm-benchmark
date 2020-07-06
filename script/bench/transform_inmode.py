#!/usr/bin/env python3

import os
import sys
import argparse
import numpy as np

def main():
    
    description = 'Transform InMoDe output to BaMM output format'

    # Initiate a ArgumentParser Class
    parser = argparse.ArgumentParser(description=description)

    # Call add_options to the parser
    parser.add_argument('ifile',
                        help='input InMoDe output parameter file in .txt format')
    parser.add_argument('-ofile1',
                        help='output in BaMM ihbcp format')
    parser.add_argument('-ofile2',
                        help='output in BaMM ihbp format')    
    parser.add_argument('-odir',
                        help='directory for output files')
    parser.add_argument('-basename',
                        help='basename for output files')   
    parser.add_argument('-order',
                        help='order of the input model')
    parser.add_argument('-alphabet',
                        help='alphabet for the input model')  
    
    args = parser.parse_args(sys.argv[1:])

    ifile = args.ifile
    ofile1 = args.ofile1
    ofile2 = args.ofile2
    odir = args.odir
    basename = args.basename
    order = args.order
    alphabet = args.alphabet
    
    convertInMoDe2BaMM(ifile, ofile1, ofile2, odir, basename, order, alphabet)
    
    
def code2base(code):
    if code == 0:
        return 'A'
    elif code == 1:
        return 'C'
    elif code == 2:
        return 'G'
    elif code == 3:
        return 'T'
    else:
        return "Error: code is undefined!"
    
    
def base2code(base):
    if base == 'A':
        return 0
    elif base == 'C':
        return 1
    elif base == 'G':
        return 2
    elif base == 'T':
        return 3
    else:
        return "Error: base is undefined!"

    
def convertInMoDe2BaMM(ifile, ofile1='', ofile2='', odir='', basename='', order='', alphabet=''):
    
    if not ofile1:
        if not basename:
            ofile1 = os.path.splitext(ifile)[0] + '.ihbcp'
            ofile2 = os.path.splitext(ifile)[0] + '.ihbp'
        elif not odir:
            ofile1 = os.path.dirname(ifile) + '/' + basename  + '.ihbcp'
            ofile2 = os.path.dirname(ifile) + '/' + basename  + '.ihbp'
        else: 
            ofile1 = odir + '/' + basename  + '.ihbcp'
            ofile2 = odir + '/' + basename  + '.ihbp' 
            
    if not order:
        order = 2
    if not alphabet:
        alphabet = "ACGT"
        
    asize = len(alphabet)
    motif_width = open(ifile).read().count("Position")

    # define the matrix
    inmode = [[] for i in range(order+1)]
    bamm = [[] for i in range(order+1)]
    bamm_p = [[] for i in range(order+1)]
    for i in range(order+1):
        num = np.power(asize, i+1)
        bamm[i] = [[0 for i in range(num)] for j in range(motif_width)]
        bamm_p[i] = [[1 for i in range(num)] for j in range(motif_width)]
        inmode[i] = [[0 for i in range(asize)] for j in range(motif_width)]

    # read in the orignal matrix and convert it to a BaMM
    with open(ifile) as fh:
        pos = 0
        pos_2 = []
        pos_1 = []
        matrix = []
        for line in fh:
            line = line.strip()
            while line:
                if line.startswith("Position"):
                    if pos == 2:
                        for idx, line in enumerate(matrix):
                            for j_1 in pos_1[idx]:
                                for j, base in enumerate(alphabet):
                                    bamm[1][pos-1][base2code(j_1)*asize+j] = matrix[idx][j]
                                    for j_2 in range(asize):
                                        bamm[2][pos-1][j_2*asize*asize+base2code(j_1)*asize+j] = matrix[idx][j]

                        for j_1 in range(asize):
                            for j in range(asize):
                                bamm[0][pos-1][j] += float(bamm[1][pos-1][j_1*asize+j]) * float(bamm[0][pos-2][j])


                    elif pos > 2:
                        for idx, line in enumerate(matrix):
                            for j_2 in pos_2[idx]:
                                for j_1 in pos_1[idx]:
                                    for j, base in enumerate(alphabet):
                                        bamm[2][pos-1][base2code(j_2)*asize*asize+base2code(j_1)*asize+j] = matrix[idx][j]

                        for j in range(asize):
                            for j_1 in range(asize):
                                for j_2 in range(asize):
                                    bamm[1][pos-1][j_1*asize+j] += float(bamm[2][pos-1][j_2*asize*asize+j_1*asize+j])
                                bamm[1][pos-1][j_1*asize+j] /= asize # normalization 
                                bamm[0][pos-1][j] += bamm[1][pos-1][j_1*asize+j]
                            bamm[0][pos-1][j] /= asize # normalization

                    pos += 1
                    pos_2 = []
                    pos_1 = []
                    matrix = []
                    #print(line)
                elif pos > 2:
                    pattern = line.split('\t')[0]
                    key2, key1 = pattern.split('][')
                    key2 = key2[1:]
                    key1 = key1[:-1]
                    pos_2.append(key2)
                    pos_1.append(key1)
                    probs = [line.split('\t')[i+1] for i in range(asize)]
                    matrix.append(probs)
                    #print(str(pos)+'\t'+pattern)
                    #print(probs)
                elif pos == 1:
                    # read in for the first position
                    probs = [line.split('\t')[i] for i in range(asize)]
                    bamm[0][pos-1] = probs
                    for j in range(asize):
                        for j_1 in range(asize):
                            bamm[1][pos-1][j_1*asize+j] = probs[j]
                            for j_2 in range(asize):
                                bamm[2][pos-1][j_2*asize*asize+j_1*asize+j] = probs[j]
                elif pos == 2:
                    # read in for the second position
                    pattern = line.split('\t')[0]
                    probs = [line.split('\t')[i+1] for i in range(asize)]
                    matrix.append(probs)
                    key1 = pattern[1:-1]
                    pos_1.append(key1)

                    #print(str(pos)+'\t'+pattern)
                    #print(probs)
                else:
                    print("nothing reading in")
                # read in the new line
                line = fh.readline().strip()

            # for the last position:
            for idx, line in enumerate(matrix):
                for j_2 in pos_2[idx]:
                    for j_1 in pos_1[idx]:
                        for j, base in enumerate(alphabet):
                            bamm[2][pos-1][base2code(j_2)*asize*asize+base2code(j_1)*asize+j] = matrix[idx][j]

            for j in range(asize):
                for j_1 in range(asize):
                    for j_2 in range(asize):
                        bamm[1][pos-1][j_1*asize+j] += float(bamm[2][pos-1][j_2*asize*asize+j_1*asize+j])
                    bamm[1][pos-1][j_1*asize+j] /= asize # normalization 
                    bamm[0][pos-1][j] += bamm[1][pos-1][j_1*asize+j]
                bamm[0][pos-1][j] /= asize # normalization


    # calculate full probabilities
    for pos in range(motif_width):
        for a_0 in range(asize):
            bamm_p[0][pos][a_0] = bamm[0][pos][a_0]

    for a_0 in range(asize):
        for a_1 in range(asize):
            for pos in range(motif_width):
                if pos < 1:
                    bamm_p[1][pos][asize*a_1+a_0] = float(bamm[1][pos][asize*a_1+a_0]) / float(asize)
                else:
                    bamm_p[1][pos][asize*a_1+a_0] = float(bamm[1][pos][asize*a_1+a_0]) * float(bamm_p[0][pos-1][a_1]) 

    for a_0 in range(asize):
        for a_1 in range(asize):
            for pos in range(motif_width):            
                for a_2 in range(asize):
                    if pos < 2:
                        bamm_p[2][pos][a_2*np.power(asize,2)+asize*a_1+a_0] = float(bamm[2][pos][a_2*np.power(asize,2)+asize*a_1+a_0]) / float(np.power(asize,2))
                    else:
                        bamm_p[2][pos][a_2*np.power(asize,2)+asize*a_1+a_0] = float(bamm[2][pos][a_2*np.power(asize,2)+asize*a_1+a_0]) * float(bamm_p[1][pos-1][a_2*asize+a_1]) 

    with open(ofile1, 'w') as fw:
        for pos in range(motif_width):
            for k in range(order+1):
                print(" ".join(['{:.4e}'.format(float(x)) for x in bamm[k][pos]]), file=fw)
            print(file=fw)

    with open(ofile2, 'w') as fw:
        for pos in range(motif_width):
            for k in range(order+1):
                print(" ".join(['{:.4e}'.format(float(x)) for x in bamm_p[k][pos]]), file=fw)
            print(file=fw)

if __name__ == "__main__":
    main()
