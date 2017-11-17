#!/usr/bin/env python
import os
import sys

currentPosition = 0
maxBuffer = 100000
textArray = dict()
#fileHandle = open('/home/raven/PycharmProjects/excassignment2/d1.txt', 'r');


def Flush():
    for pairKey in textArray.keys():
        word = pairKey[0]
        fileName = pairKey[1]
        print("{0}\t{1}\t{2}".format(word, fileName, textArray[pairKey]))


# def GetFileName(filePath):
#     components = filePath.split('/')
#     return components[len(components)]

# hdfs://macallan.inf.ed.ac.uk:8020/data/incredibly/long/path/d1.txt

for line in sys.stdin:
    tokens = line.strip('\n').split()
    fileName = os.path.basename(os.environ["mapreduce_map_input_file"])
    currentPosition += 1
    if currentPosition >= maxBuffer:
        Flush()
        textArray = dict()
        currentPosition = 0
    # print(tokens)
    for token in tokens:
        pair = (token, fileName)
        if pair in textArray:
            newWordCount = int(textArray[pair]) + 1
            textArray[pair] = newWordCount
        else:
            textArray[pair] = 1

Flush()
