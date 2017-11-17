#!/usr/bin/env python
import sys


terms = []
# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/task2breducerinput.txt', 'r')

for term in file('terms.txt'):
    terms.append(term.strip('\n'))

for line in sys.stdin:
    tokens = line.strip().split('\t')
    word = tokens[0]
    if word in terms:
        print(line)