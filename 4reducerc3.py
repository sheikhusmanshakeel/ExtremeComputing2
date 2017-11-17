#!/usr/bin/env python

import sys
previousOwnerId = ""
maxCount = 0

ownerDict = dict()

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/inputforreducerc3', 'r')

for line in sys.stdin:
    ownerId, count, payload = line.strip('\n').split('\t')
    count = int(count)
    if count > maxCount:
        ownerDict = {}
        ownerDict[ownerId] = payload
        maxCount = count
    elif count == maxCount:
        ownerDict[ownerId] = payload

for key in ownerDict.keys():
    print("{0} --> {1}, {2}".format(key, maxCount, ownerDict[key]))

