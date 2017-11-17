#!/usr/bin/env python

import sys
import operator

ownerRowDict = dict()
maxCount = 0
currentCount = 0

previousOwnerId = ''
currentOwenrId = ''

questionIdList = []

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/stacksorted.txt', 'r')
# fileHandle = open('/home/raven/PycharmProjects/excassignment2/stacksorted.txt', 'r')

for line in sys.stdin:
    ownerId, questionId = line.strip('\n').split('\t')
    currentOwenrId = int(ownerId)
    if previousOwnerId == currentOwenrId:
        questionIdList.append(questionId)
        currentCount += 1
    else:
        if previousOwnerId:
            # because some questions are being repeated
            # questions = list(set(questionIdList))
            if len(questionIdList) > maxCount:
                maxCount = len(questionIdList)
                ownerRowDict = {}  # empty whatever was in the dict, since we found something longer
                ownerRowDict[previousOwnerId] = questionIdList
                # currentCount = 0;  # this current count will be updated to 1 in the main else block
            elif len(questionIdList) == maxCount:
                ownerRowDict[previousOwnerId] = questionIdList
        previousOwnerId = currentOwenrId
        questionIdList = []
        questionIdList.append(questionId)
        # currentCount = 1

# check if the last one was as big as any other in the list
questions = list(set(questionIdList))
if len(questions) > maxCount:
    ownerRowDict = {}  # empty whatever was in the dict, since we found something longer
    ownerRowDict[previousOwnerId] = questions
    currentCount = 0;  # this current count will be updated to 1 in the main else block
elif len(questions) == maxCount:
    ownerRowDict[previousOwnerId] = questions

sortedList = sorted(ownerRowDict.items(), key=operator.itemgetter(0))
for i in range(0, len(sortedList)):
    value = sortedList[i][1]
    str = ''
    for j in range(0, len(value)):
        str += value[j] + ' ,'
    str = str[0:len(str) - 1]
    print("{0}\t{1}\t{2}".format(sortedList[i][0], maxCount, str))
