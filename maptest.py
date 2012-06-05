import unittest
import random
import time
import sys
from chainmap import ChainMap
from openmap import OpenMap

class MapTest(unittest.TestCase):
    def tearDown(self):
        print >> sys.stderr, "\nTime: %.4f seconds" % (time.time() - self.start)
    
    def testSequentialInsert(self):
        n = 100000
        for i in xrange(n):
            self.mydict[i] = 2 * i
        self.assertEqual(len(self.mydict), n)
        
    def testRandomInsert(self):
        n = 100000
        maxv = 1000000000
        for _ in xrange(n):
            self.mydict[random.randint(0, maxv)] = random.randint(0, maxv)
    
    def testEqualInsertAndGet(self):
        s = "abc"
        n = 100000
        for i in xrange(n):
            self.mydict[s] = i
        self.assertEqual(len(self.mydict), 1)
        self.assertEqual(self.mydict[s], n - 1)        
    
    def testInsertAndGet(self):
        n = 100000
        for i in xrange(n):
            self.mydict[-2 * i] = 3 * i
            self.assertEqual(self.mydict[-2 * i], 3 * i)
        for i in xrange(n):
            self.assertEqual(self.mydict[-2 * i], 3 * i)

    def testLookupAndIteration(self):
        n = 200
        for i in xrange(n):
            self.mydict[i] = i
            elemSum = 0
            for (_, value) in self.mydict.iteritems():
                elemSum += value
            self.assertEqual(elemSum, i * (i + 1) / 2)
        for i in xrange(n):
            self.assertTrue(i in self.mydict)
                        
    def testDeletion(self):
        n = 100000
        for i in xrange(n):
            self.mydict[i] = i - 1
        self.assertEqual(len(self.mydict), n)
        for i in xrange(n):
            del self.mydict[i]
            self.assertEqual(len(self.mydict), n - i - 1)
    
    def testIterationAndDeletion(self):
        n = 10000
        for i in xrange(n):
            self.mydict[i & (i + 1)] = i ^ (-i)
        tempList = []
        for i in self.mydict:
            self.assertTrue(i in self.mydict)
            tempList.append(i)
        for i in tempList:
            del self.mydict[i]
        self.assertEqual(len(self.mydict), 0)
       
    def testClear(self):
        n = 100000
        for i in xrange(n):
            self.mydict[i] = i
        self.assertEqual(len(self.mydict), n)
        self.mydict.clear()
        self.assertEqual(len(self.mydict), 0)
        
    def testErrors(self):
        n = 1000
        for i in xrange(n):
            self.assertFalse(i in self.mydict)
            self.assertRaises(KeyError, self.mydict.__getitem__, i)
            self.mydict[i] = i
        for i in xrange(n):
            self.assertTrue(i in self.mydict)
            del self.mydict[i]
            self.assertFalse(i in self.mydict)
            self.assertRaises(KeyError, self.mydict.__getitem__, i)
        
class DictTest(MapTest):
    def setUp(self):
        self.mydict = dict()
        self.start = time.time()
        
class ChainMapTest(MapTest):
    def setUp(self):
        self.mydict = ChainMap()
        self.start = time.time()

class OpenMapTest(MapTest):
    def setUp(self):
        self.mydict = OpenMap()
        self.start = time.time()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DictTest))
    suite.addTest(unittest.makeSuite(ChainMapTest))
    suite.addTest(unittest.makeSuite(OpenMapTest))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
