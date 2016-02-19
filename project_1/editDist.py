import sys
import numpy as np

file_1 = open(sys.argv[1], 'r').read()
file_2 = open(sys.argv[2], 'r').read()


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
			# If the characters are the same,
			# Set the value to diagonal neighbor.
			# Otherwise, set val to min of neighbors
			if file_1[x-1] == file_2[y-1]:
				DP[y, x] = DP[y-1, x-1]
			else:
				above = DP[y-1, x]
				left = DP[y, x-1]
				diag = DP[y-1, x-1]
				DP[y, x] = get_min(above, left, diag) + 1

	backtrack(DP, m-1, n-1)
	return DP[n-1, m-1]

def get_min(a, b, c):
	return min([a, b, c])



str_a = ''
str_b = ''
str_c = ''

# given a digit, check to see where it came from
def backtrack(DP, x, y):
	'''
	'''
	
	# Ensure strings are defined as global, not local
	global str_a, str_b, str_c
	
	# Break out of recursion once reach 0,0
	if x < 1 or y < 1:
		pretty_print(str_a[::-1], str_c[::-1], str_b[::-1])
		return
	current = DP[y, x]

	# Look at its neighbors
	above = DP[y-1, x]
	left = DP[y, x-1]
	diag = DP[y-1, x-1]
	
	# check for a minimum val
	min = get_min(above, left, diag)
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
	# if the val comes from the left, there is a gap
	elif left == min:
		str_a += file_1[x-1]
		str_b += '-'
		str_c += ' '
		next_x = x-1
		next_y = y
	# otherwise, if val comes from above, there is a gap
	else:
		str_a += '-'
		str_b += file_2[y-1]
		str_c += ' '
		next_x = x
		next_y = y-1

	# The function calls itself to proceed
	backtrack(DP, next_x, next_y)


def pretty_print(seq_one, seq_two, alignment, edit_distance):
	'''
	Prints the edit distance, and alignment sequence
	according to the project guidelines (60 chars)

	:seq_one: string containing an aligned string of `file_1`
	:seq_two: string containing an aligned string of `file_2`
	:alignment: string showing matches for `seq_one` + `seq_two`
	:edit_distance: integer of the edit distance of the pair
	'''
	import math
	# Get the alignment length
	align_len = len(alignment)
	print '\nEdit Distance = {}'.format(edit_distance)
	print 'Optimal Alignment: \n'
	# If the alignment is greater than 60 chars
	# we have to print it in chunks	
	if (align_len > 60):
		# Figure out how many chunks to print
		chunks = int(math.ceil(float(align_len) / 60))
		for i in range(0, chunks):
			start = i * 60
			end = (i + 1) * 60
			print seq_one[start:end]
			print alignment[start:end]
			print seq_two[start:end]
			print
	else:
		print seq_one
		print alignment
		print seq_two
		print


edit_distance(file_1, file_2)