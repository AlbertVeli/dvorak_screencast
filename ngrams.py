#!/usr/bin/env python

# Count bi-grams and tri-grams in text

import sys
import re
from collections import Counter

if len(sys.argv) < 2:
    print('Usage: %s <corpus textfile>' % (sys.argv[0]))
    sys.exit(1)

txt = open(sys.argv[1]).read()
words = re.findall("\w+", txt)

bigrams = []
trigrams = []
for w in words:
    w = w.lower()
    for i in range(len(w) - 1):
        bigrams.append(w[i : i + 2])
    for i in range(len(w) - 2):
        trigrams.append(w[i : i + 3])

print('Bigrams:')
print(Counter(bigrams))

print('Trirams:')
print(Counter(trigrams))

#print(Counter(words))
