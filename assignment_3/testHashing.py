import random
from my_array import Array
from HashTable_LinearProbing import HashTable_LinearProbing
# from HashTable_QuadraticProbing import HashTable_QuadraticProbing
from HashTable_DoubleHashing import HashTable_DoubleHashing

def main() :
    
    size = 1000003    # this is a prime number
    
    # generate random data to be inserted
    data = Array(size)     
    for i in range(size) :
        data[i] = random.randint(1, 1000000000)
    load = [.25, .5, .67, .8, .95]

    for load_percent in load:
        # Create new Hash Table
        h_lp = HashTable_LinearProbing(size)
        h_dh = HashTable_DoubleHashing(size)
        num_load_before = int(load_percent * size - 1)
        num_load_after = int((load_percent + 0.01) * size)
        
        for i in range(1, num_load_before):
            h_lp.insert(data[i], 'Item')
            h_dh.insert(data[i], 'Item')
        slots_accessed_before = h_lp.slotsAccessed
        slots_dh_accessed_before = h_dh.slotsAccessed
        for i in range(num_load_before, num_load_after):
            h_lp.insert(data[i], 'Item')
            h_dh.insert(data[i], 'Item')
        slots_accessed_after = h_lp.slotsAccessed
        slots_dh_accessed_after = h_dh.slotsAccessed
        
        print 'Load = {}'.format(load_percent)
        print 'Linear probing {}'.format(round(float((slots_accessed_after - slots_accessed_before)/(0.01 * size)), 2))
        print 'Double hashing {}'.format(round(float((slots_dh_accessed_after - slots_dh_accessed_before)/(0.01 * size)), 2))
        print 
    # for each load[i] 
    #    insert all elements data[j] up to i = load[i] * size - 1
    #    check average of slots accessed for inserting the next 1% of data, 
    #    that is, data[j], j from load[i] * size .. (load[i] + 0.01) * size
    #            you need to check the number of slots accessed before and after,
    #            compute the difference, and divide it by the number of elements
    #            inserted, that is, 0.01 * size


main()
    
     
         
     
     