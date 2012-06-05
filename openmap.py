from argparse import ArgumentError

class OpenMap:
    __loadFactor = 0.75
    __capacityMult = 2
    
    def __init__(self, items=20):
        if items <= 0:
            raise ArgumentError(items)
        self.capacity = items
        self.keys = 0
        self.array = [[] for _ in xrange(self.capacity)]
        
    def __rebuild(self, items):
        oldArray = self.array
        oldCapacity = self.capacity
        self.array = [[] for _ in xrange(items)]
        self.capacity = 0
        for i in xrange(oldCapacity):
            for k, v in oldArray[i]:
                self.__setitem__(k, v)
    
    def __len__(self):
        return self.keys
    
    def __getitem__(self, key):
        pass
    
    def __setitem__(self, key, value):
        pass
    
    def __delitem__(self, key):
        pass   
    
    def __contains__(self, key):
        pass
    
    def clear(self):
        for i in xrange(self.capacity):
            del self.array[i][:]
        self.keys = 0
            
    def iteritems(self):
        for i in xrange(self.capacity):
            for t in self.array[i]:
                yield t
