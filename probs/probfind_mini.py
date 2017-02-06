#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('UTF8')

emojis = [('😄').decode('utf-8'), ('😃').decode('utf-8'), ('😀').decode('utf-8'), ('😊').decode('utf-8'), ('☺').decode('utf-8'), ('😉').decode('utf-8'), ('😍').decode('utf-8'), ('😘').decode('utf-8'), ('😚').decode('utf-8'), ('😗').decode('utf-8'), ('😙').decode('utf-8'), ('😜').decode('utf-8'), ('😝').decode('utf-8'), ('😛').decode('utf-8'), ('😳').decode('utf-8'), ('😁').decode('utf-8'), ('😔').decode('utf-8'), ('😌').decode('utf-8'), ('😒').decode('utf-8'), ('😞').decode('utf-8'), ('😣').decode('utf-8'), ('😢').decode('utf-8'), ('😂').decode('utf-8'), ('😭').decode('utf-8'), ('😪').decode('utf-8'), ('😥').decode('utf-8'), ('😰').decode('utf-8'), ('😅').decode('utf-8'), ('😓').decode('utf-8'), ('😩').decode('utf-8'), ('😫').decode('utf-8'), ('😨').decode('utf-8'), ('😱').decode('utf-8'), ('😠').decode('utf-8'), ('😡').decode('utf-8'), ('😤').decode('utf-8'), ('😖').decode('utf-8'), ('😆').decode('utf-8'), ('😋').decode('utf-8'), ('😷').decode('utf-8'), ('😎').decode('utf-8'), ('😴').decode('utf-8'), ('😵').decode('utf-8'), ('😲').decode('utf-8'), ('😟').decode('utf-8'), ('😦').decode('utf-8'), ('😧').decode('utf-8'), ('😈').decode('utf-8'), ('👿').decode('utf-8'), ('😮').decode('utf-8'), ('😬').decode('utf-8'), ('😐').decode('utf-8'), ('😕').decode('utf-8'), ('😯').decode('utf-8'), ('😶').decode('utf-8'), ('😇').decode('utf-8'), ('😏').decode('utf-8'), ('😑').decode('utf-8')]

counts = []
total_count = 0

num_emojis = len(emojis)
num_processed = 0

with open('input.txt') as t:
    lines = t.readlines()    

    for e in emojis:
        count = 0
        for l in lines:
            this_count = l.count(e)
            count += this_count
            total_count += this_count
        counts.append(count)
        num_processed += 1
        print ("Completed " + str(num_processed) + " of " + str(num_emojis) + " (" + str(num_processed * 100 / num_emojis) + "%)")

probabilities = []
total_count_with_non_zeros = total_count + len(emojis)

for c in counts:
    probabilities.append(float(c + 1) / float(total_count_with_non_zeros))

with open("output_mini.txt", "w") as t:
    for p in probabilities:
        t.write(repr(p))
        t.write(",")

