from my_array import Array

class _MapEntry :                       
    def __init__(self, key, value):
        self.key = key
        self.value = value                  

UNUSED = None                     # slot never used                 
EMPTY = _MapEntry(None, None)     # key removed

class HashTable_LinearProbing : 
    def __init__(self, size):
        self._table = Array(size) 
        self._table.clear(UNUSED)
        self._size = size
        self._count = 0
        self.slotsAccessed = 0
      
    def __len__(self):
        return self._count

    def __contains__(self, key):
        (found, slot) = self._findSlot(key)
        return found
    
    # insert (if not already in table)
    # return True/False is key inserted/not
    def insert(self, key, value):
        (found, slot) = self._findSlot(key)
        if not found :
            self._table[slot] = _MapEntry(key, value)
            self._count += 1
        return not found
   
    # remove (key, value) (if in the table)
    # return True/False is key removed/not
    def remove(self, key):
        (found, slot) = self._findSlot(key)
        if found :
            self._table[slot] = EMPTY
            self._count -= 1
        return found

    # find the slot where a key is or should be inserted
    # return (True/False, slot) if key was found/not
    def _findSlot(self, key):
        home = self._hash1(key)
        i = 0
        
        # Iterate through it once
        while (i <= self._size):
            slot = (home + i) % self._size
            self.slotsAccessed += 1
            # If we come across an unused slot, it means that its
            # Never been added before, so we should add it here
            if self._table[slot] == UNUSED:
                return (False, slot)
            elif self._table[slot] != EMPTY and self._table[slot].key == key:
                return (True, slot)
            i += 1
        # Iterate once more
        i = 0
        if (self._table[home] == EMPTY):
            self.slotsAccessed += 1
            return (False, slot)
        while (i < self._size):
            slot = (home + i) % self._size
            self.slotsAccessed += 1
            if self._table[slot] == EMPTY:
                return (False, slot)
            i += 1

    # compute first slot attempted
    def _hash1(self, key):                               
        return abs(hash(key)) % self._size


# ht = HashTable_LinearProbing(98)
# print ht._hash1(55)
# ht.insert(26, 'Jam')
# ht.insert(26, 'Jammy')
# ht.insert(26, 'POO')
# ht.insert(27, 'Jelly')
# ht.insert(28, 'Marmalade')
# for index, item in enumerate(range(0, ht._size)):
#     print ht._table[index]

# ht.remove(26)
# print '============'
# for item in ht._table:
#     if item:
#         print '{} {}'.format(item.value, item.key)
# print '============'
# ht.insert(26, 'PBJ')
# for item in ht._table:
#     if item:
#         print '{} {}'.format(item.value, item.key)
# print "======HELLO WORLD======="
# print ht._table[27].value
# print ht._table[26].value