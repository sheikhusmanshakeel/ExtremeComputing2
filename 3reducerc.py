#!/usr/bin/env python

import sys
import datetime

host = ""
previousHost = ""
maxTime = ""
minTime = ""
# fileHandle = open('/afs/inf.ed.ac.uk/user/s15/s1579769/excassignment2/log1', 'r')
for line in sys.stdin:
    try:
        host, time = line.strip().split('\t')
        if host == previousHost:
            maxTime = time
        else:
            if previousHost:
                if maxTime != "" and minTime != "":
                    maxDateTime = datetime.datetime.strptime(maxTime, "%Y%m%d%H%M%S")
                    minDateTime = datetime.datetime.strptime(minTime, "%Y%m%d%H%M%S")
                    differenceDateTime = maxDateTime - minDateTime
                    dif = datetime.timedelta(seconds=differenceDateTime.total_seconds())
                    print("{0}\t {1}".format(previousHost, dif))
                    maxTime = ""
                    minTime = ""
                    # print("{0}\t{1}".format(previousHost,differenceDateTime.total_seconds()))
                    # differenceInMinutesAndSeconds = divmod(differenceDateTime.total_seconds(), 60)
                    # minutes = differenceInMinutesAndSeconds[1]
                    # seconds = differenceInMinutesAndSeconds[0]
                    # print("{0} \t minutes: {1} \t seconds: {2}".format(previousHost, minutes, seconds))

                else:
                    minDateTime = datetime.datetime.strptime(minTime, "%Y%m%d%H%M%S")
                    minDateToPrint = minDateTime.strftime("%d/%b/%Y:%H:%M:%S")
                    print("{0}\t{1}".format(previousHost, minDateToPrint))
                    maxTime = ""
                    minTime = ""
            previousHost = host
            minTime = time
    except:
        a = 1
        # print("Exception occurred", line)
