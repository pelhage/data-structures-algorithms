import sys
import numpy as np
file_1 = open(sys.argv[1], 'r').read()
file_2 = open(sys.argv[2], 'r').read()

print file_1
print file_2

def edit_distance(file_1, file_2):
	'''
	This function calculates the edit Distance
	of two passed in strings `file_1` and `file_2`

	:file_1: First string of text to be compared
	:file_2: Second string of text to be compared

	:returns: integer of the edit distance
	'''
	# Lengths of each file
	m = len(file_1) + 1
	n = len(file_2) + 1
	# Initializes 2D array
	DP = np.zeros(shape=(m,n), dtype=np.int)
	DP[0, 0] = 0
	# Initialize first col of array's values
	for i in range(1, m):
		DP[i, 0] = i * 2
	# Initialize first row of array's values
	for j in range(1, n):
		DP[0, j] = j * 1
	
	for i in range(1, m):
		for j in range(1, n):

			# Go back 2 indexes due to `len` and 
			if file_1[i-1] == file_2[j-1]:
				DP[i, j] = DP[i-1, j-1]
			else:
				above = DP[i, j-1]
				left = DP[i-1, j]
				diag = DP[i-1, j-1]
				DP[i, j] = get_min(above, left, diag) + 1
			
	print DP
	backtrack(DP)
	return DP[m-1, n-1]

def backtrack(data):
	m, n = data.shape
	data[m,n]



'''
  i   i   i   i   i   i
	  C   A   T   T   G
  0, -1, -2, -3, -4, -5
A -1, -1, 0, -1, -2, -3
T -2, -2, -1
T -3
G -4
A -5
'''
def is_match(a, b):
	if a == b:
		return 0
	else:
		return 1

def get_min(a, b, c):
	return min([a, b, c])

print edit_distance(file_2, file_1)

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