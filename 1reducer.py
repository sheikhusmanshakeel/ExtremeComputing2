#!/usr/bin/env python

import sys

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/1reducertest','r')

currentWord = ""
previousWord = ""

previousFileName = ""
numberInDocument = 0

filenFreqString = ""
wordInCorpus = 0

for line in sys.stdin:
    tokens = line.strip().strip('\n').split('\t')
    currentWord = tokens[0]
    if currentWord != previousWord:
        if previousWord: #if previous word is not blank then print. this will handle the first case.
            filenFreqString += "{0}|{1};".format(previousFileName,numberInDocument)
            filenFreqString = filenFreqString[0:len(filenFreqString)-1];
            print("{0}\t{1}\t{2}".format(previousWord,wordInCorpus,filenFreqString))
        previousWord = currentWord
        previousFileName = tokens[1]
        numberInDocument = int(tokens[2])
        wordInCorpus = 1 # It is seen this word at least once in the corpus
        filenFreqString = ''
    else:
        currentFileName = tokens[1]
        frequency = int(tokens[2])
        if currentFileName == previousFileName:
            numberInDocument += frequency
        else:
            wordInCorpus += 1 # It has seen this word in another document in the corpus
            filenFreqString += "{0}|{1};".format(previousFileName,numberInDocument)
            numberInDocument = frequency # clear the frequence
            previousFileName = currentFileName # set the previous filename as current filename

# now do it for the last word which will be the same as previous word

filenFreqString += "{0}|{1};".format(previousFileName,numberInDocument)
print("{0}\t{1}\t{2}".format(previousWord,wordInCorpus,filenFreqString))