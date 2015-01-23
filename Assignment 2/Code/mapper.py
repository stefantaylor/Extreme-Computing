#!/usr/bin/python
import sys
# input from standard input
for line in sys.stdin:
	# remove whitespaces
	line = line.strip()
	# split the line into tokens
	tokens = line.split()

	for token in tokens :
		# write the results to standard output
		print '%s\t%s' % (token , 1)
