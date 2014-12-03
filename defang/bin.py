#!/usr/bin/env python
import sys
import re
from urllib2 import urlparse

# https://gist.github.com/dperini/729294
RE_URLS = re.compile(
    r'((?:(?P<protocol>https?|ftp)://)?'
    r'(?:\S+(?::\S*)?@)?'
    r'((?P<hostname>'
    r'(?!(?:10|127)(?:\.\d{1,3}){3})'
    r'(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})'
    r'(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})'
    r'(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])'
    r'(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}'
    r'(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))'
    r'|'
    r'(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)'
    r'(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*'
    r')(?P<tld>\.(?:[a-z\u00a1-\uffff]{2,}))'
    r'))'
    r'(?::\d{2,5})?'
    r'(?:/\S*)?',
    re.IGNORECASE
)

def defanger(infile, outfile):
    for line in infile.readlines():
        clean_line = line
        for match in RE_URLS.finditer(line):
            clean = ''
            if match.group('protocol'):
                clean += match.group('protocol').replace('t', 'X')
                clean += '://'
            clean += match.group('hostname').replace('.', '[.]')
            clean += match.group('tld')
            clean_line = clean_line.replace(match.group(1), clean)
        outfile.write(clean_line)

def refanger(infile, outfile):
    for line in infile.readlines():
        dirty_line = line.replace('[.]', '.')
        dirty_line = dirty_line.replace('hXXp', 'http')
        dirty_line = dirty_line.replace('fXp', 'ftp')
        outfile.write(dirty_line)

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
