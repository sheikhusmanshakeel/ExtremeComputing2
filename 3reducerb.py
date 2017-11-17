#!/usr/bin/env python
import sys
import operator

previousHost = ""
totalCount = 0
hostsWithBadRequests = dict()

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/badrequests','r')
maxValue = 10

for line in sys.stdin:
    currentHost, count = line.strip().split('\t')
    count = int(count)
    if previousHost == currentHost:
        totalCount += count
    else:
        if previousHost:
            if len(hostsWithBadRequests) < maxValue:
                hostsWithBadRequests[previousHost] = totalCount
            else:
                minDictEntry = min(hostsWithBadRequests.items(), key=lambda x: x[1])
                minValue = minDictEntry[1]
                if minValue < totalCount:
                    for key in hostsWithBadRequests.keys():
                        if hostsWithBadRequests[key] == minValue:
                            hostsWithBadRequests.__delitem__(key)
                    hostsWithBadRequests[previousHost] = totalCount
                elif minValue == totalCount:
                    hostsWithBadRequests[previousHost] = totalCount
        previousHost = currentHost
        totalCount = count


sortedList = sorted(hostsWithBadRequests.items(), key=operator.itemgetter(1), reverse=True)

for i in range(0,len(sortedList)):
    print("{0}\t{1}".format(sortedList[i][0],sortedList[i][1]))

