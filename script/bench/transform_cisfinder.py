#!/usr/bin/env python3

import sys
import numpy as np
import argparse

def main():
    
    description = 'Transform cis_finder output to meme minimal output format'

    # Initiate a ArgumentParser Class
    parser = argparse.ArgumentParser(description=description)

    # Call add_options to the parser
    parser.add_argument('cis_finder_file',
                        help='input cis_finder test output file')
    parser.add_argument('minimal_meme_file',
                        help='output in minimal meme format')

    args = parser.parse_args(sys.argv[1:])

    input_file = args.cis_finder_file
    output_file = args.minimal_meme_file

    processed_hits = []
    with open(input_file) as fh:
        header = None
        matrix_lines = []
        for line in fh:
            line = line.strip()
            if line.startswith("Headers:"):
                continue
            # is header line
            elif len(line) > 0 and line[0] == ">":
                if header is not None:
                    processed_hits.append(process(header, matrix_lines))
                header = line
                matrix_lines = []
            elif len(line) > 0:
                matrix_lines.append(line)
        if header is not None:
            processed_hits.append(process(header, matrix_lines))

    print_meme(processed_hits, output_file)


def print_meme(hits, output_file):
    with open(output_file, "w") as fh:
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

        for p in hits:
            if p is None:
                continue
            iupac_identifier = p[0]
            matrix = p[1]

            print("MOTIF {}".format(iupac_identifier), file=fh)
            print(("letter-probability matrix: alength= {} w= {} "
                   "nsites= {} bg_prob= {} log(Pval)= {} "
                   "zoops_score= {} mops_score= {}").format(
                   4, len(matrix), 0, 0, 0, 0, 0), file=fh)

            for line in matrix:
                print(" ".join(['{:.4e}'.format(x) for x in line]), file=fh)
            print(file=fh)


def process(header, matrix_lines):
    tokens = header[1:].strip().split()
    iupac_identifier = tokens[1]

    pattern_length = len(matrix_lines)
    matrix = np.zeros((pattern_length, 4))

    for i, row in enumerate(matrix_lines):
        values = row.strip().split()[1:]
        for a in range(4):
            matrix[i][a] = float(values[a])
        s = np.sum(matrix[i])
        matrix[i] /= s

    if np.any(np.isnan(matrix)):
        return None

    return (iupac_identifier, matrix)


if __name__ == "__main__":
    main()
