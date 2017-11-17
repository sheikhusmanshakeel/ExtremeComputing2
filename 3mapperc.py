#!/usr/bin/env python

import sys
import datetime

for line in sys.stdin:
    try:
        host, restOfRequest = line.strip('\n').split('- -');
        time = restOfRequest.split(']')[0]
        time = time.replace('[', '').strip()
        dtime = datetime.datetime.strptime(time.split()[0], "%d/%b/%Y:%H:%M:%S")
        dtimeString = dtime.strftime("%Y%m%d%H%M%S")
        print("{0}\t{1}".format(host, dtimeString))
    except:
        a=1
        # print("EXCEPTION OCCURRED", line)
