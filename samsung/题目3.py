import sys
import os
import operator
from sys import argv

def main():
	args = argv
	fname = args[1]
	wordNum = args[2]

	try:
		if os.path.exists(fname):
			wordList = open(fname).readlines()
			freq = {}
			for line in wordList:
				line = line.split()
				for word in line:
					if word not in freq:
					 	freq[word] = 1 
					else:
					 	freq[word] += 1

			freq = sorted(freq.iteritems(), key=operator.itemgetter(1), reverse=True) 
			
			for i in range(0, int(wordNum)):
				print freq[i][0] + ' ' + str(freq[i][1])
		else:
			print 'Does not exist this file!'

	except Exception as e:
		print 'Does exist'
		raise e

if __name__ == '__main__':
	main()


