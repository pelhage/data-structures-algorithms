f# def answer_one():
	# 2^10
	# 2^log n
	# 4*n
	# n^2 + 10*n
	# 4*n * log n + 2*n
	# n^3	
	# 2^n
	# n*log n
	

def answer_two(n):
	print "Logarithmic - log(n)"



def answer_three(filename, n_largest):
	'''
	filename: 
	'''
	import numpy as np
	import string as String
	
	opened_file = open(filename, 'r')
	text = opened_file.read().lower()
	
	
	# Initialize data structures to count letters and digrams. 
	# Individual letters are represented via indexes of the alphabet
	letters = np.zeros(shape=(26,), dtype=np.int)
	letters_count = 0
	digrams = np.zeros(shape=(26,26), dtype=np.int) # 2d array
	
	digrams_count = 0
	# Alphabet string for reference within data structures
	abc = String.ascii_lowercase

	# Ensure each character in `text`, is a word character.
	# Count it in `letters`. Then, check for a digram and count it in `digrams`.
	# `last_char_ndx`, is declared to ensure we check within `text`'s bounds
	last_char_ndx = len(text) - 1
	for char_ndx, char in enumerate(text):
		if char.isalpha():
			# Tally the single letter occurence
			letters[abc.index(char)] += 1
			letters_count += 1	
			# Get digram pair and tally it
			if (char_ndx < last_char_ndx):
				next_letter = text[char_ndx + 1]
				if next_letter.isalpha():
					row = abc.index(char)
					col = abc.index(next_letter)
					digrams[row, col] += 1
					digrams_count += 1


	num_largest = n_largest
	

	# Create a sorted List of letters from the dictionary's key/value pairs
	# We do this by getting 
	top_letters_indices = (-letters).argsort()[:num_largest]
	top_letters_sorted = []
	
	for index in top_letters_indices:
		top_letters_sorted.append([abc[index], letters[index]])
	print top_letters_sorted



	# Search through the digram and find the `num_largest` largest values.
	# Get the indices for these values.
	# `x` and `y` contain the coordinates of the most frequent digrams
	indices = (-digrams).argpartition(num_largest, axis=None)[:num_largest]
	x, y = np.unravel_index(indices, digrams.shape)

	# Sort the `num_largest` digrams 
	sorted_digrams = []
	for coords in range(0, num_largest):
		# sorted_letter_list.append(abc[]) #####
		sorted_digrams.append([ abc[x[coords]] + abc[y[coords]],
			digrams[x[coords], y[coords]] ])
	
	print sorted(sorted_digrams, key=lambda x:x[1], reverse=True)






def compare(num_list):
	'''

	'''
	num_len = len(num_list)
	mid_point = num_len // 2
	# Initialize arbitrary min/max values for comparison
	min_num = num_list[0]
	max_num = num_list[1]

	# Search and compare the list starting from both sides
	# working towards the middle of the list
	# In the top level comparison, the smaller number will
	# be compared to the `min_num` variable and the larger
	# number will be compared to the `max_num` variable
	for index, num in enumerate(range(0, mid_point)):
		a = num_list[index]
		b = num_list[num_len - 1 - index]
		if a > b:
			if a > max_num:
				max_num = a
			if b < min_num:
				min_num = b
		else:
			if a < min_num:
				min_num = a
			if b > max_num:
				max_num = b

	# If the number list is odd, then there's one
	# element that hasn't been compared. Compare it to
	# the current min/max values
	if num_len % 2 != 0:
		mid_num = num_list[mid_point]
		if mid_num < min_num:
			min_num = mid_num
		elif mid_num > max_num:
			max_num = mid_num

	# Print results!
	print 'Minimum value: {}'.format(min_num)
	print 'Maximum value: {}'.format(max_num)


compare([0, 2, -5, -15, 55, 91, 101])
answer_three('world95.txt', 26)