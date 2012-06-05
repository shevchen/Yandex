from argparse import ArgumentError

class ChainMap:
    __loadFactor = 0.75
    __capacityMult = 2
    
    def __init__(self, items=20):
        if items <= 0:
            raise ArgumentError(items)
        self.capacity = items
        self.keys = 0
        self.array = [[] for _ in xrange(self.capacity)]
        
    def __rebuild(self, items):
        array = [[] for _ in xrange(items)]
        for i in xrange(self.capacity):
            for k, v in self.array[i]:
                array[hash(k) % items].append((k, v))
        self.array = array
        self.capacity = items
    
    def __len__(self):
        return self.keys
    
    def __getitem__(self, key):
        for k, v in self.array[hash(key) % self.capacity]:
            if k == key:
                return v
        raise KeyError(key)
    
    def __setitem__(self, key, value):
        chain = self.array[hash(key) % self.capacity]
        for i, (k, _) in enumerate(chain):
            if k == key:
                list[i] = value
                return
        chain.append((key, value))
        self.keys += 1
        if self.keys > self.__loadFactor * self.capacity:
            self.__rebuild(self.__capacityMult * self.capacity)
    
    def __delitem__(self, key):
        chain = self.array[hash(key) % self.capacity]
        for i, (k, _) in enumerate(chain):
            if k == key:
                if i == len(chain) - 1:
                    chain.pop()
                else:
                    chain[i] = chain.pop()
                self.keys -= 1
                return
        raise KeyError(key)
    
    def __contains__(self, key):
        for k, _ in self.array[hash(key) % self.capacity]:
            if k == key:
                return True
        return False
    
    def clear(self):
        for i in xrange(self.capacity):
            del self.array[i][:]
        self.keys = 0
            
    def iteritems(self):
        for i in xrange(self.capacity):
            for t in self.array[i]:
                yield t
