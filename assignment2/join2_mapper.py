#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key_value = line.split(",")
    key_in = key_value[0]
    value_in = key_value[1]

    try:
        viewers = int(value_in)
        print('%s\t%s' % (key_in, value_in))
    except:
        # Value is not a number. Must be a station
        if value_in == 'ABC':
            print('%s\t%s' % (key_in, value_in))

