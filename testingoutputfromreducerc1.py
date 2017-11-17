#!/usr/bin/env python

import sys

ownerRowIdDict = dict()
maxCount = 0
currentCount = 0

previousOwnerId = ''
currentOwenrId = ''

answerIds = ''

fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/outputfromreducerc1', 'r')
# fileHandle = open('/home/raven/PycharmProjects/excassignment2/stacksorted.txt', 'r')

for line in fileHandle.readlines():
    currentOwenrId, payload = line.strip('\n').split('\t')
    if currentOwenrId not in ownerRowIdDict:
        ownerRowIdDict[currentOwenrId] = payload + ' , '
    else:
        answers = ownerRowIdDict[currentOwenrId]
        ownerRowIdDict[currentOwenrId] = answers + ' , ' + payload

for key in ownerRowIdDict.keys():
    count = len(ownerRowIdDict[key].split(',')) -1
    print("{0}\t{1}".format(key,count))