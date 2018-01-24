#!/usr/bin/env python

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

def defang(line):
    clean_line = line
    for match in RE_URLS.finditer(line):
        clean = ''
        if match.group('protocol'):
            clean += match.group('protocol').replace('t', 'X')
            clean += '://'
        clean += match.group('hostname')
        clean += match.group('tld').replace('.', '[.]')
        clean_line = clean_line.replace(match.group(1), clean)
    return clean_line
    
def defanger(infile, outfile):
    for line in infile:
        clean_line = defang(line)
        outfile.write(clean_line)

def refang(line):
    dirty_line = re.sub(r'\[((\.)|((dot)|DOT))\]', '.', line)
    if re.match(r'^h([x]{2}|[X]{2})p(s)*:', dirty_line):
        dirty_line = re.sub(r'^h([x]{2}|[X]{2})p', 'http', dirty_line)
    if re.match(r'^f([x]{1}|[X]{1})p:', dirty_line):
        dirty_line = re.sub(r'^f([x]{1}|[X]{1})p', 'ftp', dirty_line)
    return dirty_line
    
def refanger(infile, outfile):
    for line in infile:
        dirty_line = refang(line)
        outfile.write(dirty_line)
