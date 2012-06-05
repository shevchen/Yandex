from argparse import ArgumentError

class OpenMap:
    __loadFactor = 0.75
    __capacityMult = 2
    
    def __init__(self, items=20):
        if items < 0:
            raise ArgumentError(items)
        pass
        
    def __rebuild(self, items):
        pass
    
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