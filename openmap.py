from argparse import ArgumentError

class OpenMap:
    __loadFactor = 0.75
    __capacityMult = 2
    
    def __assign(self, items):
        self.capacity = items        
        self.array = [None] * self.capacity
        self.used = [False] * self.capacity
        self.keys = 0
    
    def __init__(self, items=20):
        if items <= 0:
            raise ArgumentError(items)
        self.__assign(items)
        
    def __rebuild(self, items):
        oldArray = self.array
        oldUsed = self.used
        self.__assign(items)
        for i, (k, v) in enumerate(oldArray):
            if oldUsed[i]:
                self.__setitem__(k, v)
    
    def __len__(self):
        return self.keys
    
    def __getitem__(self, key):
        h = hash(key)
        for i in xrange(self.capacity):
            index = (h + i) % self.capacity
            if self.used[index] and self.array[index][0] == key:
                return self.array[index][1]
        raise KeyError(key)
    
    def __setitem__(self, key, value):
        h = hash(key)
        for i in xrange(self.capacity):
            index = (h + i) % self.capacity
            if not self.used[index]:
                self.array[index] = key, value
                self.used[index] = True
                self.keys += 1
                if self.keys > self.__loadFactor * self.capacity:
                    self.__rebuild(self.__capacityMult * self.capacity)
                return
            if self.array[index][0] == key:
                self.array[index] = key, value
                return
    
    def __delitem__(self, key):
        h = hash(key)
        for i in xrange(self.capacity):
            index = (h + i) % self.capacity
            if self.used[index] and self.array[index][0] == key:
                self.used[index] = False
                self.keys -= 1
                return
        raise KeyError(key)
    
    def __contains__(self, key):
        h = hash(key)
        for i in xrange(self.capacity):
            index = (h + i) % self.capacity
            if self.used[index] and self.array[index][0] == key:
                return True
        return False
    
    def clear(self):
        for i in xrange(self.capacity):
            self.used[i] = False
        self.keys = 0
        
    def __iter__(self):
        size = self.keys
        for i, t in enumerate(self.array):
            if self.used[i]:
                if size != self.keys:
                    raise RuntimeError("dictionary changed size during iteration")
                yield t[0]

    def iteritems(self):
        size = self.keys
        for i, t in enumerate(self.array):
            if self.used[i]:
                if size != self.keys:
                    raise RuntimeError("dictionary changed size during iteration")
                yield t
