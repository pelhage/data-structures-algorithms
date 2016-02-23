/***

I intend to make the equivalent program as `editDist.py` 
but with JavaScript instead. This will be a fun exercise
in showing the differences and similiarities of 
the two languages.

Status: Not complete.
***/


Array.matrix = function(numRows, numCols, initial) {
  var arr = [];
  for (var i = 0; i < numRows; i++) {
    var columns = [];
    for (var j = 0; j < numCols; j++) {
      columns[j] = initial;
    }
    arr[i] = columns;
  }
  return arr;
};




function SequenceAlignment(fileOne, fileTwo) {
  this.fileOne = fileOne;
  this.fileTwo = fileTwo;
  this.seqOneLen = fileOne.length;
  this.seqTwoLen = fileTwo.length;
  this.penalty = 1;
  this.match = 0;
}

SequenceAlignment.prototype._initData = function() {
  // Initialize Dynamic Programming matrix.
  // Seq one on x axis, seq two on y axis
  var DP = Array.matrix(this.seqTwoLen, this.seqOneLen, 0);
  DP[0, 0] = 0;
  for (var i = 1; i <= this.seqOneLen; i++) {
    DP[0, i] = i;
  }
  for (var j = 1; j <= this.seqTwoLen; j++) {
    DP[j, 0] = j;
  } 
  // Calculate scores by comparing seq1 to seq2
  for (var i = 1; i <= this.seqOneLen; i++) {
    for (var j = 1; i <= this.seqTwoLen; j++) {
      // If the chars are same, set val to 
      // diagonal neighbor, else set to min
      DP[j, i] = min(
        DP[j-1, i] + self.penalty, // above
        DP[j, i-1] + self.penalty, // left
        DP[j-1, i-1] + self._match_score(j,i)); // diagonal)
    }
  }
  this.DP = DP;
  this.editDistance = DP[this.seqTwoLen-1,
                         this.seqOneLen-1];
  return;
};

SequenceAlignment.prototype._matchScore = function(y, x) {
  return this.fileOne[x - 1] === this.fileTwo[y - 1] ? 0 : 1;
};

SequenceAlignment.prototype.printData = function() {

};

SequenceAlignment.prototype.backtrace = function() {

};

SequenceAlignment.prototype.alignment = function() {

};

var editDistance = new SequenceAlignment(fileOne, fileTwo);
editDistance.backtrace();
editDistance.print_data();
editDistance.local_alignment();