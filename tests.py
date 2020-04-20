#!/usr/bin/env python
import unittest
from seqlen import sum_files, fileset

class seqlenTests(unittest.TestCase):
    def testsum(self):
        #Tests if sum is as expected
        self.assertEqual(sum_files(fileset('data')), 1324172)

if __name__ == '__main__':
    unittest.main()