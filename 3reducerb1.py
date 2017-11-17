#!/usr/bin/python

import sys
import operator
prev_host = ''
totalcount = 0
maxsofar = 0
top10 = {}
for line in sys.stdin:
    line = line.strip('\n')
    host, count = line.split('\t')
    count = int(count)
    if prev_host == host:
        totalcount += count
    else:
        if prev_host:
            if len(top10) < 10:
                top10[host] = totalcount
            else:
                key_min_top10 = min(top10, key = top10.get)
                min_top10 = top10[key_min_top10]
                if totalcount > min_top10:
                    for key, value in top10.items():
                        if value == min_top10:
                            top10.pop(key)
                    top10[host] = totalcount
                else:
                    if totalcount == min_top10:
                        top10[host] = totalcount
        totalcount = int(count)
        prev_host = host
sorted_top10 = sorted(top10.items(), key=operator.itemgetter(1), reverse=True)

for i in range(0, len(sorted_top10)):
    print('{0}\t{1}'.format(sorted_top10[i][0], sorted_top10[i][1]))







#!/usr/bin/env python
import sys
import operator

previousHost = ""
totalCount = 0
hostsWithBadRequests = {}

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
                hostsWithBadRequests[currentHost] = totalCount
            else:
                minDictEntryKey = min(hostsWithBadRequests, key = hostsWithBadRequests.get)
                minValue = hostsWithBadRequests[minDictEntryKey]
                if minValue < totalCount:
                    for key, value in hostsWithBadRequests.items():
                        if value == minValue:
                            hostsWithBadRequests.pop(key)
                    hostsWithBadRequests[currentHost] = totalCount
                elif minValue == totalCount:
                    hostsWithBadRequests[currentHost] = totalCount
        previousHost = currentHost
        totalCount = count


sortedList = sorted(hostsWithBadRequests.items(), key=operator.itemgetter(1), reverse=True)

for i in range(0,len(sortedList)):
    print("{0}\t{1}".format(sortedList[i][0],sortedList[i][1]))