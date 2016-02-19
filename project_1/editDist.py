import sys
import numpy as np

file_1 = open(sys.argv[1], 'r').read()
file_2 = open(sys.argv[2], 'r').read()

class SequenceAlignment:
    
    def __init__(self, file_1, file_2):
        self.file_1 = file_1
        self.file_2 = file_2
        # M and N indexes
        self.seq_one_len = len(self.file_1)
        self.seq_two_len = len(self.file_2)
        # Initialize Data structure
        self.__init_data()

    
    def __init_data(self):
        # Initialize Dynamic Programming matrix.
        # Seq one on x axis, seq two on y axis
        DP = np.zeros(
            shape=(self.seq_two_len + 1, self.seq_one_len + 1), 
            dtype=np.int)
        DP[0, 0] = 0
        for x in range(1, self.seq_one_len + 1):
            DP[0, x] = x
        for y in range(1, self.seq_two_len + 1):
            DP[y, 0] = y
        # For each letter in file 1
        for x in range(1, self.seq_one_len + 1):
            # Go through the letters of file 2
            for y in range(1, self.seq_two_len + 1):
                # If the chars are same, set val to 
                # diagonal neighbor, else set to min
                if self.file_1[x-1] == self.file_2[y-1]:
                    DP[y, x] = DP[y-1, x-1]
                else:
                    DP[y, x] = min(
                        DP[y-1, x], # above
                        DP[y, x-1], # left
                        DP[y-1, x-1] # diagonal
                    ) + 1
        self.DP = DP
        self.edit_distance = DP[self.seq_two_len-1, 
                                self.seq_one_len-1]
        return

    
    def print_data(self):
        print self.DP


    def backtrace(self, x=None, y=None):
        """
        Recursive function that Backtraces a sequence 
        from given x,y coords. If no coords provided, 
        backtrace assumes user is tracing entire matrix
        """
        if x == None or y == None:
            x = len(self.file_1)
            y = len(self.file_2)
            self.seq_one = ''
            self.seq_two = ''
            self.seq_match = ''
        # Break out of recursion once reach 0,0
        if x < 1 or y < 1:
            self.alignment()
            return
        # Look at neighbors and find min val
        above = self.DP[y-1, x]
        left = self.DP[y, x-1]
        diag = self.DP[y-1, x-1]
        min_val = min(above, left, diag)

        if diag == min_val:
            self.seq_one += self.file_1[x-1]
            self.seq_two += self.file_2[y-1]
            if file_1[x-1] == self.file_2[y-1]:
                self.seq_match += '|'
            else:
                self.seq_match += ' '
            next_x = x-1
            next_y = y-1
        # if the val comes from left or above, there is a gap
        elif left == min_val:
            self.seq_one += file_1[x-1]
            self.seq_two += '-'
            self.seq_match += ' '
            next_x = x-1
            next_y = y
        else:
            self.seq_one += '-'
            self.seq_two += self.file_2[y-1]
            self.seq_match += ' '
            next_x = x
            next_y = y-1

        # The function calls itself to proceed
        self.backtrace(next_x, next_y)


    def alignment(self):
        """
        Prints the edit distance, and alignment sequence
        according to the project guidelines (60 chars)
        """
        import math
        seq_one = self.seq_one[::-1]
        seq_two = self.seq_two[::-1]
        seq_match = self.seq_match[::-1]
        align_len = len(seq_match)
        
        print '\nEdit Distance = {}'.format(self.edit_distance)
        print 'Optimal Alignment: \n'

        # If alignment > 60 chars, break into chunks
        if (align_len > 60):
            chunks = int(math.ceil(float(align_len) / 60))
            for i in range(0, chunks):
                start = i * 60
                end = (i + 1) * 60
                print seq_one[start:end]
                print seq_match[start:end]
                print seq_two[start:end]
        else:
            print seq_one
            print seq_match
            print seq_two
        print
    
    def local_alignment(self):
        DP = self.DP[1:, 1:]
        indices = np.where(DP == DP.argmax())
        x_y_coords = zip(indices[0], indices[1])
        print x_y_coords


edit_distance = SequenceAlignment(file_1, file_2)
edit_distance.backtrace()
edit_distance.print_data()
edit_distance.local_alignment()