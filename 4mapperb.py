#!/usr/bin/env python

import sys

# Why did i not use a combiner here?

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/stackSmall.txt','r')
# fileHandle = open('/home/raven/PycharmProjects/excassignment2/stackSmall.txt', 'r')

def ReturnParsedValue(line, wordToFind):
    parsedValue = -1
    line = line.lower()
    wordToFind = wordToFind.lower()
    indexOfWordToFind = line.find(wordToFind, 0, len(line))
    if indexOfWordToFind != -1:
        # find the first space.
        indexOfFirstSpace = line.find(' ', indexOfWordToFind, len(line))
        if indexOfFirstSpace != -1:
            parsedValue = int(line[indexOfWordToFind + len(wordToFind):indexOfFirstSpace].replace('\"','').strip())
    return parsedValue



for line in sys.stdin:
    line = line.strip();
    try:
        ownerUserId = ReturnParsedValue(line, "OwnerUserId=")
        questionId = ReturnParsedValue(line, "ParentId=")
        postTypeId = ReturnParsedValue(line,"PostTypeId=")
        if ownerUserId != -1 and questionId != -1 and postTypeId == 2:
            print("{0}\t{1}".format(ownerUserId, questionId))
    except ValueError:
        a = 1
        # print('SOMETHING WENT HORRIBLY WRONG.')