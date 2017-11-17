#!/usr/bin/env python

import sys

ownerRowIdDict = dict()
maxCount = 0
currentCount = 0

previousOwnerId = ''
currentOwenrId = ''

answerIds = ''

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/sortedinputforreducerc2', 'r')
# fileHandle = open('/home/raven/PycharmProjects/excassignment2/stacksorted.txt', 'r')

for line in sys.stdin:
    try:
        currentOwenrId, payload = line.strip('\n').split('\t')
        if currentOwenrId == previousOwnerId:
            answerIds += payload + ','
            currentCount += 1
        else:
            if previousOwnerId:
                if currentCount > maxCount:
                    ownerRowIdDict = {}  # blank out the dictionary
                    ownerRowIdDict[previousOwnerId] = answerIds[0:len(answerIds)-1]
                    maxCount = currentCount
                elif currentCount == maxCount:
                    ownerRowIdDict[previousOwnerId] = answerIds[0:len(answerIds)-1]
            previousOwnerId = currentOwenrId
            answerIds = ""
            answerIds += payload + ','
            currentCount = 1
    except:
        print('exception happened', line)

for key in ownerRowIdDict.keys():
    print("{0}\t{1}\t{2}".format(key, maxCount, ownerRowIdDict[key]))
