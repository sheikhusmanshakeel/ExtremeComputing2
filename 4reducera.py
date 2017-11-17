#!/usr/bin/env python

import sys
import operator

rowViewCountDict = dict()

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/logsSmall.txt','r')
# fileHandle = open('/home/raven/PycharmProjects/excassignment2/stacksorted.txt', 'r')

for line in sys.stdin:
    rowId, viewCount = line.strip('\n').split('\t')
    viewCount = int(viewCount)
    rowId = int(rowId)
    if len(rowViewCountDict) < 10:
        rowViewCountDict[rowId] = viewCount
    else:
        minDictEntry = min(rowViewCountDict.items(), key=lambda x: x[1])
        if minDictEntry[1] < viewCount:
            rowViewCountDict.__delitem__(minDictEntry[0])
            rowViewCountDict[rowId] = viewCount
        elif minDictEntry[1] == viewCount:
            rowViewCountDict[rowId] = viewCount




sortedList = sorted(rowViewCountDict.items(), key=operator.itemgetter(0))

for i in range(0,len(sortedList)):
    print("{0}\t{1}".format(sortedList[i][0],sortedList[i][1]))

