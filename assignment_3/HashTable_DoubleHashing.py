from my_array import Array

class _MapEntry :                       
    def __init__( self, key, value ):
        self.key = key
        self.value = value                  

UNUSED = None                     # slot never used                 
EMPTY = _MapEntry( None, None )     # key removed

class HashTable_DoubleHashing : 
    def __init__( self, size ):
        self._table = Array( size ) 
        self._table.clear( None )
        self._size = size
        self._count = 0
        self.slotsAccessed = 0
      
    def __len__( self ):
        return self._count

    def __contains__( self, key ):
        ( found, slot ) = self._findSlot( key)
        return found
    
    # insert (if not already in table)
    # return True/False is key inserted/not
    def insert( self, key, value ):
        ( found, slot ) = self._findSlot( key )
        if not found :
            self._table[slot] = _MapEntry( key, value )
            self._count += 1
        return not found
   
    # remove (key, value) (if in the table)
    # return True/False is key removed/not
    def remove( self, key ):
        ( found, slot ) = self._findSlot( key )
        if found :
            self._table[slot] = EMPTY
            self._count -= 1
        return found

    # find the slot where a key is or should be inserted
    # return (True/False, slot) if key was found/not
    def _findSlot(self, key):
        home = self._hash1(key)
        i = 0
        slot = (home + i) % self._size
        # IF WE FOUND IT WITHOUT COLLISION, NO NEED TO DOUBLE HASH
        self.slotsAccessed += 1
        if (self._table[slot] == UNUSED or \
            (self._table[slot] != EMPTY and \
            self._table[slot].key == key)):
            if self._table[slot] == UNUSED:
                return (False, slot)
            elif self._table[slot] != EMPTY and self._table[slot].key == key:
                return (True, slot)            
        else:
            i = 1
            # Iterate through it once
            while (i <= self._size):
                slot = (home + i * self._hash2(key)) % self._size
                i += 1
                self.slotsAccessed += 1
                # If we come across an unused slot, it means that its
                # Never been added before, so we should add it here
                if self._table[slot] == UNUSED:
                    return (False, slot)
                elif self._table[slot] != EMPTY and self._table[slot].key == key:
                    return (True, slot)        
        
    # compute first slot attempted
    def _hash1( self, key ):
        return abs(hash(key)) % self._size
    
    # compute step for double hashing
    def _hash2( self, key ):
        return 1 + abs(hash(key)) % (self._size - 2)    
