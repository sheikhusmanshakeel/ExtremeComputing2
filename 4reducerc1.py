#!/usr/bin/env python

import sys


# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/task4mapperoutputforreducer','r')
acceptedAnswerId = ""
ownerUserId = ""

for line in sys.stdin:
    token1, token2 = line.strip().split('\t')
    if token2 == "-1":  # This means that we have an accepted answer id coming in
        acceptedAnswerId = token1
    else:
        if acceptedAnswerId == token1:
            ownerUserId = token2
            print("{0}\t{1}".format(ownerUserId, acceptedAnswerId))
            ownerUserId = ""
            acceptedAnswerId = ""
        else:
            acceptedAnswerId = ""
