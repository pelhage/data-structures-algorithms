## Assignment 1

Check out the pdf file for the full assignment breakdown, but the assignment questions can be summarized as follows:

1. Order the following functions increasingly by their growth rate (functions with the same growth rate may be ordered arbitrarily):
  * 4*n*log*n* + 2*n*
  * 2<sup>10</sup>
  * 2<sup>log*n*</sup>
  * 3*n* + 100log*n*
  * 4*n*
  * 2<sup>*n*</sup>
  * *n*<sup>2</sup> + 10*n*
  * *n*<sup>3</sup>
  * *n*log*n*
2. Determine the Big O complexity of a given code segment:
  
  ```python
  sum = 0
  i = n
  while (i >= 1):
  	sum += i
	i /= 2
  i = n
  j = 2
  while (i >= 1):
	sum += i
	i /= j
	j *= 2
  # Hint: you do not need to find the precise complexity for all parts of the code, only for the dominant ones
  ```
3. Write an algorithm that parses an input file of English text and finds the top 10 most frequent letters (i.e. 'a', 'o') and top 10 most frequent digrams (i.e. 'an', 'th', 'om', etc)
4. Give an algorithm for finding both the minimum and maximum of *n* numbers using at most 3*n*/2 comparisons.
