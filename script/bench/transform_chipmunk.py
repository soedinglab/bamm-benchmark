#!/usr/bin/env python3

import sys
import numpy as np

def main():
    import argparse
    description = 'Transform ChIPMunk output to meme minimal output format'

    # Initiate a ArgumentParser Class
    parser = argparse.ArgumentParser(description=description)

    # Call add_options to the parser
    parser.add_argument('chipmunk_matrix_file',
                        help='input chipmunk matrix file')
    parser.add_argument('minimal_meme_file',
                        help='output in minimal meme format')

    args = parser.parse_args(sys.argv[1:])

    input_file = args.chipmunk_matrix_file
    output_file = args.minimal_meme_file

    processed_hits = []
    with open(input_file) as fh:
        for line in fh:
            line = line.strip()

            if line.startswith("A|"):
                values = line[2:].split()
                pattern_length = len(values)
                matrix = np.zeros((pattern_length, 4))
                for idx, val in enumerate(values):
                    matrix[idx][0] = float(val)
            elif line.startswith("C|"):
                values = line[2:].split()
                for idx, val in enumerate(values):
                    matrix[idx][1] = float(val)
            elif line.startswith("G|"):
                values = line[2:].split()
                for idx, val in enumerate(values):
                    matrix[idx][2] = float(val)
            elif line.startswith("T|"):
                values = line[2:].split()
                for idx, val in enumerate(values):
                    matrix[idx][3] = float(val)
            elif line.startswith("IUPA|"):
                iupac_identifier = line.split("|")[1]

                # get frequencies in matrix
                for i in range(len(matrix)):
                    s = sum(matrix[i])
                    matrix[i] /= s

                processed_hits.append((iupac_identifier, matrix))

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


if __name__ == "__main__":
    main()
