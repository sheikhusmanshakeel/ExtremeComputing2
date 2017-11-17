#!/usr/bin/env python

import sys

for line in sys.stdin:
    try:
        host, restOfRequest = line.strip().split('- -')
        httpResponsesAndBytes = restOfRequest.split('" ')
        httpResponse = httpResponsesAndBytes[len(httpResponsesAndBytes) - 1]
        http, requestBytes = httpResponse.split()
        if int(http) == 404:
            print("{0}\t{1}".format(host, 1))
    except:
        a=1
