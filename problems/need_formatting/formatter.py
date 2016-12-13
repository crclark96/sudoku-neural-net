#!/usr/bin/python

import sys

try:
    sys.argv[1]
except:
    print "usage: ./formatter.py <filename>"
    sys.exit()

filename = sys.argv[1]
infile = open(filename, 'r')
outfile = open(filename[:len(filename)-3] + 'edit.txt', 'w')

line = infile.readline()
while(line != '\n' and line != ''):
    l = list(line)
    for i in range(len(l)):
        if l[i] == '0':
            l[i] = '.'
    for i in l:
        outfile.write(i)
    line = infile.readline()

outfile.write('n')

infile.close()
outfile.close()
