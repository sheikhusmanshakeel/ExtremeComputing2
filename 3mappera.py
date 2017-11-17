#!/usr/bin/env python

import sys

webpageDict = dict()
maxBuffer = 100000
currentBuffer = 0
#fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/logsSmall.txt','r')

def Flush():
    for page in webpageDict.keys():
        print("{0}\t{1}".format(page,webpageDict[page]))

for line in sys.stdin:
    try:
        currentBuffer += 1
        if currentBuffer > maxBuffer:
            Flush()
            webpageDict = {}
            currentBuffer = 0
        parsedLine = line.strip().split('\"');
        webRequest = parsedLine[1]
        webPage = webRequest.split()[1]
        if webPage in webpageDict:
            #update the number of times page has been called
            newWebPageCount = int(webpageDict[webPage]) +1;
            webpageDict[webPage] = newWebPageCount
        else:
            webpageDict[webPage] = 1
    except:
        a=2;
        # Don't let the program break, data is messy innit!
Flush()
