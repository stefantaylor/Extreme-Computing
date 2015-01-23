#!/usr/bin/python
import sys
# input from standard input
i = 0
for line in sys.stdin:
	line = line.upper()
	print line
#	# remove whitespaces
#	line = line.strip()
#	# split the line into tokens
#	tokens = line.split()
#	
#	for token in tokens :
#		i = i + 1
#		# write the results to standard output
#		print '%s\t%s' % (token.upper() , i)
