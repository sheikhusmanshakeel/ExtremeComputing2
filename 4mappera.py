#!/usr/bin/env python

import sys
import operator

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/stackSmall.txt','r')
# fileHandle = open('/home/raven/PycharmProjects/excassignment2/stackSmall.txt', 'r')

rowViewCountDict = dict()


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
        viewCount = ReturnParsedValue(line, "viewcount=")
        rowId = ReturnParsedValue(line, "Id=")
        if viewCount != -1 and rowId != -1:
            if len(rowViewCountDict) < 10:
                rowViewCountDict[rowId] = viewCount
            else:
                minDictEntry = min(rowViewCountDict.items(), key=lambda x: x[1])
                if minDictEntry[1] < viewCount:
                    rowViewCountDict.__delitem__(minDictEntry[0])
                    rowViewCountDict[rowId] = viewCount
                elif minDictEntry[1] == viewCount:
                    rowViewCountDict[rowId] = viewCount
    except:
        a = 1
        # print("WARNING WARNING WARNING. EXCEPTION OCCURRED")

sortedList = sorted(rowViewCountDict.items(), key=operator.itemgetter(1))

for i in range(0, len(sortedList)):
    print("{0}\t{1}".format(sortedList[i][0],sortedList[i][1]))
