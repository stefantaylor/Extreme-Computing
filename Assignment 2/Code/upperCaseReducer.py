#! /usr/bin/python
from operator import itemgetter
import sys

pairs = []
for line in sys.stdin:
	pairs.append(line)
pairs.sort(key=lambda pair: int(pair[pair.index("\t")+1:]))
for pair in pairs:
	print pair[:pair.index("\t")]
	
