# Implementation of the algorithm for validating balanced brackets in
# a C++ source file.

class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)
     def __getitem__(self, key):
         return self.items[key]

def isValidSource( srcfile ):
  srcfile = open(srcfile, 'r')
  s = Stack() 
  for line in srcfile :
    for token in line :
      if token in "{[(" :
        s.push( token )
        print("push " + token)
      elif token in "}])" :
        if s.isEmpty() :
          return False
        else :
          left = s.pop()
          print("pop " + left)
          if (token == "}" and left != "{") or \
             (token == "]" and left != "[") or \
             (token == ")" and left != "(") :
            return False
               
  return s.isEmpty()