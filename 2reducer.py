#!/usr/bin/env python
import sys
import math

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/inputForReducer1a.txt', 'r')
numberOfDocumentsInCorpus = 17.0
terms = []
termsAlreadyUsed = []

# The only reason i am reading the fine again is coz i wanna keep track of which terms have been used
# coz i need to output terms not used as well...
for term in file('terms.txt'):
    terms.append(term.strip('\n'))

for line in sys.stdin:
    tokens = line.strip('\n').split('\t')
    word = tokens[0]
    if word in terms:
        numberOfAppearancesInCorpus = tokens[1]
        documents = tokens[2].split(';')
        for document in documents:
            fileName, frequencyOfWordInFile = document.split('|')
            if fileName == 'd1.txt':
                logValue = float(numberOfDocumentsInCorpus) / (1 + int(numberOfAppearancesInCorpus))
                try:
                    idf = math.log10(logValue)
                    tf_idf = idf * float(frequencyOfWordInFile)
                    print("{0}, {1} = {2}".format(word, fileName, tf_idf))
                    termsAlreadyUsed.append(word)
                except:
                    a = 1

for i in range(0, len(terms)):
    if terms[i] not in termsAlreadyUsed:
        print("{0}, {1} = {2}".format(terms[i], "d1.txt", 0))
