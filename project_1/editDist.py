import sys
import numpy as np
file_1 = open(sys.argv[1], 'r').read()
file_2 = open(sys.argv[2], 'r').read()

str_a = ''
str_b = ''
str_c = ''
def edit_distance(file_1, file_2):
	'''
	This function calculates the edit Distance
	of two passed in strings `file_1` and `file_2`

	:file_1: First string of text to be compared
	:file_2: Second string of text to be compared

	:returns: integer of the edit distance
	'''
	# Lengths of each file
	m = len(file_1) + 1 # FILE 1
	n = len(file_2) + 1

	# Initializes 2D array
	DP = np.zeros(shape=(n,m), dtype=np.int)
	DP[0, 0] = 0
	# Initialize first row of array's values
	# representing file 1
	for x in range(1, m):
		DP[0, x] = x
	# Initialize first col of array's values
	# representing file 2
	for y in range(1, n):
		DP[y, 0] = y

	# For each letter in file 1
	for x in range(1, m):
		# Go through the letters of file 2
		for y in range(1, n):

			# Go back 2 indexes due to `len` and 
			if file_1[x-1] == file_2[y-1]:
				DP[y, x] = DP[y-1, x-1]
			else:
				above = DP[y-1, x]
				left = DP[y, x-1]
				diag = DP[y-1, x-1]
				DP[y, x] = get_min(above, left, diag) + 1
			
	print DP
	backtrack(DP, m-1, n-1)
	return DP[n-1, m-1]

def get_min(a, b, c):
	return min([a, b, c])




# given a digit, check to see where it came from
def backtrack(DP, x, y):

	global str_a, str_b, str_c
	if x < 1 or y < 1:
		return False
	current = DP[y, x]

	
	# Look at its neighbors
	above = DP[y-1, x]
	left = DP[y, x-1]
	diag = DP[y-1, x-1]
	
	
	# check for a minimum val
	min = get_min(above, left, diag)
	print 'Above: {}, left: {}, diag: {}, MIN: {}'.format(above, left, diag, min)
	print 'Current: {} at {},{}'.format(current, x, y)
	# if the minimum val is from the diagonal
	if diag == min:
		str_a += file_1[x-1]
		str_b += file_2[y-1]
		if file_1[x-1] == file_2[y-1]:
			str_c += '|'
		else:
			str_c += ' '
		next_x = x-1
		next_y = y-1
		print 'Moving Diagonally to {} at {},{}'.format(diag, next_x, next_y)
	# if the minimum val is from the left, then you deleted
	# the column value
	elif left == min:
		str_a += file_1[x-1]
		str_b += '-'
		str_c += ' '
		next_x = x-1
		next_y = y
		print 'Moving Left to {} at {},{}'.format(left, next_x, next_y)
	# otherwise
	else:
		str_a += '-'
		str_b += file_2[y-1]
		str_c += ' '
		next_x = x
		next_y = y-1
		print 'Moving Up to {} at {},{}'.format(left, next_x, next_y)
	print str_a[::-1]
	print str_c[::-1]
	print str_b[::-1]
	

	print DP
	backtrack(DP, next_x, next_y)

edit_distance(file_1, file_2)
def is_match(a, b):
	if a == b:
		return 0
	else:
		return 1
















### NOTES TAKEN TO COMPLETE THE PROJECT ###
'''
Edit Distance: the minimum number of edit operations it takes
to convert one to another.
	- Substitutions
	- Indels

Alignment:
	Simplest Scoring Function:
		Match = +1
		Mismatch = -1
		indel = -1
		- This is called 'linear gap penalty'

Take the following set of strings and use our
'Simplest Scoring Function'. What would be the
score?

AATGCGA-TTTT
G-TG--ACTTTC

Matches: +6
Mismatch: -2
Indel: -4
----------
Score: 0


How can alignment be computed?
	- Dynamic Programming (Get this explained)
		- Requires the subsolution
		  of an optimal soultion to
		  also be optimal:

		  AATGCGA     Score: +4 - 3
		  A-TG--A

		  AATGCGA-TTT Score: +7 - 4
		  A-TG--ACTTT

Last Column of an Alignment:
Align two strings S[1...i] and T[1..j]

S[1... i - 1] S[i]      
T[1... j - 1] T[j]

Optimal Alignment Score = 
		Optimal Alignment Score[S[1...i-1],T[1..j-1] ]
				+ score between last two letters


'''