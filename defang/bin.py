#!/usr/bin/env python
import sys
from defang import defanger, refanger

def defang():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--refang', '-r', action='store_true', help='refangs urls')
    parser.add_argument('-i', '--input', help='input file, default stdin')
    parser.add_argument('-o', '--output', help='output file, default stdout')
    args = parser.parse_args()
    
    try:
        if args.input:
            input_f = open(args.input)
        else:
            input_f = sys.stdin
        if args.output:
            output_f = open(args.output, 'w')
        else:
            output_f = sys.stdout
        if args.refang:
            refanger(input_f, output_f)
        else:
            defanger(input_f, output_f)
    finally:
        try:
            if args.output:
                output_f.close()
        finally:
            if args.input:
                input_f.close()

if __name__ == '__main__':
    defang()
