#!/usr/bin/env python3

import os
import sys
import argparse
import numpy as np

def main():
    
    description = 'Transform diChIPMunk output to meme and bamm output format'

    # Initiate a ArgumentParser Class
    parser = argparse.ArgumentParser(description=description)

    # Call add_options to the parser
    parser.add_argument('dichipmunk_matrix_file',
                        help='input di-chipmunk matrix file')

    args = parser.parse_args(sys.argv[1:])

    input_file = args.dichipmunk_matrix_file

    # parse matrics
    pwm_matrix, bamm_matrix, iupac_identifier, nsites = parse_matrix(input_file)

    fn = os.path.splitext(input_file)[0]
    
    pwm_ofile = fn + '.meme'
    bamm_ihbcp_file = fn + '.ihbcp'
    bamm_hbcp_file = fn + '.hbcp'

    print_meme2(pwm_matrix, iupac_identifier, nsites, pwm_ofile) 
    print_bamm(pwm_matrix, bamm_matrix, bamm_ihbcp_file, bamm_hbcp_file)
    

def parse_matrix(ifile):
    
    alphabet_size = 4
    
    # parse the di-PWM matrices
    with open(ifile) as fh:
        for line in fh:
            line = line.strip()
            if line.startswith("AA|"):
                values = line[3:].split()
                pattern_length = len(values)
                matrix = np.zeros((pattern_length, alphabet_size * alphabet_size))
                count_matrix = np.zeros((pattern_length, alphabet_size * alphabet_size))
                for idx, val in enumerate(values):
                    count_matrix[idx][0] = int(float(val))
                ln = 0 
            elif line.startswith("PW"):
                values = line[5:].split()
                for idx, val in enumerate(values):
                    matrix[idx][ln] = float(val)
                ln = ln + 1
            elif line.startswith("AC|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][1] = int(float(val))
            elif line.startswith("AG|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][2] = int(float(val))     
            elif line.startswith("AT|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][3] = int(float(val)) 
            elif line.startswith("CA|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][4] = int(float(val)) 
            elif line.startswith("CC|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][5] = int(float(val))
            elif line.startswith("CG|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][6] = int(float(val))     
            elif line.startswith("CT|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][7] = int(float(val)) 
            elif line.startswith("GA|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][8] = int(float(val))  
            elif line.startswith("GC|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][9] = int(float(val))
            elif line.startswith("GG|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][10] = int(float(val))     
            elif line.startswith("GT|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][11] = int(float(val))
            elif line.startswith("TA|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][12] = int(float(val))  
            elif line.startswith("TC|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][13] = int(float(val))
            elif line.startswith("TG|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][14] = int(float(val))     
            elif line.startswith("TT|"):
                values = line[3:].split()
                for idx, val in enumerate(values):
                    count_matrix[idx][15] = int(float(val))
            elif line.startswith("IUPA|"):
                iupac_identifier = line[5:]
            elif line.startswith("NN|"):
                nsites = int(float(line[3:]))
        
        # transform counts to matrics
        pwm_matrix = np.zeros((pattern_length, alphabet_size))
        bamm_matrix = np.zeros((pattern_length, 16 ))
        for row, vals in enumerate(count_matrix):

            for i in range(alphabet_size):
                for alp in range(alphabet_size):
                    pwm_matrix[row][alp] += vals[i*alphabet_size+alp]      

            for i in range(alphabet_size):
                sum4 = 1.e-5 # avoid dividing by zeros
                for alp in range(alphabet_size):
                    sum4 += vals[i*alphabet_size+alp]
                for alp in range(alphabet_size):
                    bamm_matrix[row][i*alphabet_size+alp] = vals[i*alphabet_size+alp] / sum4

            pwm_matrix[row] /= sum(vals) 
    return pwm_matrix, bamm_matrix, iupac_identifier, nsites
            
            
def print_meme2(matrix, iupac, nsites, ofile):
    with open(ofile, "w") as fh:
        print("MEME version 4", file=fh)
        print(file=fh)

        print("ALPHABET= ACGT", file=fh)
        print(file=fh)

        print("Background letter frequencies", file=fh)

        bg_probs = []
        for nt, value in [("A", 0.25), ("C", 0.25), ("G", 0.25), ("T", 0.25)]:
            bg_probs.append(nt)
            bg_probs.append(str(value))
        print(" ".join(bg_probs), file=fh)
        print(file=fh)

        iupac_identifier = iupac

        print("MOTIF {}".format(iupac_identifier), file=fh)
        print(("letter-probability matrix: alength= {} w= {} "
               "nsites= {} bg_prob= {} log(Pval)= {} "
               "zoops_score= {} mops_score= {}").format(
               4, len(matrix), nsites, 0, 0, 0, 0), file=fh)

        for line in matrix:
            print(" ".join(['{:.3e}'.format(x) for x in line]), file=fh)
        print(file=fh)

        
def print_bamm(pwm_matrix, bamm_matrix, ofile1, ofile2):
    with open(ofile1, "w") as fh:
        for ln, line in enumerate(bamm_matrix):
            print(" ".join(['{:.3e}'.format(x) for x in pwm_matrix[ln]]), file=fh)
            print(" ".join(['{:.3e}'.format(x) for x in line]), file=fh)
            print(file=fh)
            
    with open(ofile2, "w") as f2:
        print("# K = 2", file=f2)
        print("# A = 1 10 10", file=f2)
        mono = [0.25] * 4
        dino = [0.625] * 16
        tri  = [0.015625] * 64
        print(" ".join(['{:.4e}'.format(x) for x in mono]), file=f2)
        print(" ".join(['{:.4e}'.format(x) for x in dino]), file=f2)
        print(" ".join(['{:.4e}'.format(x) for x in tri]),  file=f2) 
        
        
if __name__ == "__main__":
    main()
