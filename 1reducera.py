#!/usr/bin/env python

import sys

# fileHandle = open('/home/raven/PycharmProjects/excassignment2/r2txt', 'r');
# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/inputForReducer1a.txt', 'r')

for line in sys.stdin:
    try:
        tokens = line.strip().split('\t')
        word = tokens[0]
        numberOfAppearances = tokens[1]
        documents = tokens[2].split(';')
        filesString = ""
        for document in documents:
            fileName, count = document.split('|')
            filesString += "({0},{1}),".format(fileName, count)
        filesTrunc = filesString[0:len(filesString) - 1]
        filesFormed = "{0}".format(filesTrunc)
        filesFormedBracs = "{"+filesFormed+"}"
        print("{0} : {1} : {2}".format(word, numberOfAppearances, filesFormedBracs))
    except:
        a=1
