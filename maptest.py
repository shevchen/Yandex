import unittest
import random
from chainmap import ChainMap
from openmap import OpenMap

class MapTest(unittest.TestCase):
    def testSequentialInsert(self):
        n = 50000
        for i in xrange(n):
            self.mydict[i] = 2 * i
        self.assertEqual(len(self.mydict), n)
        
    def testRandomInsert(self):
        n = 50000
        maxv = 1000000000
        for _ in xrange(n):
            self.mydict[random.randint(0, maxv)] = random.randint(0, maxv)
    
    def testEqualInsertAndGet(self):
        s = "abc"
        n = 50000
        for i in xrange(n):
            self.mydict[s] = i
        self.assertEqual(len(self.mydict), 1)
        self.assertEqual(self.mydict[s], n - 1)
        self.assertRaises(KeyError, self.mydict[0])
    
    def testInsertAndGet(self):
        n = 50000
        for i in xrange(n):
            self.mydict[-2 * i] = 3 * i
            self.assertEqual(self.mydict[-2 * i], 3 * i)
        for i in xrange(n):
            self.assertEqual(self.mydict[-2 * i], 3 * i)
            self.assertRaises(KeyError, self.mydict[i + 1])

    def testLookupAndIteration(self):
        n = 100
        for i in xrange(n):
            self.mydict[i] = i
            elemSum = 0
            for (_, value) in self.mydict.iteritems():
                elemSum += value
            self.assertEqual(elemSum, i * (i + 1) / 2)
        for i in xrange(n):
            self.assertTrue(i in self.mydict)
            self.assertFalse(i + n in self.mydict)
            
    def testDeletion(self):
        n = 50000
        for i in xrange(n):
            self.assertFalse(i in self.mydict)
            self.mydict[i] = i - 1
            self.assertTrue(i in self.mydict)
            del self.mydict[i]
            self.assertFalse(i in self.mydict)
            self.assertEqual(len(self.mydict), 0)
    
    def testIterationAndDeletion(self):
        n = 50000
        for i in xrange(n):
            self.mydict[i & (i + 1)] = i ^ (-i)
        for i in self.mydict:
            self.assertTrue(i in self.mydict)
        for i in xrange(n):
            if i in self.mydict:
                del self.mydict[i]
        self.assertEqual(len(self.mydict), 0)
        
    def testClear(self):
        n = 50000
        for i in xrange(n):
            self.mydict[i] = i
        self.assertEqual(len(self.mydict), n)
        self.mydict.clear()
        self.assertEqual(len(self.mydict), 0)
        
class DictTest(MapTest):
    def setUp(self):
        self.mydict = dict()
        
class ChainMapTest(MapTest):
    def setUp(self):
        self.mydict = ChainMap()

class OpenMapTest(MapTest):
    def setUp(self):
        self.mydict = OpenMap()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DictTest))
    suite.addTest(unittest.makeSuite(ChainMapTest))
    suite.addTest(unittest.makeSuite(OpenMapTest))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())
