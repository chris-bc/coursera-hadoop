#!/usr/bin/env python

import sys

prev_show = " "
show_count = 0
is_abc = 0

for line in sys.stdin:
    line = line.strip()
    key_value = line.split('\t')

    curr_show = key_value[0]
    value_in = key_value[1]

    if prev_show != ' ' and curr_show != prev_show:
        if is_abc == 1:
            print('%s %d' % (curr_show, show_count))
        show_count = 0
        is_abc = 0
    prev_show = curr_show

    # either get station info or view count for this record
    try:
        curr_views = int(value_in)
        show_count += curr_views
    except:
        if value_in == 'ABC':
            is_abc = 1

# print final show
if is_abc == 1:
    print('%s %d' % (prev_show, show_count))

