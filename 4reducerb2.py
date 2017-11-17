#!/usr/bin/env python

import sys
import operator

ownerRowDict = dict()
maxCount = 0
currentCount = 0


previousOwnerId = ''
currentOwenrId = ''

rowIdStringList = ''

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/logsSmall.txt','r')
# fileHandle = open('/home/raven/PycharmProjects/excassignment2/stacksorted.txt', 'r')

for line in sys.stdin:
    ownerId, count, payload = line.strip('\n').split('\t')
    # we know at this point that none of the owner ids will be repeated.
    # so this becomes a simple task of just sorting
    ownerId = int(ownerId)
    count = int(count)
    if count > maxCount:
        maxCount = count
        ownerRowDict = {}
        ownerRowDict[ownerId] = payload
    elif count == maxCount:
        ownerRowDict[ownerId] = payload


sortedList = sorted(ownerRowDict.items(), key=operator.itemgetter(1))
for i in range(0,len(sortedList)):
    print("{0} --> \t{1}".format(sortedList[i][0],sortedList[i][1]))