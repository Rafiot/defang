#!/usr/bin/env python
import sys
import re
from urllib2 import urlparse

def defanger(infile, outfile):
    for line in infile.readlines():
        host = urlparse.urlparse(line).netloc
        clean_host = host.replace('.', '[.]')
        clean = re.sub('^http', 'hXXp', line)
        clean = clean.replace(host, clean_host)
        outfile.write(clean + '\n')

def defang():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--refang', '-r', action='store_true', help='refangs urls')
    parser.add_argument('-i', '--input', help='input file, default stdin')
    parser.add_argument('-o', '--output', help='output file, default stdout')
    args = parser.parse_args()
    
    if not args.refang:
        if args.input:
            input_f = open(args.input)
        else:
            input_f = sys.stdin
        if args.output:
            output_f = open(args.output)
        else:
            output_f = sys.stdout
        defanger(input_f, output_f)
    if args.input:
        input_f.close()
    if args.output:
        output_f.close()

if __name__ == '__main__':
    defang()
