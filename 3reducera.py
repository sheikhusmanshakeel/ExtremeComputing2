#!/usr/bin/env python
import sys
previousWebPage = ""
totalCount = 0
webPage = ""
maxCount = 0;
highestPages = []


for line in sys.stdin:
    webPage, value = line.strip().split('\t')
    value = int(value)
    if previousWebPage == webPage:
        totalCount += value
    else:
        if previousWebPage:
            if totalCount == maxCount:
                highestPages.append(previousWebPage)
            elif totalCount > maxCount:
                highestPages = [];
                highestPages.append(previousWebPage)
                maxCount = totalCount
        totalCount = value
        previousWebPage = webPage

for i in range(0,len(highestPages)):
    print("{0}\t{1}".format(highestPages[i],maxCount))
