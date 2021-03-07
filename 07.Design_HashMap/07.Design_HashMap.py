'''
	Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.

'''

class MyHashMap:
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]
        
    def put(self, key, value):
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t][i] = (k, value)
                return
        self.arr[t].append((key, value))

    def get(self, key):
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.arr[t]):
            if k == key: return v
        return -1

    def remove(self, key: int):
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t].remove((k,v))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)