#!/usr/bin/env python

import sys

# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/stackSmall.txt','r')
# fileHandle = open('/home/raven/PycharmProjects/excassignment2/stackSmall.txt', 'r')
counter = 0


def ReturnParsedValue(line, wordToFind):
    parsedValue = -1
    line = line.lower()
    wordToFind = wordToFind.lower()
    indexOfWordToFind = line.find(wordToFind, 0, len(line))
    if indexOfWordToFind != -1:
        # find the first space.
        indexOfFirstSpace = line.find(' ', indexOfWordToFind, len(line))
        if indexOfFirstSpace != -1:
            parsedValue = int(line[indexOfWordToFind + len(wordToFind):indexOfFirstSpace].replace('\"', '').strip())
    return parsedValue


for line in sys.stdin:
    try:
        postTypeId = ReturnParsedValue(line, "PostTypeId=")
        if postTypeId == 1:
            acceptedAnswerId = ReturnParsedValue(line, "AcceptedAnswerId=")
            if acceptedAnswerId != -1:
                print("{0}\t{1}".format(acceptedAnswerId,"-1"))
        elif postTypeId == 2 :
            postId = ReturnParsedValue(line,"Id=")
            ownerUserId = ReturnParsedValue(line,"owneruserid=")
            if postId != -1 and ownerUserId != -1:
                print("{0}\t{1}".format(postId,ownerUserId))
    except:
        a = 1
        # print("COUNTER IS", counter)
        # print(line)
